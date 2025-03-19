from sqlalchemy.orm import Session
from app.db import models
from app.schemas import notes


def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()


def get_notes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Note).offset(skip).limit(limit).all()


def create_note(db: Session, note: notes.NoteCreate):
    db_note = models.Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def update_note(db: Session, note_id: int, note: notes.NoteUpdate):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    for key, value in note.dict(exclude_unset=True).items():
        setattr(db_note, key, value)
    db.commit()
    db.refresh(db_note)
    return db_note


def delete_note(db: Session, note_id: int):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    db.delete(db_note)
    db.commit()
