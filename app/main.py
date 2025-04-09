import os

from dotenv import load_dotenv
from fastapi import FastAPI
from mangum import Mangum

from app.router.chat_router import router as chat_router
from app.router.survey_generate_router import router as survey_generate_router

app = FastAPI(docs_url="/", redoc_url="/redoc")

load_dotenv()
ai_server_api_key = os.getenv("AI_SERVER_API_KEY")


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


app.include_router(survey_generate_router)
app.include_router(chat_router)

Handler = Mangum(app)
