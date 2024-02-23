from pydantic import BaseModel


class SurveyRead(BaseModel):
	id: int
	name_survey: str
	type_of_establishment: str


class SurveyCreate(BaseModel):
	name_survey: str
	type_of_establishment: str


class ErrorCreateSurvey(BaseModel):
	error: str
