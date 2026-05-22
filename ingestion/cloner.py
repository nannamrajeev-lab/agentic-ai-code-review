import shutil
import time
from pathlib import Path

from git import Repo


def clone_repository(
    repo_url: str,
    repo_name: str
):
    """
    Clone GitHub repository.

    Deletes previous clone
    before creating a new one
    to avoid Git conflicts.
    """

    temp_dir = Path(
        "temp_repos"
    )

    temp_dir.mkdir(
        exist_ok=True
    )

    repo_path = (
        temp_dir / repo_name
    )

    # Remove old repo safely
    if repo_path.exists():

        try:

            shutil.rmtree(
                repo_path
            )

            # Small delay so Windows
            # releases file locks
            time.sleep(1)

        except Exception:

            try:
                shutil.rmtree(
                    repo_path,
                    ignore_errors=True
                )

                time.sleep(1)

            except Exception:
                pass

    # Clone fresh repo
    try:

        Repo.clone_from(
            repo_url,
            str(repo_path)
        )

        return str(
            repo_path
        )

    except Exception as e:

        raise Exception(
            f"Failed to clone "
            f"repository: {e}"
        )