from sqlalchemy.orm import Session

import models
import schemas


# FEATURE 1
def get_episodes(db: Session):
    return db.query(models.Episode).all()


def get_characters(db: Session):
    return db.query(models.Character).all()


# FEATURE 2
def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).get(comment_id)


def get_comments(db: Session):
    return db.query(models.Comment).all()


def get_episode_comments(db: Session, episode_id: int):
    return db.query(models.Comment).filter(models.Comment.episode_id == episode_id).all()


def get_character_comments(db: Session, character_id: int):
    return db.query(models.Comment).filter(models.Comment.character_id == character_id).all()


def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(comment=comment.comment, character_id=comment.character_id,
                                episode_id=comment.episode_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def update_comment(db: Session, comment_id: int, comment: schemas.CommentCreate):
    db_comment = db.query(models.Comment).get(comment_id)
    db_comment.comment = comment.comment
    db_comment.character_id = comment.character_id
    db_comment.episode_id = comment.episode_id

    db.commit()
    db.refresh(db_comment)
    return db_comment


def delete_comment(db: Session, comment_id: int):
    db.query(models.Comment).filter(models.Comment.id == comment_id).delete()
    db.commit()


# FEATURE 3
def search_comments(db: Session, keyword: str):
    return db.query(models.Comment).filter(models.Comment.comment.like(f"%{keyword}%")).all()


def search_episodes(db: Session, keyword: str):
    return db.query(models.Episode).filter(models.Episode.name.like(f"%{keyword}%")).all()


def search_characters(db: Session, keyword: str):
    return db.query(models.Character).filter(models.Character.name.like(f"%{keyword}%")).all()
