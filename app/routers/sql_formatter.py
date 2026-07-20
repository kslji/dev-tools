import sqlparse
from fastapi import APIRouter, HTTPException
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
        raise HTTPException(
            status_code=400,
            detail={"error": f"Invalid SQL: {str(e)}", "code": "invalid_sql"}
        )
