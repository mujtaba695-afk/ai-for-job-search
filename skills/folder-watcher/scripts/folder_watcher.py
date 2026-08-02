#!/usr/bin/env python3
"""
Folder Watcher — Automatic Change Detection & Backup
Monitors a folder for changes and triggers backup/sync actions.
"""

import os
import sys
import time
import json
import hashlib
import shutil
import argparse
from datetime import datetime
from pathlib import Path

class FolderWatcher:
    def __init__(self, watch_path, backup_path=None, interval=5, memory_path=None):
        self.watch_path = os.path.abspath(watch_path)
        self.backup_path = backup_path or os.path.join(os.path.dirname(self.watch_path), 'backups')
        self.interval = interval
        self.memory_path = memory_path
        self.snapshot_file = os.path.join(self.backup_path, '.last_snapshot.json')
        self.running = False
        
    def get_file_hash(self, filepath):
        """Calculate MD5 hash of file content."""
        try:
            with open(filepath, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except (IOError, OSError):
            return None
    
    def get_snapshot(self):
        """Get current state of all files in watched folder."""
        snapshot = {}
        for root, dirs, files in os.walk(self.watch_path):
            # Skip hidden directories and backup folder
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'backups']
            for f in files:
                if f.startswith('.'):
                    continue
                filepath = os.path.join(root, f)
                rel_path = os.path.relpath(filepath, self.watch_path)
                try:
                    stat = os.stat(filepath)
                    snapshot[rel_path] = {
                        'hash': self.get_file_hash(filepath),
                        'size': stat.st_size,
                        'modified': stat.st_mtime
                    }
                except (IOError, OSError):
                    pass
        return snapshot
    
    def load_last_snapshot(self):
        """Load the previous snapshot from disk."""
        try:
            with open(self.snapshot_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save_snapshot(self, snapshot):
        """Save current snapshot to disk."""
        os.makedirs(self.backup_path, exist_ok=True)
        with open(self.snapshot_file, 'w') as f:
            json.dump(snapshot, f, indent=2)
    
    def detect_changes(self, old_snapshot, new_snapshot):
        """Compare two snapshots and return changes."""
        changes = {
            'added': [],
            'modified': [],
            'deleted': [],
            'has_changes': False
        }
        
        old_files = set(old_snapshot.keys())
        new_files = set(new_snapshot.keys())
        
        # New files
        for f in new_files - old_files:
            changes['added'].append(f)
        
        # Deleted files
        for f in old_files - new_files:
            changes['deleted'].append(f)
        
        # Modified files
        for f in old_files & new_files:
            if old_snapshot[f]['hash'] != new_snapshot[f]['hash']:
                changes['modified'].append(f)
        
        changes['has_changes'] = bool(changes['added'] or changes['modified'] or changes['deleted'])
        return changes
    
    def backup_folder(self, changes):
        """Create a timestamped backup of changed files."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_dir = os.path.join(self.backup_path, timestamp)
        os.makedirs(backup_dir, exist_ok=True)
        
        # Copy entire watched folder to backup
        for item in os.listdir(self.watch_path):
            if item.startswith('.') or item == 'backups':
                continue
            src = os.path.join(self.watch_path, item)
            dst = os.path.join(backup_dir, item)
            if os.path.isdir(src):
                shutil.copytree(src, dst, ignore=shutil.ignore_patterns('.*'))
            else:
                shutil.copy2(src, dst)
        
        return backup_dir
    
    def notify(self, changes, backup_path):
        """Print notification about detected changes and backup."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"\n{'='*60}")
        print(f"🔔 FOLDER ACTIVITY DETECTED — {timestamp}")
        print(f"{'='*60}")
        print(f"📁 Watching: {self.watch_path}")
        
        if changes['added']:
            print(f"\n✅ New files ({len(changes['added'])}):")
            for f in changes['added']:
                print(f"   + {f}")
        
        if changes['modified']:
            print(f"\n📝 Modified files ({len(changes['modified'])}):")
            for f in changes['modified']:
                print(f"   ~ {f}")
        
        if changes['deleted']:
            print(f"\n❌ Deleted files ({len(changes['deleted'])}):")
            for f in changes['deleted']:
                print(f"   - {f}")
        
        print(f"\n💾 Backup saved to: {backup_path}")
        print(f"✅ All changes saved and backed up!")
        print(f"{'='*60}\n")
    
    def update_memory(self, changes, backup_path):
        """Update OpenClaw memory with change log."""
        if not self.memory_path:
            return
        
        memory_file = os.path.join(self.memory_path, 'folder-changes.md')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        entry = f"\n## {timestamp}\n"
        entry += f"- Folder: `{self.watch_path}`\n"
        entry += f"- Backup: `{backup_path}`\n"
        
        if changes['added']:
            entry += f"- Added: {', '.join(changes['added'])}\n"
        if changes['modified']:
            entry += f"- Modified: {', '.join(changes['modified'])}\n"
        if changes['deleted']:
            entry += f"- Deleted: {', '.join(changes['deleted'])}\n"
        
        os.makedirs(self.memory_path, exist_ok=True)
        with open(memory_file, 'a') as f:
            f.write(entry)
    
    def cleanup_old_backups(self, max_backups=10):
        """Keep only the most recent N backups."""
        try:
            backups = sorted([
                d for d in os.listdir(self.backup_path)
                if os.path.isdir(os.path.join(self.backup_path, d)) and not d.startswith('.')
            ])
            
            while len(backups) > max_backups:
                oldest = backups.pop(0)
                oldest_path = os.path.join(self.backup_path, oldest)
                shutil.rmtree(oldest_path)
                print(f"🗑️  Cleaned up old backup: {oldest}")
        except Exception:
            pass
    
    def watch(self):
        """Main watch loop."""
        self.running = True
        print(f"👀 Watching folder: {self.watch_path}")
        print(f"💾 Backup location: {self.backup_path}")
        print(f"⏱️  Check interval: {self.interval}s")
        print(f"🔄 Monitoring started... (Ctrl+C to stop)\n")
        
        # Get initial snapshot
        current_snapshot = self.get_snapshot()
        last_snapshot = self.load_last_snapshot()
        
        # Detect any immediate changes
        if last_snapshot:
            changes = self.detect_changes(last_snapshot, current_snapshot)
            if changes['has_changes']:
                backup_path = self.backup_folder(changes)
                self.notify(changes, backup_path)
                self.update_memory(changes, backup_path)
                self.cleanup_old_backups()
        
        self.save_snapshot(current_snapshot)
        
        try:
            while self.running:
                time.sleep(self.interval)
                
                new_snapshot = self.get_snapshot()
                changes = self.detect_changes(current_snapshot, new_snapshot)
                
                if changes['has_changes']:
                    backup_path = self.backup_folder(changes)
                    self.notify(changes, backup_path)
                    self.update_memory(changes, backup_path)
                    self.cleanup_old_backups()
                    current_snapshot = new_snapshot
                    self.save_snapshot(current_snapshot)
                    
        except KeyboardInterrupt:
            print("\n\n⏹️  Watcher stopped.")
            self.running = False


def main():
    parser = argparse.ArgumentParser(description='Folder Watcher — Automatic Change Detection & Backup')
    parser.add_argument('folder', help='Path to folder to watch')
    parser.add_argument('--backup', '-b', help='Backup destination path')
    parser.add_argument('--interval', '-i', type=int, default=5, help='Check interval in seconds (default: 5)')
    parser.add_argument('--memory', '-m', action='store_true', help='Update OpenClaw memory with changes')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.folder):
        print(f"❌ Error: Folder not found: {args.folder}")
        sys.exit(1)
    
    memory_path = None
    if args.memory:
        memory_path = os.path.expanduser('~/.openclaw/workspace/memory')
    
    watcher = FolderWatcher(
        watch_path=args.folder,
        backup_path=args.backup,
        interval=args.interval,
        memory_path=memory_path
    )
    
    watcher.watch()


if __name__ == '__main__':
    main()
