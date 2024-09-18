from fastapi import FastAPI
from app.router.survey_generate_router import router as survey_generate_router

app = FastAPI(docs_url='/', redoc_url='/redoc')

app.include_router(survey_generate_router)