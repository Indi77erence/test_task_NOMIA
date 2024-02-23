from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from src.database import metadata, Base
from src.user.models import establishment

survey = Table(
    'survey',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name_survey', String(50), nullable=False),
    Column('type_of_establishment', String(50), nullable=False),
)


class Survey(Base):
    __tablename__ = 'survey'

    id = Column(Integer, primary_key=True)
    name_survey = Column(String(50), nullable=False)
    type_of_establishment = Column(String(50), nullable=False)

    def __str__(self):
        return self.name_survey


question = Table(
    'question',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('question_text', String(500), nullable=False),
    Column('survey_id', Integer, ForeignKey(survey.c.id, ondelete='SET NULL'))
)


class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    question_text = Column(String(500), nullable=False)
    survey_id = Column(Integer, ForeignKey('survey.id', ondelete='CASCADE'))
    survey = relationship('Survey', backref='questions')

    def __str__(self):
        return self.question_text


answer = Table(
    'answer',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('answer_text', String(500), nullable=False),
    Column('question_id', Integer, ForeignKey(question.c.id, ondelete='CASCADE')),
    Column('establishment_id', Integer, ForeignKey(establishment.c.id, ondelete='CASCADE'))
)


class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    answer_text = Column(String(500), nullable=False)
    question_id = Column(Integer, ForeignKey('question.id', ondelete='CASCADE'))
    question = relationship('Question', backref='answers')
    establishment_id = Column(Integer, ForeignKey('establishment.id', ondelete='CASCADE'))
    establishment = relationship('Establishment', backref='answers')


    def __str__(self):
        return self.answer_text
