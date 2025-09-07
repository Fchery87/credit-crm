from fastapi import FastAPI

app = FastAPI(title="CredKit API")

@app.get("/")
async def root():
    return {"message": "CredKit API is running"}
