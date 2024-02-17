import abc
from typing import Any as Model


class IPostRepository(abc.ABC):
    @abc.abstractmethod
    async def add(self, **kw) -> int:
        ...

    @abc.abstractmethod
    async def get(self, **kw) -> Model:
        ...

    @abc.abstractmethod
    async def list(self) -> list[Model]:
        ...

    @abc.abstractmethod
    async def get_with_publisher(self, **kw) -> Model:
        ...
