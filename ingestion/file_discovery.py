from pathlib import Path


IGNORE_DIRS = {
    ".git",
    "__pycache__",
    "venv",
    "env",
    ".venv",
    "node_modules",
    "dist",
    "build",
    ".idea",
    ".vscode",
    "docs",
    "tests",
    "test",
    "site-packages",
    ".pytest_cache",
    ".mypy_cache",
    ".tox",
    "migrations",
    "examples"
}


IGNORE_FILES = {
    "setup.py",
    "__init__.py"
}


def get_python_files(repo_path: str):
    """
    Find Python files inside a repository
    while skipping irrelevant folders
    and problematic files.
    """

    python_files = []

    for file_path in Path(
        repo_path
    ).rglob("*.py"):

        # Skip ignored folders
        if any(
            part in IGNORE_DIRS
            for part in file_path.parts
        ):
            continue

        # Skip ignored files
        if (
            file_path.name
            in IGNORE_FILES
        ):
            continue

        # Skip hidden files
        if (
            file_path.name
            .startswith(".")
        ):
            continue

        try:
            # Verify file is readable text
            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:
                f.read(100)

            python_files.append(
                str(file_path)
            )

        except (
            UnicodeDecodeError,
            PermissionError,
            OSError
        ):
            # Ignore weird/binary files
            continue

    return python_files