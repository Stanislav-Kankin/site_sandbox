from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    content: str
    importance: int
    is_done: bool = False


class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteBase):
    pass


class Note(NoteBase):
    id: int

    class Config:
        orm_mode = True
