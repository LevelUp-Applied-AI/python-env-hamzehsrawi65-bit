import sys

REQUIRED_MAJOR = 3
REQUIRED_MINOR = 11

if sys.version_info[:2] >= (REQUIRED_MAJOR, REQUIRED_MINOR):
    print("Environment OK")
else:
    raise RuntimeError(
        f"Python {REQUIRED_MAJOR}.{REQUIRED_MINOR}+ is required, "
        f"but found {sys.version.split()[0]}"
    )