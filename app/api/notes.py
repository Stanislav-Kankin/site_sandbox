from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, session
from app.crud import notes as crud_notes
from app.schemas import notes as schemas_notes

router = APIRouter()


@router.post("/", response_model=schemas_notes.Note)
def create_note(note: schemas_notes.NoteCreate, db: Session = Depends(session.get_db)):
    return crud_notes.create_note(db=db, note=note)


@router.get("/", response_model=list[schemas_notes.Note])
def read_notes(skip: int = 0, limit: int = 10, db: Session = Depends(session.get_db)):
    notes = crud_notes.get_notes(db, skip=skip, limit=limit)
    return notes


@router.get("/{note_id}", response_model=schemas_notes.Note)
def read_note(note_id: int, db: Session = Depends(session.get_db)):
    note = crud_notes.get_note(db, note_id=note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put("/{note_id}", response_model=schemas_notes.Note)
def update_note(note_id: int, note: schemas_notes.NoteUpdate, db: Session = Depends(session.get_db)):
    return crud_notes.update_note(db, note_id=note_id, note=note)


@router.delete("/{note_id}", response_model=dict)
def delete_note(note_id: int, db: Session = Depends(session.get_db)):
    crud_notes.delete_note(db, note_id=note_id)
    return {"detail": "Note deleted"}
