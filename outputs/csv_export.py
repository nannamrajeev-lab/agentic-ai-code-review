import pandas as pd


def export_to_csv(data, file_name="review_results.csv"):
    """
    Export review results to CSV.
    """

    comments = data.get("comments", [])

    df = pd.DataFrame(comments)

    df.to_csv(
        file_name,
        index=False
    )

    return file_name