import json


def build_review_prompt(code_chunk):
    """
    Build structured prompt for LLM code review.
    """

    schema = {
        "comments": [
            {
                "file": "string",
                "line": "integer",
                "category": "security | bug | performance | maintainability",
                "issue": "string",
                "severity": "low | medium | high",
                "confidence": "integer (0-100)",
                "suggestion": "string",
                "reasoning": "string"
            }
        ]
    }

    prompt = f"""
You are a senior software engineer performing a code review.

Review the code for:
- security issues
- bugs
- performance issues
- maintainability concerns

IMPORTANT RULES:
1. Return VALID JSON ONLY.
2. Follow the schema exactly.
3. If uncertain, confidence must be below 50.
4. Do not invent issues without evidence.

JSON Schema:
{json.dumps(schema, indent=2)}

Code Metadata:
File: {code_chunk['file']}
Type: {code_chunk['type']}
Name: {code_chunk['name']}
Lines: {code_chunk['start_line']} - {code_chunk['end_line']}
Imports: {code_chunk['imports']}

Code:
{code_chunk['code']}
"""

    return prompt