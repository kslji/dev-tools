import sqlparse
from fastapi import APIRouter
from app.schemas.sql import SQLFormatRequest, SQLFormatResponse

router = APIRouter()

@router.post("/sql/format", response_model=SQLFormatResponse)
async def format_sql(request: SQLFormatRequest):
    try:
        formatted = sqlparse.format(
            request.sql,
            reindent=request.reindent,
            keyword_case=request.keyword_case,
            indent_width=request.indent_width
        )
        return SQLFormatResponse(formatted_sql=formatted, success=True)
    except Exception as e:
        return SQLFormatResponse(formatted_sql="", success=False, error=str(e))
