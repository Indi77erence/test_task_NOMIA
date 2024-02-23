from typing import Union, List

from fastapi import APIRouter, status, Depends

from src.app.answers.schemas import AnswerCreate, AnswerRead
from src.app.answers.service import get_answer_list, get_answers_by_estab, del_answer, create_answers
from src.auth.baseconfig import current_user
from src.database import get_async_session

router = APIRouter(
    tags=['Answer']
)


@router.post('/create_answer', response_model=List[AnswerCreate], status_code=status.HTTP_201_CREATED)
async def create_new_answer(new_answer_data: List[AnswerCreate], session=Depends(get_async_session),
                 establishment=Depends(current_user)):
    all_answer = await create_answers(survey_data=new_answer_data, establishment=establishment, session=session)
    return all_answer


@router.get('/all_answers', response_model=list[AnswerRead], status_code=status.HTTP_200_OK)
async def get_all_answer(session=Depends(get_async_session)):
    answer = await get_answer_list(session=session)
    return answer


@router.get('/answer/{establishment_id}', response_model=list[AnswerRead], status_code=status.HTTP_200_OK)
async def get_answers_by_establishment(establishment_id: int, session=Depends(get_async_session)):
    answer = await get_answers_by_estab(establishment_id, session)
    return answer


@router.delete('/answer/{id_answer}')
async def delete_question(id_answer: int, session=Depends(get_async_session)):
    answer = await del_answer(id_answer, session)
    return answer
