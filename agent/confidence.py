def adjust_confidence(comment, code_chunk):
    """
    Adjust confidence score based on context quality.
    """

    confidence = comment["confidence"]

    # Penalize huge chunks (harder to reason about)
    lines = code_chunk["end_line"] - code_chunk["start_line"]

    if lines > 100:
        confidence -= 10

    # Penalize missing imports
    if not code_chunk["imports"]:
        confidence -= 5

    # Clamp score between 0 and 100
    confidence = max(0, min(confidence, 100))

    comment["final_confidence"] = confidence

    # Human verification flag
    comment["verify"] = confidence < 75

    return comment