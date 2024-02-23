from typing import Optional

from fastapi import Depends, Request, Response
from fastapi_users import BaseUserManager, IntegerIDMixin

from ..auth.service import get_user_db
from src.config import SECRET
from src.user.models import Establishment


class UserManager(IntegerIDMixin, BaseUserManager[Establishment, int]):
	reset_password_token_secret = SECRET
	verification_token_secret = SECRET


async def get_user_manager(user_db=Depends(get_user_db)):
	yield UserManager(user_db)
