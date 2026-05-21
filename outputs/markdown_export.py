def export_to_markdown(
    data,
    file_name="review_results.md"
):
    """
    Export review results to Markdown.
    """

    comments = data.get("comments", [])

    markdown = "# AI Code Review Report\n\n"

    for comment in comments:

        markdown += (
            f"## {comment.get('file', 'Unknown File')}\n\n"
        )

        markdown += (
            f"**Line:** "
            f"{comment.get('line', 'N/A')}\n\n"
        )

        markdown += (
            f"**Issue:** "
            f"{comment.get('issue', 'N/A')}\n\n"
        )

        markdown += (
            f"**Confidence:** "
            f"{comment.get('confidence', 'N/A')}%\n\n"
        )

        markdown += "---\n\n"

    with open(
        file_name,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(markdown)

    return file_name