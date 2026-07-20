import base64
from fastapi import APIRouter, HTTPException
from app.schemas.base64 import Base64Request, Base64Response

router = APIRouter()

@router.post("/base64/encode", response_model=Base64Response)
async def base64_encode(request: Base64Request):
    try:
        # Encode text to bytes
        input_bytes = request.text.encode(request.encoding)
        if request.url_safe:
            encoded_bytes = base64.urlsafe_b64encode(input_bytes)
        else:
            encoded_bytes = base64.b64encode(input_bytes)
        
        result_str = encoded_bytes.decode("ascii")
        return Base64Response(result=result_str, success=True)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={"error": f"Base64 encoding failed: {str(e)}", "code": "base64_encode_error"}
        )

@router.post("/base64/decode", response_model=Base64Response)
async def base64_decode(request: Base64Request):
    try:
        # Decode base64 string to bytes
        input_bytes = request.text.encode("ascii")
        if request.url_safe:
            decoded_bytes = base64.urlsafe_b64decode(input_bytes)
        else:
            # Handle possible missing padding
            missing_padding = len(request.text) % 4
            if missing_padding:
                input_bytes += b'=' * (4 - missing_padding)
            decoded_bytes = base64.b64decode(input_bytes)
        
        result_str = decoded_bytes.decode(request.encoding)
        return Base64Response(result=result_str, success=True)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={"error": f"Base64 decoding failed: {str(e)}", "code": "base64_decode_error"}
        )
