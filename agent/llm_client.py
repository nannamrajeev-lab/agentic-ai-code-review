import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def get_openai_client():
    """
    Return OpenAI client
    if API key exists.
    """

    api_key = os.getenv(
        "OPENAI_API_KEY"
    )

    if not api_key:
        return None

    return OpenAI(
        api_key=api_key
    )


def review_code(prompt: str):
    """
    Run LLM review.

    Falls back gracefully
    if API key or quota
    is unavailable.
    """

    client = (
        get_openai_client()
    )

    # No API key
    if client is None:

        return {
            "comments": [
                {
                    "issue":
                    "Mock review: "
                    "Consider reviewing "
                    "this code block",

                    "confidence":
                    75,

                    "severity":
                    "medium"
                }
            ]
        }

    try:

        response = (
            client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role":
                        "system",

                        "content":
                        "You are an expert "
                        "AI code reviewer."
                    },
                    {
                        "role":
                        "user",

                        "content":
                        prompt
                    }
                ]
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )

    except Exception as e:

        print(
            f"LLM Error: {e}"
        )

        # Fallback if quota fails
        return {
            "comments": [
                {
                    "issue":
                    "Mock review: "
                    "Potential improvement "
                    "identified",

                    "confidence":
                    72,

                    "severity":
                    "low"
                }
            ]
        }