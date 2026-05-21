from schemas.response_parser import parse_llm_response


fake_response = """
{
  "comments": [
    {
      "file": "auth.py",
      "line": 42,
      "category": "security",
      "issue": "Possible SQL injection",
      "severity": "high",
      "confidence": 91,
      "suggestion": "Use parameterized queries",
      "reasoning": "User input enters SQL query directly"
    }
  ]
}
"""

result = parse_llm_response(fake_response)

print(result)