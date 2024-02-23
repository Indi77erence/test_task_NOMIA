from pathlib import Path

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from src.auth.baseconfig import current_user
from src.database import get_async_session
from src.pages.service import get_surveys_with_questions
from src.user.models import Establishment

router = APIRouter(
	tags=['Pages']
)

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory='src/templates')

multi_questions = {"Какой у вас тип заведения?": ["ресторан", "бар", "кафе", "столовая", "закусочная", "предприятие быстрого обслуживания", "буфет", "кафетерий", "кофейня", "магазин кулинарии"],
				   "Какие типы сервисов вы будете предоставлять в вашем заведении?": ["навынос", "в заведении", "Доставка"],
				   "Есть ли дополнительный сервис?": ["Доставка", "Навынос", "Не имеем"],
				   "Укажите ваш тип заведения": ["Салон красоты", "Медицинская клиника", "Фитнес-центр", "Туристическое агентство"],
				   "Какая отрасль вашего заведения?": ["Супермаркеты и гипермаркеты", "Магазины одежды и обуви", "Магазины электроники и бытовой техники", "Другое"]}

questions_type_est = {"Укажите свой тип заведения": ["Ритейл", "Услуги по записи", "Общественное питание"]}


@router.get('/registration')
async def get_start_page(request: Request):
	return templates.TemplateResponse("registration.html", {"request": request, "questions_type_est": questions_type_est})


@router.get('/log_in')
async def get_log_in_page(request: Request):
	return templates.TemplateResponse("log_in.html", {"request": request})


@router.get('/onboarding/{name_survey}')
async def get_login_page(name_survey: str, request: Request, estanlishment: Establishment = Depends(current_user),
						 session=Depends(get_async_session)):
	survey = await get_surveys_with_questions(estanlishment.type_of_establishment, session, name_survey)
	return templates.TemplateResponse("onboarding.html", {"request": request,
														  "survey": survey,
														  "multi_questions": multi_questions})


@router.get('/final')
async def get_error_page(request: Request):
	return templates.TemplateResponse("final.html", {"request": request})
