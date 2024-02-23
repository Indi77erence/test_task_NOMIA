from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from src.auth.manager import get_user_manager
from src.config import SECRET
from src.database import async_session_maker
from src.user.models import Establishment

cookie_transport = CookieTransport(cookie_name="my_cookies", cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
	return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
	name="jwt",
	transport=cookie_transport,
	get_strategy=get_jwt_strategy,
)

user_db = SQLAlchemyUserDatabase(Establishment, async_session_maker)

fastapi_users = FastAPIUsers[Establishment, int](
	get_user_manager,
	[auth_backend],
)

current_user = fastapi_users.current_user()
