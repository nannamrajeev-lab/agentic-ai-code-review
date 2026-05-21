from agent.confidence import adjust_confidence


sample_comment = {
    "confidence": 85,
    "issue": "Possible performance issue"
}

sample_chunk = {
    "start_line": 1,
    "end_line": 140,
    "imports": []
}

result = adjust_confidence(sample_comment, sample_chunk)

print(result)