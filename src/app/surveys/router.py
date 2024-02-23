from typing import Union

from fastapi import APIRouter, status, Depends

from src.app.surveys.schemas import SurveyRead, SurveyCreate, ErrorCreateSurvey
from src.app.surveys.service import create_survey, get_survey_list, del_survey, get_survey_type
from src.database import get_async_session

router = APIRouter(
	tags=['Surveys']
)

types_of_establishment = ["Общественное питание", "Ритейл", "Услуги по записи"]


@router.post('/create_survey', response_model=Union[SurveyCreate, ErrorCreateSurvey], status_code=status.HTTP_201_CREATED)
async def create_new_survey(new_survey_data: SurveyCreate, session=Depends(get_async_session)):
	if new_survey_data.type_of_establishment not in types_of_establishment:
		return {"error": "Некорректный тип заведения."}
	new_survey = await create_survey(new_survey_data=new_survey_data, session=session)
	return new_survey


@router.get('/all_survey', response_model=list[SurveyRead], status_code=status.HTTP_200_OK)
async def get_all_survey(session=Depends(get_async_session)):
	answer = await get_survey_list(session=session)
	return answer


@router.get('/survey/{type_of_establishment}', response_model=list[SurveyRead], status_code=status.HTTP_200_OK)
async def get_survey_by_type(type_of_establishment, session=Depends(get_async_session)):
	answer = await get_survey_type(type_of_establishment, session)
	return answer


@router.delete('/survey/{id_survey}')
async def delete_survey(id_survey: int, session=Depends(get_async_session)):
	answer = await del_survey(id_survey, session)
	return answer
