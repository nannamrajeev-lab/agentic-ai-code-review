from ingestion.cloner import clone_repository
from ingestion.file_discovery import get_python_files
from parser.ast_parser import extract_code_chunks
from agent.prompt_builder import build_review_prompt


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

    print(f"\nFound {len(chunks)} code chunks")

    first_chunk = chunks[0]

    prompt = build_review_prompt(first_chunk)

    print("\nGenerated Prompt:\n")
    print(prompt[:2000])

except Exception as e:
    print(e)