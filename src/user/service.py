import fastapi_users
import requests
from fastapi import Depends, HTTPException
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.baseconfig import current_user
from src.config import KEYHUNTER
from src.database import get_async_session
from src.user.models import Establishment
from src.user.schemas import EstablishmentCreate


async def check_email(email: str):
    """
    Функция, которая проверяет валидность email при помощи сервиса "emailhunter".

    Принимает 1 аргумент:
    - email - email пользователя, который хочет зарегистрироваться.

    Возвращает валидность email адреса.
    """
    api_key = KEYHUNTER
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    if "errors" in data:
        return False
    result = data['data']['status']
    if result == "valid":
        return True
    return False


async def create_establishment(create_establishment_data: EstablishmentCreate, user_manager):
    """
    Функция, которая регистрирует нового пользователя в системе.

    Принимает 2 аргумента:
    - create_establishment_data - схема fastapi_users для валидации введенных данных пользователем при регистрации.
    - user_manager - объект fastapi_users для управления пользователями.

    Функция возвращает данные зарегистрированного пользователя.
    """
    try:
        new_user = await user_manager.create(create_establishment_data)
        return new_user
    except fastapi_users.exceptions.UserAlreadyExists:
        return {"error": "Пользователь уже существует"}


async def del_establishment(session: AsyncSession = Depends(get_async_session),
                         establishment=Depends(current_user)):
    query = select(Establishment).where(Establishment.id == establishment.id)
    rez_query = await session.execute(query)
    if not rez_query.first()[0]:
        yield HTTPException(status_code=403, detail="Доступ запрещен")
    stmt = delete(Establishment).where(Establishment.id == establishment.id)
    await session.execute(stmt)
    await session.commit()
    yield "Пользователь удален!"
