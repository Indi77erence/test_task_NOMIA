
from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.models import question
from src.app.questions.schemas import QuestionsCreate, QuestionsRead
from src.app.surveys.schemas import SurveyRead, SurveyCreate


async def create_questions(new_questions_data: QuestionsCreate, session: AsyncSession):
    stmt = insert(question).values(question_text=new_questions_data.question_text, survey_id=new_questions_data.survey_id)
    await session.execute(stmt)
    await session.commit()
    return new_questions_data


async def get_questions_list(session: AsyncSession):
    stmt = select(question)
    result = await session.execute(stmt)
    answer = [QuestionsRead(id=s.id, question_text=s.question_text, survey_id=s.survey_id) for s in result]
    return answer


async def get_questions_by_survey(survey_id: int, session: AsyncSession):
    stmt = select(question).where(question.c.survey_id == survey_id)
    result = await session.execute(stmt)
    answer = [QuestionsRead(id=s.id, question_text=s.question_text, survey_id=s.survey_id) for s in result]
    return answer


async def del_question(id_question: int, session: AsyncSession):
    stmt = delete(question).where(question.c.id == id_question)
    await session.execute(stmt)
    await session.commit()
    return True
