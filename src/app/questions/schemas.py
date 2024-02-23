from pydantic import BaseModel


class QuestionsRead(BaseModel):
	id: int
	question_text: str
	survey_id: int


class QuestionsCreate(BaseModel):
	question_text: str
	survey_id: int


class ErrorCreateQuestions(BaseModel):
	error: str