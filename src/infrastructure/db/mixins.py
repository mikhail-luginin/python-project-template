import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase

from utilities.time import get_current_time


class Base(DeclarativeBase):
    id = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)
    created_at = sa.Column(sa.DateTime, default=get_current_time)
    edited_at = sa.Column(sa.DateTime, nullable=True, onupdate=get_current_time)
