FROM python:3.11-alpine

RUN mkdir '/onboarding_system'

WORKDIR /onboarding_system

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .