from pydantic import BaseModel
from typing import Optional

class Base64Request(BaseModel):
    text: str
    url_safe: bool = False
    encoding: str = "utf-8"

class Base64Response(BaseModel):
    result: str
    success: bool
    error: Optional[str] = None
