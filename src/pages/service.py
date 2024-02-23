from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.models import survey, question as question_tbl


async def get_surveys_with_questions(type_of_establishment: str, session: AsyncSession, name_survey: str):
    """
	Функция, которая необходима для получения необходимых опросов.

	Принимает 3 аргумента:
	- session - экземпляр, который обеспечивает асинхронное взаимодействие с БД.
	- type_of_establishment - тип заведения.
	- name_survey - название опроса.

	Функция возвращает состояние проверки.
	"""
    query = select(survey.c.name_survey, question_tbl.c.question_text, question_tbl.c.id).where(
        (survey.c.name_survey.contains(f'{name_survey}')) & (survey.c.type_of_establishment == type_of_establishment)
    ).select_from(survey.join(question_tbl))
    result = await session.execute(query)
    surveys = {}
    for row in result.fetchall():
        survey_name = row[0]
        question = row[1]
        question_id = row[2]
        if survey_name not in surveys:
            surveys[survey_name] = [[question, question_id]]
        else:
            surveys[survey_name].append([question, question_id])
    return surveys


