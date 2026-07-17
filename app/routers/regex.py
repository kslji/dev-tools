import re
from fastapi import APIRouter
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
        return RegexTestResponse(
            valid_pattern=False,
            pattern_error=str(e),
            matches=[],
            match_count=0
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
