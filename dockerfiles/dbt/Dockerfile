FROM python:3.11-buster

RUN pip install poetry==1.8.5

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /project

COPY . /project

RUN poetry install --no-root --with dbt && \
    rm -rf $POETRY_CACHE_DIR

RUN poetry run dbt deps

ARG DBT_PROFILES_DIR=/project
ARG POSTGRES_HOST
ARG POSTGRES_PORT
ARG DBT_USER
ARG DBT_PASSWORD
ARG DBT_DB

CMD ["sh", "-c", "poetry run dbt run"]