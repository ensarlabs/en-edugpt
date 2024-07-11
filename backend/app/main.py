from fastapi import FastAPI
from .api.v1 import document, thread, assistant, user

app = FastAPI()

app.include_router(document.router, prefix="/api/v1", tags=["documents"])
app.include_router(thread.router, prefix="/api/v1", tags=["threads"])
app.include_router(assistant.router, prefix="/api/v1", tags=["assistants"])
app.include_router(user.router, prefix="/api/v1", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application with PostgreSQL and OpenAI integration"}
