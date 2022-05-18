from importlib.metadata import metadata
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from db import meta, engine

users = Table("users", meta, Column(
    "id", Integer, primary_key=True), Column("name", String(64)), Column("email", String(128)), Column("password", String(128)))

meta.create_all(engine)