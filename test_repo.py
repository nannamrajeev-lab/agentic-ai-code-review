from ingestion.cloner import clone_repository
from ingestion.file_discovery import get_python_files
from parser.ast_parser import extract_code_chunks


repo_url = "https://github.com/psf/requests"

try:
    path = clone_repository(repo_url, "requests_repo")

    print("\nRepository cloned successfully!")
    print(f"Saved at: {path}")

    files = get_python_files(path)

    print(f"\nFound {len(files)} Python files")

    first_file = files[0]

    print(f"\nAnalyzing:\n{first_file}")

    chunks = extract_code_chunks(first_file)

    print(f"\nFound {len(chunks)} code chunks:\n")

    for chunk in chunks[:5]:
        print("=" * 50)
        print(f"Type: {chunk['type']}")
        print(f"Name: {chunk['name']}")
        print(f"File: {chunk['file']}")
        print(f"Lines: {chunk['start_line']} - {chunk['end_line']}")
        print(f"Imports: {chunk['imports'][:5]}")

except Exception as e:
    print(e)