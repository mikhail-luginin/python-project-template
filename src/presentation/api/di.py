from functools import partial
from typing import Iterable

from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from application.common.interfaces.uow import UnitOfWork
from infrastructure.common.db.config import database_credentials
from infrastructure.db.uow import UnitOfWorkImpl

from .stub import Stub


def all_depends(cls: type) -> None:
    """
    Adds `Depends()` to the class `__init__` methods, so it can be used
    a fastapi dependency having own dependencies
    """
    init = cls.__init__  # type: ignore
    total_ars = init.__code__.co_kwonlyargcount + init.__code__.co_argcount - 1
    init.__defaults__ = tuple(Depends() for _ in range(total_ars))


def create_session_maker() -> sessionmaker:  # type: ignore
    engine = create_engine(
        "{connector}://{user}:{password}@{host}:{port}/{database}".format(**database_credentials()),
        # echo=True,
        # pool_size=15,
        # max_overflow=15,
        # connect_args={
        #     "connect_timeout": 5,
        # },
        pool_pre_ping=True,
    )
    return sessionmaker(engine, autoflush=False, expire_on_commit=False)


def new_session(session_maker: sessionmaker) -> Iterable[Session]:  # type: ignore
    with session_maker() as session:
        yield session


def generate_uow(session: Session = Depends(Stub(Session))) -> UnitOfWork:
    return UnitOfWorkImpl(session=session)


def init_dependencies(app: FastAPI) -> None:
    session_maker = create_session_maker()

    app.dependency_overrides[Session] = partial(new_session, session_maker)
    app.dependency_overrides[UnitOfWork] = generate_uow
