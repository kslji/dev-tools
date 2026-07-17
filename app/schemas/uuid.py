from pydantic import BaseModel

class UUIDResponse(BaseModel):
    uuids: list[str]
