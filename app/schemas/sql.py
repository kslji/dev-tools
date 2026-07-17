from pydantic import BaseModel
from typing import Optional

class SQLFormatRequest(BaseModel):
    sql: str
    keyword_case: str = "upper"  # "upper", "lower", "capitalize"
    reindent: bool = True
    indent_width: int = 2

class SQLFormatResponse(BaseModel):
    formatted_sql: str
    success: bool
    error: Optional[str] = None
