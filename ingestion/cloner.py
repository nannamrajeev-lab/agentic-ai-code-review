from git import Repo
from pathlib import Path
import shutil
import stat


def remove_readonly(func, path, _):
    """Handle Windows permission errors."""
    Path(path).chmod(stat.S_IWRITE)
    func(path)


def clone_repository(repo_url: str, repo_name: str = "repo") -> str:
    """
    Clone a GitHub repository into temp_repos.
    Returns local repo path.
    """

    temp_path = Path("temp_repos") / repo_name

    # Remove old repo safely
    if temp_path.exists():
        shutil.rmtree(temp_path, onerror=remove_readonly)

    try:
        Repo.clone_from(repo_url, temp_path)
        return str(temp_path)

    except Exception as e:
        raise Exception(f"Failed to clone repository: {e}")