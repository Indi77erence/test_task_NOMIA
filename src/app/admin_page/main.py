from sqladmin import ModelView

from src.user.models import Establishment
from src.app.models import Survey, Question, Answer


class EstablishmentAdmin(ModelView, model=Establishment):
	column_list = [Establishment.id,
				   Establishment.name_establishment,
				   Establishment.type_of_establishment,
				   Establishment.email,
				   Establishment.is_verified,
				   Establishment.registered_at]


class SurveyAdmin(ModelView, model=Survey):
	column_list = [Survey.id,
				   Survey.name_survey,
				   Survey.type_of_establishment]



class QuestionAdmin(ModelView, model=Question):
	column_list = [Question.id,
				   Question.question_text,
				   Question.survey_id]


class AnswerAdmin(ModelView, model=Answer):
	column_list = [Answer.id,
				   Answer.answer_text,
				   Answer.question_id,
				   Answer.establishment_id]
