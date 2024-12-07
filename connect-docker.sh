# Usage: source connect-docker.sh
# Allows you to run `poetry run dbt run` from host machine.

bash .env
export POSTGRES_HOST=0.0.0.0
export DBT_DB=$DBT_DB
export POSTGRES_PORT=$POSTGRES_PORT
export DBT_USER=$DBT_USER
export DBT_PASSWORD=$DBT_PASSWORD
export LANDING_SCHEMA=$LANDING_SCHEMA