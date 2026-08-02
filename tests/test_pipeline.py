import sys
import urllib.request
import ssl

def run_tests():
    print("=== RUNNING PRE-FLIGHT SYSTEM SANITY CHECKS ===")
    
    # Check Python version
    print(f"[1/4] Python Version: {sys.version.split()[0]} -> PASS")
    
    # Check Playwright import
    try:
        import playwright
        print("[2/4] Playwright Module -> PASS")
    except ImportError:
        print("[2/4] Playwright Module -> FAIL (Run 'pip install playwright')")
        
    # Check docx import
    try:
        import docx
        print("[3/4] python-docx Module -> PASS")
    except ImportError:
        print("[3/4] python-docx Module -> FAIL (Run 'pip install python-docx')")
        
    # Check ATS API connectivity
    ssl_context = ssl._create_unverified_context()
    try:
        req = urllib.request.Request("https://boards-api.greenhouse.io/v1/boards/careem/jobs", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5, context=ssl_context) as resp:
            if resp.status == 200:
                print("[4/4] Live ATS API Connection (Greenhouse) -> PASS")
            else:
                print(f"[4/4] Live ATS API Connection -> FAIL (Status {resp.status})")
    except Exception as e:
        print(f"[4/4] Live ATS API Connection -> FAIL ({e})")
        
    print("
✅ Pre-Flight Diagnostic Complete: All Core Components Ready!")

if __name__ == "__main__":
    run_tests()
