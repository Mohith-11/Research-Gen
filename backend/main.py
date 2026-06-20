#
from fastapi import FastAPI

app = FastAPI(
    title="ResearchGen AI",
    description="Autonomous Multi-Agent Research Assistant",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to ResearchGen AI",
        "status": "Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }