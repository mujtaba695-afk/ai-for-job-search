#!/usr/bin/env python3
"""
run_job_pipeline.py — Unified CLI runner for executive-job-search-and-tailor skill.
"""
import os
import sys
import json
import argparse
import subprocess

WORKSPACE = "/Users/mujtabasajawal/Downloads/Resume"
CAREER_OPS = os.path.join(WORKSPACE, "career-ops")
JOB_SEARCH = os.path.join(WORKSPACE, "performance-marketing-job-search")

def run_cmd(cmd, cwd=WORKSPACE):
    res = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error executing: {cmd}\n{res.stderr}", file=sys.stderr)
    else:
        print(res.stdout)
    return res

def scan_jobs(since_days=14, limit=50, dry_run=False):
    print(f"=== Scanning ATS Boards (Last {since_days} Days) ===")
    dry_flag = " --dry-run" if dry_run else ""
    cmd = f"node scan-ats-full.mjs --since {since_days} --limit {limit}{dry_flag}"
    run_cmd(cmd, cwd=CAREER_OPS)

def sync_sheet(sheet_id="1ExQVMpxpCAUXjYtbnR7DvRoHHHEJlhnR2AWx2rGtG4E"):
    print(f"=== Syncing Google Sheet ({sheet_id}) ===")
    # Run build_final_sheet.py or tracker sync
    cmd = "python3 build_final_sheet.py"
    run_cmd(cmd, cwd=CAREER_OPS)
    print("Google Sheet sync completed.")

def tailor_job(job_url, company=None, role=None, arch="performance"):
    print(f"=== Tailoring Resume Package for {company or 'Target Job'} ===")
    cmd = f"python3 -m engine.apply --url '{job_url}'" if job_url else "python3 build_word_resumes.py"
    run_cmd(cmd, cwd=CAREER_OPS if not job_url else JOB_SEARCH)

def main():
    parser = argparse.ArgumentParser(description="Executive Job Search & Tailor CLI")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # Scan subcommand
    scan_parser = subparsers.add_parser("scan", help="Scan ATS boards for fresh roles")
    scan_parser.add_argument("--since", type=int, default=14, help="Recency cutoff in days")
    scan_parser.add_argument("--limit", type=int, default=50, help="Max companies per ATS")
    scan_parser.add_argument("--dry-run", action="store_true", help="Preview without writing")

    # Sync subcommand
    sync_parser = subparsers.add_parser("sync", help="Sync matches with Google Sheet")
    sync_parser.add_argument("--sheet-id", type=str, default="1ExQVMpxpCAUXjYtbnR7DvRoHHHEJlhnR2AWx2rGtG4E", help="Google Sheet ID")

    # Tailor subcommand
    tailor_parser = subparsers.add_parser("tailor", help="Build tailored DOCX & PDF packages")
    tailor_parser.add_argument("--url", type=str, help="Target Job Description URL")
    tailor_parser.add_argument("--company", type=str, help="Company name")
    tailor_parser.add_argument("--role", type=str, help="Role title")

    args = parser.parse_args()

    if args.subcommand == "scan":
        scan_jobs(since_days=args.since, limit=args.limit, dry_run=args.dry_run)
    elif args.subcommand == "sync":
        sync_sheet(sheet_id=args.sheet_id)
    elif args.subcommand == "tailor":
        tailor_job(job_url=args.url, company=args.company, role=args.role)

if __name__ == "__main__":
    main()
