from datetime import datetime
from pydantic import BaseModel


class ReqQuestion(BaseModel):
    questions_num: int

    class Config:
        orm_mode = True


class Question(BaseModel):
    question_text: str = None
    answer_text: str = None
    created_at: datetime = None
    jservice_id: int = None

    class Config:
        orm_mode = True
