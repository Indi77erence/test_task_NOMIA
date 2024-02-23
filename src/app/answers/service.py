from typing import List, Dict

from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.answers.schemas import AnswerCreate, AnswerRead
from src.app.models import answer
from src.app.questions.schemas import QuestionsCreate, QuestionsRead
from src.app.surveys.schemas import SurveyRead, SurveyCreate


async def create_answers(establishment, survey_data: List[AnswerCreate], session: AsyncSession):
    values = []
    for answer_data in survey_data:
        value = {
            "answer_text": answer_data.answer_text,
            "question_id": answer_data.question_id,
            "establishment_id": establishment.id
        }
        values.append(value)
    await save_answer(values, session=session)
    return values


async def save_answer(new_answer_data: List[Dict], session: AsyncSession):
    stmt = insert(answer).values(new_answer_data)
    await session.execute(stmt)
    await session.commit()
    return new_answer_data


async def get_answer_list(session: AsyncSession):
    stmt = select(answer)
    result = await session.execute(stmt)
    result_fin = [
        AnswerRead(id=s.id, answer_text=s.answer_text, question_id=s.question_id, establishment_id=s.establishment_id)
        for s in result]
    return result_fin


#
#
async def get_answers_by_estab(establishment_id: int, session: AsyncSession):
    stmt = select(answer).where(answer.c.establishment_id == establishment_id)
    result = await session.execute(stmt)
    result_fin = [AnswerRead(id=s.id, answer_text=s.answer_text,
                             question_id=s.question_id, establishment_id=s.establishment_id) for s in result]
    return result_fin


async def del_answer(id_question: int, session: AsyncSession):
    stmt = delete(answer).where(answer.c.id == id_question)
    await session.execute(stmt)
    await session.commit()
    return True
