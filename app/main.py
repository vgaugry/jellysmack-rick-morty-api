from typing import List

from fastapi import FastAPI, HTTPException, Depends

import schemas
import crud
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(
    title="Rick & Morty API", openapi_url="/openapi.json"
)


@app.get("/")
def root() -> dict:
    """
    Root
    """
    return {"message": "Hello and welcome to the Rick & Morty API ! You can find the doc at /docs"}


@app.get("/episodes", response_model=List[schemas.Episode])
def list_episodes(db: Session = Depends(get_db)) -> list:
    """
    List all the episodes.
    """
    db_episodes = crud.get_episodes(db)
    if db_episodes is None:
        raise HTTPException(status_code=404, detail="No episodes found")
    return db_episodes


@app.get("/characters", response_model=List[schemas.Character])
def list_characters(db: Session = Depends(get_db)) -> list:
    """
    List all the characters.
    """
    db_characters = crud.get_characters(db)
    if db_characters is None:
        raise HTTPException(status_code=404, detail="No characters found")
    return db_characters


