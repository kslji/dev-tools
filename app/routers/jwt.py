from fastapi import APIRouter, HTTPException
import jwt
from app.schemas.jwt import JWTDecodeRequest, JWTDecodeResponse, JWTEncodeRequest, JWTEncodeResponse

router = APIRouter()

@router.post("/jwt/decode", response_model=JWTDecodeResponse)
async def decode_jwt(request: JWTDecodeRequest):
    errors = []
    header = None
    payload = None
    signature_status = "Unverified"
    signature_info = {}

    # Extract header without verification first
    try:
        header = jwt.get_unverified_header(request.token)
        signature_info["algorithm"] = header.get("alg")
        signature_info["type"] = header.get("typ")
    except Exception as e:
        return JWTDecodeResponse(
            valid=False,
            errors=[f"Invalid JWT format or header: {str(e)}"],
            signature_status="Invalid"
        )

    # Decode payload
    if not request.verify:
        try:
            # Decode payload without verifying signature
            payload = jwt.decode(request.token, options={"verify_signature": False})
            return JWTDecodeResponse(
                valid=True,
                header=header,
                payload=payload,
                signature_status="Unverified",
                signature_info=signature_info
            )
        except Exception as e:
            return JWTDecodeResponse(
                valid=False,
                header=header,
                errors=[f"Failed to decode payload: {str(e)}"],
                signature_status="Unverified",
                signature_info=signature_info
            )
    else:
        # Perform signature verification
        if not request.key:
            return JWTDecodeResponse(
                valid=False,
                header=header,
                errors=["A verification key is required when verify=True"],
                signature_status="Unverified",
                signature_info=signature_info
            )
        
        algorithms = [request.algorithm] if request.algorithm else [header.get("alg", "HS256")]
        try:
            payload = jwt.decode(request.token, request.key, algorithms=algorithms)
            signature_status = "Verified"
            return JWTDecodeResponse(
                valid=True,
                header=header,
                payload=payload,
                signature_status=signature_status,
                signature_info=signature_info
            )
        except jwt.ExpiredSignatureError:
            errors.append("Token has expired (exp claim)")
            signature_status = "Failed (Expired)"
        except jwt.InvalidSignatureError:
            errors.append("Signature verification failed")
            signature_status = "Failed (Invalid Signature)"
        except jwt.InvalidTokenError as e:
            errors.append(f"Invalid token: {str(e)}")
            signature_status = "Failed (Invalid)"
        
        # If we failed verification, try to extract payload anyway for inspection
        try:
            payload = jwt.decode(request.token, options={"verify_signature": False})
        except Exception:
            pass

        return JWTDecodeResponse(
            valid=False,
            header=header,
            payload=payload,
            errors=errors,
            signature_status=signature_status,
            signature_info=signature_info
        )

@router.post("/jwt/encode", response_model=JWTEncodeResponse)
async def encode_jwt(request: JWTEncodeRequest):
    try:
        token = jwt.encode(
            payload=request.payload,
            key=request.key,
            algorithm=request.algorithm,
            headers=request.headers
        )
        return JWTEncodeResponse(token=token, success=True)
    except Exception as e:
        return JWTEncodeResponse(token="", success=False, error=str(e))

