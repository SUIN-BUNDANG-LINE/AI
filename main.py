from fastapi import FastAPI
from app.router.survey_generate_router import router as survey_generate_router

app = FastAPI()

app.include_router(survey_generate_router)