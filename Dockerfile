FROM python:3 AS poetry

RUN pip install poetry

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml ./

RUN poetry export -f requirements.txt --output requirements.txt

FROM python:3

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --from=poetry /app/requirements.txt .

RUN pip install -r requirements.txt

COPY . .


