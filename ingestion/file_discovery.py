from pathlib import Path


IGNORE_DIRS = {
    ".git",
    "venv",
    "__pycache__",
    "node_modules",
    "build",
    "dist",
    "tests",
    "docs",
    "_themes"
}


def get_python_files(repo_path: str):
    """
    Find all Python files in repo.
    Ignore unnecessary folders.
    """

    python_files = []

    for file_path in Path(repo_path).rglob("*.py"):

        # Skip ignored directories
        if any(part in IGNORE_DIRS for part in file_path.parts):
            continue

        # Skip setup.py
        if file_path.name == "setup.py":
            continue

        python_files.append(str(file_path))

    return python_files