"""Pre-flight sanity checks for the AI Job Search toolchain.

Verifies the interpreter, the optional export dependencies, and live
connectivity to a public ATS endpoint. Exits non-zero if any check fails so
the script is usable in CI.
"""

import sys
import urllib.error
import urllib.request

MIN_PYTHON = (3, 10)
ATS_PROBE_URL = "https://boards-api.greenhouse.io/v1/boards/careem/jobs"


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
        return False, f"{package} not installed (run 'pip install {package}')"
    return True, f"{package} importable"


def check_ats_connectivity():
    request = urllib.request.Request(
        ATS_PROBE_URL, headers={"User-Agent": "ai-for-job-search/1.0"}
    )
    try:
        # Default SSL context: certificates are verified.
        with urllib.request.urlopen(request, timeout=10) as response:
            if response.status != 200:
                return False, f"Greenhouse API returned HTTP {response.status}"
    except urllib.error.URLError as exc:
        return False, f"Greenhouse API unreachable ({exc.reason})"
    except OSError as exc:
        return False, f"Greenhouse API unreachable ({exc})"
    return True, "Greenhouse API reachable (HTTP 200)"


def run_tests():
    checks = [
        ("Python version", check_python),
        ("Playwright module", lambda: check_module("playwright", "playwright")),
        ("python-docx module", lambda: check_module("docx", "python-docx")),
        ("Live ATS connectivity", check_ats_connectivity),
    ]

    print("=== Pre-flight system checks ===")
    failures = []
    for index, (label, check) in enumerate(checks, start=1):
        passed, detail = check()
        status = "PASS" if passed else "FAIL"
        print(f"[{index}/{len(checks)}] {label}: {detail} -> {status}")
        if not passed:
            failures.append(label)

    print()
    if failures:
        print(f"{len(failures)} check(s) failed: {', '.join(failures)}")
        return 1

    print("All systems operational: Playwright, ATS connectors & exporters ready.")
    return 0


if __name__ == "__main__":
    sys.exit(run_tests())
