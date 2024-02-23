from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, Boolean
from sqlalchemy.orm import relationship

from src.database import metadata, Base

establishment = Table(
	"establishment",
	metadata,
	Column("id", Integer, primary_key=True),
	Column("email", String, nullable=False),
	Column("name_establishment", String, nullable=False),
	Column("type_of_establishment", String, nullable=False),
	Column("registered_at", TIMESTAMP, default=datetime.utcnow),
	Column("hashed_password", String, nullable=False),
	Column("is_active", Boolean, default=True, nullable=False),
	Column("is_superuser", Boolean, default=False, nullable=False),
	Column("is_verified", Boolean, default=False, nullable=False),
)


class Establishment(SQLAlchemyBaseUserTable[int], Base):
	__tablename__ = 'establishment'
	id = Column(Integer, primary_key=True)
	email = Column(String, nullable=False)
	name_establishment = Column(String, nullable=False)
	type_of_establishment = Column(String, nullable=False)
	registered_at = Column(TIMESTAMP, default=datetime.utcnow)
	hashed_password: str = Column(String(length=1024), unique=True, nullable=False)
	is_active: bool = Column(Boolean, default=True, nullable=False)
	is_superuser: str = Column(Boolean, default=False, nullable=False)
	is_verified: str = Column(Boolean, default=False, nullable=False)

	def __str__(self):
		return self.name_establishment
