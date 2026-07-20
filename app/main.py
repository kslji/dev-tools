from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import jwt, base64, uuid_gen, sql_formatter, regex, yaml_validator
from app.middleware.gateway_auth import GatewayAuthMiddleware
from app.utils.log_helper import CentralLoggerMiddleware

app = FastAPI(
    title="DevUtils Microservice",
    description="JWT decoder, Base64, UUID, SQL formatter, Regex tester, YAML validator",
    version="1.0.0"
)

app.add_middleware(GatewayAuthMiddleware)
app.add_middleware(CentralLoggerMiddleware, service_name="dev-service")

# CORS for frontend (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routers
app.include_router(jwt.router, prefix="/api/v1")
app.include_router(base64.router, prefix="/api/v1")
app.include_router(uuid_gen.router, prefix="/api/v1")
app.include_router(sql_formatter.router, prefix="/api/v1")
app.include_router(regex.router, prefix="/api/v1")
app.include_router(yaml_validator.router, prefix="/api/v1")

@app.get("/health")
async def health():
    return {"status": "ok"}