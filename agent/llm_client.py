import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def get_openai_client():
    """
    Initialize OpenAI client.
    """

    api_key = os.getenv(
        "OPENAI_API_KEY"
    )

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY not found "
            "in .env file."
        )

    client = OpenAI(
        api_key=api_key
    )

    return client