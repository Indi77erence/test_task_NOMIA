from pydantic import BaseModel


class AnswerRead(BaseModel):
    id: int
    answer_text: str
    question_id: int
    establishment_id: int


class AnswerCreate(BaseModel):
    answer_text: str
    question_id: int


class ErrorCreateAnswer(BaseModel):
    error: str