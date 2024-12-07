from __future__ import annotations

import datetime
import json
import os
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datagen.main import Datagen

from sqlalchemy import JSON, Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import CreateTable
from sqlalchemy.sql.expression import Insert
from sqlalchemy.sql.schema import MetaData

from datagen.core import get_engine, md5, session

Base = declarative_base()

metadata = MetaData(schema=os.getenv("DBT_DB", "") + "." + os.getenv("LANDING_SCHEMA", ""))


recent_timestamp = lambda: datetime.datetime.now() - datetime.timedelta(seconds=random.randint(0, 60))
now = datetime.datetime.now
region_id = lambda: random.choice(["us-east-1", "us-west-1", "eu-west-1"])
user_id = lambda: "user-" + random.choice(list(map(lambda s: f"{s:x}", range(12))))
client_version = lambda: "1.0." + str(random.randint(0, 10))


def generate_login_data():
    return {"status": random.choice(["success"] * 10 + ["failure"])}


def generate_click_data():
    return {"xy": (random.randint(0, 100), random.randint(0, 100))}


EVENT_DATA_GENERATORS = {
    "login": generate_login_data,
    "click": generate_click_data,
}

event_type = lambda: random.choice(list(EVENT_DATA_GENERATORS.keys()))


class UserEvent(Base):
    __tablename__ = "user_events"
    __table_args__ = {"schema": os.getenv("LANDING_SCHEMA", "")}
    region_id = Column(String)
    user_id = Column(String)
    client_version = Column(String)
    event_type = Column(String)
    event_data = Column(JSON)
    event_timestamp = Column(DateTime)
    event_id = Column(String, primary_key=True)
    received_at = Column(DateTime)

    def __init__(
        self,
        region_id: str,
        user_id: str,
        client_version: str,
        event_type: str,
        event_data: dict,
        event_timestamp: str,
        received_at: str,
    ):
        self.region_id = region_id
        self.user_id = user_id
        self.client_version = client_version
        self.event_type = event_type
        self.event_data = event_data
        self.event_timestamp = event_timestamp
        self.event_id = md5(
            region_id,
            user_id,
            event_timestamp,
            event_type,
            json.dumps(event_data),
        )
        self.received_at = received_at

    def tuple(self):
        return (
            self.region_id,
            self.user_id,
            self.client_version,
            self.event_type,
            self.event_data,
            self.event_timestamp,
            self.event_id,
            self.received_at,
        )

    @classmethod
    def new_random(cls):
        return cls(
            region_id=region_id(),
            user_id=user_id(),
            client_version=client_version(),
            event_type=(et := event_type()),
            event_data=EVENT_DATA_GENERATORS[et](),
            event_timestamp=recent_timestamp().isoformat(),
            received_at=now().isoformat(),
        )


def user_events(self: "Datagen"):
    with session() as sess:
        create_expr = CreateTable(UserEvent.__table__, if_not_exists=True)
        sess.execute(create_expr)
        sess.commit()
        insert_expr = Insert(UserEvent.__table__).values(
            [UserEvent.new_random().tuple() for _ in range(random.randint(1, 10))]
        )
        sess.execute(insert_expr)
        sess.commit()
