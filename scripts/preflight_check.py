#!/usr/bin/env python3
"""Environment check for the AI Job Search skill library.

Uses only the standard library. Required checks fail the run; optional ones are
reported but do not, since the document-generation packages are only needed once
you start producing resumes. Pass --strict to fail on optional checks too, and
--offline to skip the network probe.
"""

import argparse
import sys
import urllib.error
import urllib.request

MIN_PYTHON = (3, 10)
ATS_PROBE_URL = "https://boards-api.greenhouse.io/v1/boards/careem/jobs"
TIMEOUT_SECONDS = 10


def check_python():
    version = ".".join(str(p) for p in sys.version_info[:3])
    if sys.version_info < MIN_PYTHON:
        required = ".".join(str(p) for p in MIN_PYTHON)
        return False, f"Python {version} (requires {required}+)"
    return True, f"Python {version}"


def check_module(module, package):
    try:
        __import__(module)
    except ImportError:
        return False, f"{package} not installed (pip install {package})"
    return True, f"{package} available"


def check_ats_connectivity():
    request = urllib.request.Request(
        ATS_PROBE_URL, headers={"User-Agent": "ai-for-job-search/1.0"}
    )
    try:
        # Default SSL context: certificates are verified.
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            if response.status != 200:
                return False, f"Greenhouse API returned HTTP {response.status}"
    except urllib.error.URLError as exc:
        return False, f"Greenhouse API unreachable ({exc.reason})"
    except OSError as exc:
        return False, f"Greenhouse API unreachable ({exc})"
    return True, "Greenhouse API reachable (HTTP 200)"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict", action="store_true", help="treat optional checks as required"
    )
    parser.add_argument(
        "--offline", action="store_true", help="skip the network connectivity probe"
    )
    args = parser.parse_args()

    checks = [
        ("Python version", check_python, True),
        ("python-docx", lambda: check_module("docx", "python-docx"), False),
        ("playwright", lambda: check_module("playwright", "playwright"), False),
    ]
    if not args.offline:
        checks.append(("Live ATS connectivity", check_ats_connectivity, False))

    print("=== Environment check ===")
    failures, warnings = [], []

    for index, (label, check, required) in enumerate(checks, start=1):
        passed, detail = check()
        if passed:
            status = "PASS"
        elif required or args.strict:
            status = "FAIL"
            failures.append(label)
        else:
            status = "OPTIONAL"
            warnings.append(label)
        print(f"[{index}/{len(checks)}] {label}: {detail} -> {status}")

    print()
    if failures:
        print(f"{len(failures)} required check(s) failed: {', '.join(failures)}")
        return 1
    if warnings:
        print(f"Ready. Optional components not installed: {', '.join(warnings)}.")
        print("Install them with 'pip install -r requirements.txt' when you need them.")
        return 0

    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
