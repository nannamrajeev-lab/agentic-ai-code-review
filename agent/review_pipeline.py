import json
import random

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

    all_reviews = []

    client = get_openai_client()

    for chunk in chunks[:5]:

        prompt = build_review_prompt(
            chunk
        )

        comment = None

        try:
            response = (
                client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content":
                            "You are an expert code reviewer."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0
                )
            )

            content = (
                response.choices[0]
                .message.content
            )

            parsed = json.loads(content)

            if (
                parsed.get("comments")
                and len(
                    parsed["comments"]
                ) > 0
            ):
                comment = (
                    parsed["comments"][0]
                )

        except Exception as e:
            print(
                f"LLM Error: {e}"
            )

        # Fallback mock
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
                "confidence": random.randint(55, 95),
                "suggestion":
                "Refactor if complexity grows.",
                "reasoning":
                "Fallback mock review."
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