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
    return db_episodes


@app.get("/characters", response_model=List[schemas.Character])
def list_characters(db: Session = Depends(get_db)) -> list:
    """
    List all the characters.
    """
    db_characters = crud.get_characters(db)
    return db_characters


@app.get("/comments/{comment_id}", response_model=schemas.Comment)
def get_comment(comment_id: int, db: Session = Depends(get_db)) -> dict:
    """
    List all the comments.
    """
    db_comment = crud.get_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="No comment found")
    return db_comment


@app.get("/comments", response_model=List[schemas.Comment])
def list_comments(db: Session = Depends(get_db)) -> list:
    """
    List all the comments.
    """
    db_comments = crud.get_comments(db)
    return db_comments


@app.get("/episodes/{episode_id}/comments", response_model=List[schemas.Comment])
def list_episode_comments(episode_id: int, db: Session = Depends(get_db)) -> list:
    """
    List all the comments for an episode.
    """
    db_comments = crud.get_episode_comments(db, episode_id)
    return db_comments


@app.get("/characters/{character_id}/comments", response_model=List[schemas.Comment])
def list_character_comments(character_id: int, db: Session = Depends(get_db)) -> list:
    """
    List all the comments for a character.
    """
    db_comments = crud.get_character_comments(db, character_id)
    return db_comments


@app.post("/comments", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    """
    Create a comment on an episode, a character or on a character in one episode.
    """
    if comment.episode_id is None and comment.character_id is None:
        raise HTTPException(status_code=400, detail="Comment needs to be link to at least a character or an episode")
    return crud.create_comment(db=db, comment=comment)


@app.delete("/comments/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)) -> dict:
    """
    Delete a comment.
    """
    crud.delete_comment(db, comment_id)
    return {"message": f"Comment {comment_id} deleted"}


