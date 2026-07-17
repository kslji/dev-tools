from pydantic import BaseModel
from typing import Optional

class YAMLRequest(BaseModel):
    yaml_str: str
    indent: int = 2

class YAMLValidateResponse(BaseModel):
    valid: bool
    error: Optional[str] = None
    error_line: Optional[int] = None
    error_column: Optional[int] = None

class YAMLFormatResponse(BaseModel):
    formatted_yaml: str
    success: bool
    error: Optional[str] = None
