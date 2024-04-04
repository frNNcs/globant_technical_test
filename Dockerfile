FROM python:3.12.2-alpine3.18 AS app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements/base.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
