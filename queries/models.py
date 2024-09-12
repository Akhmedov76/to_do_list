import sqlalchemy
from sqlalchemy import Column, String, Integer, Boolean, inspect

from Decorator.decorator import log_decorator
from database.database import metadata, engine

tasks = sqlalchemy.Table(
    'to_do_list', metadata,
    Column('id', Integer, primary_key=True),
    Column('task', String),
    Column('status', Boolean, default=False),
    Column('priority', Integer)
)

@log_decorator
def table_exists(table_name):
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    return table_name in tables

@log_decorator
def create_to_do_list_table():
    if not table_exists('to_do_list'):
        metadata.create_all(bind=engine)
