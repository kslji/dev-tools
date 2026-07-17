from pydantic import BaseModel
from typing import Optional, Any

class JWTDecodeRequest(BaseModel):
    token: str
    key: Optional[str] = None
    algorithm: Optional[str] = None
    verify: bool = False

class JWTDecodeResponse(BaseModel):
    valid: bool
    header: Optional[dict[str, Any]] = None
    payload: Optional[dict[str, Any]] = None
    signature_status: Optional[str] = None
    errors: Optional[list[str]] = None
    signature_info: Optional[dict[str, Any]] = None

class JWTEncodeRequest(BaseModel):
    payload: dict[str, Any]
    key: str
    algorithm: str = "HS256"
    headers: Optional[dict[str, Any]] = None

class JWTEncodeResponse(BaseModel):
    token: str
    success: bool
    error: Optional[str] = None

