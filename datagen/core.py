import hashlib
import logging
import os
import sys
from functools import lru_cache
from typing import Any, Hashable

import psycopg as pg
import sqlalchemy
from sqlalchemy.orm import sessionmaker

_logger = logging.getLogger("sqlalchemy")
_logger.setLevel(logging.INFO)
_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
_handler.setLevel(logging.INFO)
_logger.addHandler(_handler)


@lru_cache
def get_engine():
    global _logger
    engine = sqlalchemy.create_engine(
        f"postgresql+psycopg://{os.getenv('DBT_USER', 'dbt')}:"
        f"{os.getenv('DBT_PASSWORD', 'dbt')}@"
        f"{os.getenv('POSTGRES_HOST', 'localhost')}:"
        f"{os.getenv('POSTGRES_PORT', '5432')}/"
        f"{os.getenv('DBT_DB', 'dbt')}"
    )
    engine.logger = _logger
    return engine


def md5(*data: Hashable) -> str:
    return hashlib.md5("".join(map(str, data)).encode()).hexdigest()


session = sessionmaker(bind=get_engine())
