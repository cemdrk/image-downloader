FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

ARG ENV=production

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN if [ "$ENV" = "development" ] ; then pip install -r requirements-dev.txt ; fi

ENV PYTHONPATH=/app
