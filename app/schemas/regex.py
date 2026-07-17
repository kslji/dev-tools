from pydantic import BaseModel
from typing import Optional, Any

class RegexTestRequest(BaseModel):
    pattern: str
    text: str
    ignore_case: bool = False
    multiline: bool = False
    dot_all: bool = False

class RegexMatchDetail(BaseModel):
    match: str
    span: tuple[int, int]
    groups: list[Optional[str]]
    group_dict: dict[str, Optional[str]]

class RegexTestResponse(BaseModel):
    valid_pattern: bool
    pattern_error: Optional[str] = None
    matches: list[RegexMatchDetail]
    match_count: int
