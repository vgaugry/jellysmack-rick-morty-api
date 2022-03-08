from sqlalchemy.orm import Session

import models
import schemas


def get_episodes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Episode).offset(skip).limit(limit).all()


def get_characters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Character).offset(skip).limit(limit).all()


def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()


def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(comment=comment.comment, character_id=comment.character_id,
                                episode_id=comment.episode_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

