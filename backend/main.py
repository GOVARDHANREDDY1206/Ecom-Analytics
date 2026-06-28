from fastapi import FastAPI
from sqlalchemy import text

from app.database.database import engine

app = FastAPI(title="Ecom Analytics API")


@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}


@app.get("/db-test")
def db_test():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"message": "Database Connected Successfully"}