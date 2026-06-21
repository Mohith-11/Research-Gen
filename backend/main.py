from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="ResearchGen AI",
    description="Autonomous Research Agent using LangGraph",
    version="1.0.0"
)

app.include_router(router)