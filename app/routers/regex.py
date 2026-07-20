import re
from fastapi import APIRouter, HTTPException
from app.schemas.regex import RegexTestRequest, RegexTestResponse, RegexMatchDetail

router = APIRouter()

@router.post("/regex/test", response_model=RegexTestResponse)
async def test_regex(request: RegexTestRequest):
    flags = 0
    if request.ignore_case:
        flags |= re.IGNORECASE
    if request.multiline:
        flags |= re.MULTILINE
    if request.dot_all:
        flags |= re.DOTALL

    try:
        compiled_regex = re.compile(request.pattern, flags)
    except re.error as e:
        raise HTTPException(
            status_code=400,
            detail={"error": f"Invalid Regex pattern: {str(e)}", "code": "invalid_regex"}
        )

    matches = []
    # Find all matches
    for match in compiled_regex.finditer(request.text):
        groups = list(match.groups())
        group_dict = match.groupdict()
        matches.append(
            RegexMatchDetail(
                match=match.group(0),
                span=match.span(),
                groups=groups,
                group_dict=group_dict
            )
        )

    return RegexTestResponse(
        valid_pattern=True,
        matches=matches,
        match_count=len(matches)
    )
