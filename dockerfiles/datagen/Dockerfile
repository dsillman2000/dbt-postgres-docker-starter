FROM python:3.11-buster

RUN pip install poetry==1.8.5
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY . /project
WORKDIR /project

RUN poetry install --no-root --with datagen && \
    rm -rf $POETRY_CACHE_DIR

CMD bash dockerfiles/datagen/jobs/user_events.sh
