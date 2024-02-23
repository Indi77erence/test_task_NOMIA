
from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.models import survey
from src.app.surveys.schemas import SurveyRead, SurveyCreate


async def create_survey(new_survey_data: SurveyCreate, session: AsyncSession):
    stmt = insert(survey).values(name_survey=new_survey_data.name_survey, type_of_establishment=new_survey_data.type_of_establishment)
    await session.execute(stmt)
    await session.commit()
    return new_survey_data


async def get_survey_list(session: AsyncSession):
    stmt = select(survey)
    result = await session.execute(stmt)
    answer = [SurveyRead(id=s.id, name_survey=s.name_survey, type_of_establishment=s.type_of_establishment) for s in result]
    return answer


async def get_survey_type(type_of_establishment: str, session: AsyncSession):
    stmt = select(survey).where(survey.c.type_of_establishment == type_of_establishment)
    result = await session.execute(stmt)
    answer = [SurveyRead(id=s.id, name_survey=s.name_survey, type_of_establishment=s.type_of_establishment) for s in result]
    return answer


async def del_survey(id_survey: int, session: AsyncSession):
    stmt = delete(survey).where(survey.c.id == id_survey)
    await session.execute(stmt)
    await session.commit()
    return True
