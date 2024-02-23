from typing import Union

from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from src.auth.manager import get_user_manager
from src.user.schemas import EstablishmentCreate, EstablishmentRead, ErrorRegisterEstablishment
from src.user.service import check_email, del_establishment, create_establishment

router = APIRouter(
	tags=['Establishment']
)

types_of_establishment = ["Общественное питание", "Ритейл", "Услуги по записи"]


@router.post('/create_establishment', response_model=Union[EstablishmentRead, ErrorRegisterEstablishment],
			 status_code=status.HTTP_201_CREATED
			 )
async def create_new_establishment(
		new_establishment_data: EstablishmentCreate,
		user_manager=Depends(get_user_manager)
):
	if await check_email(new_establishment_data.email):
		if new_establishment_data.type_of_establishment not in types_of_establishment:
			return JSONResponse(
				status_code=status.HTTP_400_BAD_REQUEST,
				content={"error": "Некорректный тип заведения."}
			)
		new_establishment_data.is_verified = True
		new_establishment = await create_establishment(
			create_establishment_data=new_establishment_data,
			user_manager=user_manager
		)
		return new_establishment
	return JSONResponse(
		status_code=status.HTTP_400_BAD_REQUEST,
		content={"error": "Email не валидный"}
	)


@router.delete('/delete_establishment')
async def delete_establishment(answer=Depends(del_establishment)):
	return answer
