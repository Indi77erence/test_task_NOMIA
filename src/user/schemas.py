from typing import Optional
from fastapi_users import schemas
from pydantic import EmailStr, BaseModel


class EstablishmentCreate(schemas.BaseUserCreate):
	name_establishment: str
	email: EmailStr
	password: str
	type_of_establishment: str
	is_active: Optional[bool] = True
	is_superuser: Optional[bool] = False
	is_verified: Optional[bool] = False


class EstablishmentRead(schemas.BaseUser[int]):
	id: int | None
	email: EmailStr | None
	name_establishment: str | None
	type_of_establishment: str | None
	is_active: bool = True
	is_superuser: bool = False
	is_verified: bool = False


class ErrorRegisterEstablishment(BaseModel):
	error: str
