from ingestion.cloner import clone_repository


repo_url = "https://github.com/psf/requests"

try:
    path = clone_repository(repo_url, "requests_repo")
    print(f"Repository cloned successfully!")
    print(f"Saved at: {path}")

except Exception as e:
    print(e)