from fastapi import FastAPI

from src.app.admin_page.main import EstablishmentAdmin, SurveyAdmin, QuestionAdmin, AnswerAdmin
from src.app.surveys.router import router as survey_router
from src.app.questions.router import router as questions_router
from src.app.answers.router import router as answer_router
from src.auth.baseconfig import fastapi_users, auth_backend
from src.database import engine
from src.user.router import router as user_router
from src.pages.router import router as pages_router
from sqladmin import Admin


def create_app():
    app = FastAPI(title='Onboarding service APP')
    admin = Admin(app, engine)
    admin.add_view(EstablishmentAdmin)
    admin.add_view(SurveyAdmin)
    admin.add_view(QuestionAdmin)
    admin.add_view(AnswerAdmin)
    app.include_router(pages_router)
    app.include_router(user_router)
    app.include_router(fastapi_users.get_auth_router(auth_backend), tags=["Establishment_login"], prefix='/auth')
    app.include_router(survey_router, prefix="/api/v1")
    app.include_router(questions_router, prefix="/api/v1")
    app.include_router(answer_router, prefix="/api/v1")
    return app
