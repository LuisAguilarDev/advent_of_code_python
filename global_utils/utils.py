import os
import inspect


def read_file(file_name: str) -> list[str]:
    """Read a text file and return its lines.

    Resolution order for a relative `file_name`:
    1. Verify if the file exists in the route provided.
    2. Current working directory.

    Raises FileNotFoundError with a helpful message when the file cannot be found.
    """
    # Verify if the file exists in the route provided
    if os.path.exists(file_name):
        candidate_paths = [file_name]
    # Verify current working directory
    else:
        candidate_paths = []
        try:
            caller = inspect.stack()[1]
            caller_file = caller.filename
            caller_dir = os.path.dirname(os.path.abspath(caller_file))
            candidate_paths.append(caller_dir + "/" + file_name)
        except Exception:
            pass
        # try the root directory
        candidate_paths.append(os.path.abspath(file_name))
    for path in candidate_paths:
        if os.path.exists(path):
            with open(path, "r") as file:
                return file.read().splitlines()

    # nothing found -> raise clear error
    tried = '\n'.join(candidate_paths)
    raise FileNotFoundError(
        f"Could not find file '{file_name}'. Tried the following paths:\n{tried}"
    )
