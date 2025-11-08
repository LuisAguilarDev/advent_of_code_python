import os
import sys

# Make the repository root, src and test directories available on sys.path during pytest collection
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_ROOT = os.path.join(REPO_ROOT, "src")
TEST_ROOT = os.path.join(REPO_ROOT, "test")

for p in (TEST_ROOT, SRC_ROOT, REPO_ROOT):
    if p and os.path.isdir(p) and p not in sys.path:
        # insert at front so tests import local packages before installed ones
        sys.path.insert(0, p)
