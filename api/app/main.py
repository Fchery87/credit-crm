from fastapi import FastAPI

app = FastAPI(
    title="CredKit CRM API",
    description="The API for the CredKit CRM application.",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "CredKit CRM API"}
