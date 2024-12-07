# dbt-postgres-docker-starter

This is an example starter project which uses Docker compose to host a PostgreSQL database and a dbt execution container. It also supports using the host machine as a dbt execution environment for development.

## Prerequisites

For using the dockerized project, you will need the following installed on your machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

To run dbt on your host machine, you will need the following installed:

- Python 3.11 or later
- [poetry](https://python-poetry.org/docs/)

## Installation and Setup

Just run the following command to start the docker containers:

```bash
docker-compose up --build
```

This will start the PostgreSQL database and dbt execution container. The dbt container will run the `dbt run` command to execute the models in the `models` directory.

To run dbt on your host machine after the docker-compose project has started, you can use the following commands:

```bash
poetry install
source connect-docker.sh
poetry run dbt run
```

## Acknowledgements

David Sillman <dsillman2000@gmail.com>