import yaml
from fastapi import APIRouter, HTTPException
from app.schemas.yaml import YAMLRequest, YAMLValidateResponse, YAMLFormatResponse

router = APIRouter()

@router.post("/yaml/validate", response_model=YAMLValidateResponse)
async def validate_yaml(request: YAMLRequest):
    try:
        yaml.safe_load(request.yaml_str)
        return YAMLValidateResponse(valid=True)
    except yaml.MarkedYAMLError as e:
        line = e.problem_mark.line + 1 if e.problem_mark else None
        column = e.problem_mark.column + 1 if e.problem_mark else None
        raise HTTPException(
            status_code=400,
            detail={
                "error": f"Invalid YAML: {str(e)}",
                "code": "invalid_yaml",
                "line": line,
                "column": column
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={"error": f"Invalid YAML: {str(e)}", "code": "invalid_yaml"}
        )

@router.post("/yaml/format", response_model=YAMLFormatResponse)
async def format_yaml(request: YAMLRequest):
    try:
        data = yaml.safe_load(request.yaml_str)
        formatted = yaml.dump(
            data,
            indent=request.indent,
            default_flow_style=False,
            sort_keys=False
        )
        return YAMLFormatResponse(formatted_yaml=formatted, success=True)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={"error": f"Invalid YAML for formatting: {str(e)}", "code": "invalid_yaml"}
        )
