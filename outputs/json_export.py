import json


def export_to_json(data, file_name="review_results.json"):
    """
    Export review results to JSON.
    """

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4
        )

    return file_name