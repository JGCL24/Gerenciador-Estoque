"""Simple runtime prerequisite checker for the backend."""
import sys

REQUIRED = [
    ("fastapi", "FastAPI"),
    ("uvicorn", "Uvicorn"),
    ("sqlmodel", "SQLModel"),
]

ok = True
print("Checking backend prerequisites...")
print("Python: ", sys.version.split()[0])

for pkg, name in REQUIRED:
    try:
        __import__(pkg)
        print(f"  {name}: installed")
    except Exception:
        print(f"  {name}: MISSING (run: pip install {pkg})")
        ok = False

if not ok:
    print("\nSome required packages are missing. Install them with: pip install -r requirements.txt")
    sys.exit(2)

print("All backend prerequisites appear satisfied.")
