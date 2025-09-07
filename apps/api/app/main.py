from fastapi import FastAPI
from app.api.endpoints import login, password_reset, google_auth, staff
from app.core.config import settings

app = FastAPI(title="CredKit API")

app.include_router(login.router, prefix=settings.API_V1_STR, tags=["login"])
app.include_router(password_reset.router, prefix=f"{settings.API_V1_STR}/password", tags=["password"])
app.include_router(google_auth.router, prefix=settings.API_V1_STR, tags=["google-auth"])
app.include_router(staff.router, prefix=settings.API_V1_STR, tags=["staff"])

@app.get("/")
async def root():
    return {"message": "CredKit API is running"}
