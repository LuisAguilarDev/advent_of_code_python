"""Shim package to expose the repository-level `global_utils` package when running from `src/`.

This file dynamically loads the real `global_utils` package located at the repository root
so code running with `src` as the working directory (for example `python -m 2023.day1.index`)
can still `import global_utils.utils`.

This is intentionally small and defensive.
"""
import importlib.util
import os
import sys

# Compute repository root (two levels up from src/global_utils)
this_dir = os.path.dirname(__file__)
repo_root = os.path.abspath(os.path.join(this_dir, "..", ".."))
real_pkg_dir = os.path.join(repo_root, "global_utils")

__all__ = []

if os.path.isdir(real_pkg_dir):
    for mod_name in ("utils", "logger"):
        mod_path = os.path.join(real_pkg_dir, f"{mod_name}.py")
        if os.path.exists(mod_path):
            full_name = f"global_utils.{mod_name}"
            # avoid reloading if already present
            if full_name in sys.modules:
                module = sys.modules[full_name]
            else:
                spec = importlib.util.spec_from_file_location(
                    full_name, mod_path)
                module = importlib.util.module_from_spec(spec)
                # register early to allow intra-package imports
                sys.modules[full_name] = module
                spec.loader.exec_module(module)

            # attach as attribute on this package
            globals()[mod_name] = module
            __all__.append(mod_name)

else:
    # Nothing to load; keep package empty (imports will fail later with clear message)
    pass
