FROM python:3.12.2-alpine3.18 AS app


WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

COPY requirements/base.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
