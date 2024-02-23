from typing import Union

from fastapi import APIRouter, status, Depends

from src.app.questions.schemas import QuestionsCreate, ErrorCreateQuestions, QuestionsRead
from src.app.questions.service import create_questions, get_questions_list, get_questions_by_survey, del_question
from src.database import get_async_session

router = APIRouter(
	tags=['Questions']
)


@router.post('/create_questions', response_model=Union[QuestionsCreate, ErrorCreateQuestions], status_code=status.HTTP_201_CREATED)
async def create_new_questions(new_questions_data: QuestionsCreate, session=Depends(get_async_session)):
	new_questions = await create_questions(new_questions_data, session=session)
	return new_questions


@router.get('/all_questions', response_model=list[QuestionsRead], status_code=status.HTTP_200_OK)
async def get_all_questions(session=Depends(get_async_session)):
	answer = await get_questions_list(session=session)
	return answer


@router.get('/questions/{survey_id}', response_model=list[QuestionsRead], status_code=status.HTTP_200_OK)
async def get_questions_by_survey_id(survey_id: int, session=Depends(get_async_session)):
	answer = await get_questions_by_survey(survey_id, session)
	return answer


@router.delete('/questions/{id_question}')
async def delete_question(id_question: int, session=Depends(get_async_session)):
	answer = await del_question(id_question, session)
	return answer
