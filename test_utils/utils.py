"""Helper functions for loading and testing Advent of Code modules."""

import os
import importlib.util
import importlib
import sys
from types import ModuleType


def load_module(path: str, src_root: str = "src", reload: bool = True) -> ModuleType:
    """Load a module from the repository by filesystem path.

    Args:
        path: Path to the module or package relative to the repository root, e.g.
              "src/2023/day1" or "2023/day1" or "src/2023/day1/index.py".
        src_root: The source root directory name to add to sys.path while importing (default: "src").
        reload: If True and a module with the same generated name exists in sys.modules,
                it will be removed first so the file is re-imported.

    Returns:
        The loaded module object.

    This helper ensures that the repository `src` directory is temporarily added to
    ``sys.path`` so package-style imports inside the loaded module (like
    ``from utils.utils import ...`` or ``from global_utils.utils import ...``) resolve
    during module execution. It also registers the module under a deterministic
    name derived from the path so multiple test modules don't collide.
    """
    if not path:
        raise ValueError("path is required")

    # compute repo root by walking up until we find a directory that looks like the repo root
    def find_repo_root(start: str) -> str:
        cur = os.path.abspath(start)
        while True:
            # heuristic: repo root should contain `src` and either `global_utils` or `README.md`
            if (os.path.isdir(os.path.join(cur, "src")) and
                    (os.path.isdir(os.path.join(cur, "global_utils")) or os.path.exists(os.path.join(cur, "README.md")))):
                return cur
            parent = os.path.dirname(cur)
            if parent == cur:
                break
            cur = parent
        # fallback to three levels up from this file
        return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    repo_root = find_repo_root(os.path.dirname(__file__))

    # normalize incoming path: if it already starts with src_root, keep it; else try both
    candidate = path
    # If caller provided a path that is a file, use it directly
    if os.path.isabs(candidate):
        module_file = candidate
    else:
        # allow callers to pass either "src/2023/day1" or "2023/day1"
        parts = candidate.split("/")
        if parts[0] == src_root:
            rel_parts = parts[1:]
        else:
            rel_parts = parts

        # if candidate already contains a .py file at the end
        if rel_parts and rel_parts[-1].endswith(".py"):
            module_file = os.path.join(repo_root, *([src_root] + rel_parts))
        else:
            # treat as package/directory and assume index.py
            module_file = os.path.join(
                repo_root, src_root, *rel_parts, "index.py")

    module_file = os.path.abspath(module_file)
    if not os.path.exists(module_file):
        raise FileNotFoundError(f"Module file not found: {module_file}")

    # generate a safe module name from the path
    rel = os.path.relpath(module_file, repo_root)
    mod_name = "testmod_" + rel.replace(os.sep, "_").replace(".", "_")

    # prepare spec
    spec = importlib.util.spec_from_file_location(mod_name, module_file)

    # ensure src root is on sys.path while importing so package imports inside file resolve
    src_path = os.path.join(repo_root, src_root)
    old_sys_path = list(sys.path)
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

    # Also add repo root to sys.path for global_utils imports
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

    try:
        # optionally remove existing module to force reload
        if reload and mod_name in sys.modules:
            del sys.modules[mod_name]

        module = importlib.util.module_from_spec(spec)
        # register early to allow intra-module imports
        sys.modules[mod_name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        # restore sys.path to previous state
        sys.path[:] = old_sys_path
