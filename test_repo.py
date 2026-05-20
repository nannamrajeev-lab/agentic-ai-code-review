from ingestion.cloner import clone_repository
from ingestion.file_discovery import get_python_files


repo_url = "https://github.com/psf/requests"

try:
    path = clone_repository(repo_url, "requests_repo")

    print("\nRepository cloned successfully!")
    print(f"Saved at: {path}")

    files = get_python_files(path)

    print(f"\nFound {len(files)} Python files:\n")

    for file in files[:10]:
        print(file)

except Exception as e:
    print(e)