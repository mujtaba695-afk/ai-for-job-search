---
name: folder-watcher
description: >
  Automatically monitors folders for any file activity (create, modify, delete) and triggers
  backup/sync actions. Saves snapshots of folder contents when changes are detected and notifies
  the user when everything is safely stored. Use when the user wants automatic folder monitoring,
  real-time backup of work files, change detection for project folders, or automated save-on-change
  behavior for any directory.
---

# Folder Watcher — Automatic Change Detection & Backup

## How It Works

1. **Start watching** a specified folder (recursive or top-level)
2. **Detect changes** — new files, modifications, deletions
3. **Auto-save** — backup/sync when activity detected
4. **Notify** — inform user when everything is saved

## Usage

### Start Watching
```bash
# Watch the job-search-results folder
python3 scripts/folder_watcher.py /path/to/folder --backup /path/to/backup

# Watch with custom interval (default: 5 seconds)
python3 scripts/folder_watcher.py /path/to/folder --interval 10

# Watch and sync to memory folder
python3 scripts/folder_watcher.py /path/to/folder --memory
```

### Via Conversation
Tell the assistant:
- "Watch my job search folder"
- "Auto-save changes in my project folder"
- "Monitor this folder and notify me when saved"

## Configuration

The watcher can be configured to:
- **Backup location**: Where to save snapshots
- **Watch interval**: How often to check for changes (default: 5s)
- **File filters**: Watch only specific file types
- **Notification**: Whether to notify on each save
- **Memory integration**: Save to OpenClaw memory system

## Output

When changes are detected:
```
🔔 Change Detected: [folder]
- New file: new-resume.pdf
- Modified: job-listings.md
- Deleted: old-notes.txt

✅ Backup saved to: /path/to/backup/[timestamp]/
📝 Memory updated
```

## Rules
- Always verify write permissions before starting
- Don't watch system/temp folders
- Use checksums to detect real changes (not just timestamps)
- Compress backups to save space
- Keep backup history (last 10 snapshots)
