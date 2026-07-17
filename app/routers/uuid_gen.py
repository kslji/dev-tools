from fastapi import APIRouter, Query
from app.schemas.uuid import UUIDResponse

router = APIRouter()

@router.get("/uuid/generate", response_model=UUIDResponse)
async def generate_uuids(count: int = Query(1, ge=1, le=1000)):
    import uuid
    return {"uuids": [str(uuid.uuid4()) for _ in range(count)]}