from pydantic import BaseModel
from typing import List


class ReviewComment(BaseModel):
    file: str
    line: int
    category: str
    issue: str
    severity: str
    confidence: int
    suggestion: str
    reasoning: str


class ReviewResponse(BaseModel):
    comments: List[ReviewComment]