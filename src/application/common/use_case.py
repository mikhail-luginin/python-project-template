import abc
from typing import Callable, Generic, Optional, TypeVar

InputDTO = TypeVar("InputDTO")
OutputDTO = TypeVar("OutputDTO")


class UseCase(Generic[InputDTO, OutputDTO], abc.ABC):
    def __call__(self, data: Optional[InputDTO] = None) -> Optional[OutputDTO]:
        raise NotImplementedError


UseCaseT = TypeVar("UseCaseT")
UseCaseFactory = Callable[[], UseCaseT]
