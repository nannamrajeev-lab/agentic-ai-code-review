from git import Repo
from pathlib import Path
import shutil


def clone_repository(repo_url: str, repo_name: str = "repo") -> str:
    """
    Clone a GitHub repository into temp_repos.
    Returns the local path of the cloned repo.
    """

    temp_path = Path("temp_repos") / repo_name

    # Remove existing repo if already exists
    if temp_path.exists():
        shutil.rmtree(temp_path)

    try:
        Repo.clone_from(repo_url, temp_path)
        return str(temp_path)

    except Exception as e:
        raise Exception(f"Failed to clone repository: {e}")