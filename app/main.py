import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from mangum import Mangum

from app.router.chat_router import router as chat_router
from app.router.survey_generate_router import router as survey_generate_router

app = FastAPI(docs_url="/", redoc_url="/redoc")

load_dotenv()
ai_server_api_key = os.getenv("AI_SERVER_API_KEY")


@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    api_key = request.headers.get("x-api-key")
    if api_key != ai_server_api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await call_next(request)


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


app.include_router(survey_generate_router)
app.include_router(chat_router)

Handler = Mangum(app)
