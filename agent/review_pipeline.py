import json

from agent.prompt_builder import (
    build_review_prompt
)

from agent.confidence import (
    adjust_confidence
)

from agent.llm_client import (
    get_openai_client
)


def run_review_pipeline(chunks):
    """
    Review pipeline.
    Uses mock reviews if API fails.
    """

    all_reviews = []

    client = None

    try:
        client = get_openai_client()

    except:
        pass

    for chunk in chunks[:5]:

        prompt = build_review_prompt(
            chunk
        )

        comment = None

        # Future LLM block
        if client:
            try:
                # Will activate after credits
                pass

            except:
                pass

        # Mock fallback
        if not comment:

            comment = {
                "file": chunk["file"],
                "line": chunk[
                    "start_line"
                ],
                "category":
                "maintainability",
                "issue":
                f"Consider reviewing "
                f"{chunk['name']}",
                "severity":
                "low",
                "confidence": 82,
                "suggestion":
                "Refactor if complexity grows.",
                "reasoning":
                "Mock review before "
                "API integration."
            }

        final_comment = (
            adjust_confidence(
                comment,
                chunk
            )
        )

        all_reviews.append(
            final_comment
        )

    return {
        "comments": all_reviews
    }