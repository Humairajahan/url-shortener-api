from fastapi import FastAPI
from app.routes import url, redirect

app = FastAPI()

app.include_router(url.router)
app.include_router(redirect.router)
