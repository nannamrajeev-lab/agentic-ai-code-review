import json
from schemas.review_schema import ReviewResponse


def parse_llm_response(response_text):
    """
    Parse and validate LLM JSON response.
    """

    try:
        data = json.loads(response_text)

        validated_response = ReviewResponse(**data)

        return validated_response.model_dump()

    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by LLM"
        }

    except Exception as e:
        return {
            "error": str(e)
        }