import functools
from typing import Awaitable, Callable, ParamSpec, TypeVar

from fastapi import HTTPException

R = TypeVar("R")
P = ParamSpec("P")


def controller():
    def wrapper(func: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]:
        @functools.wraps(func)
        async def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            try:
                return await func(*args, **kwargs)
            except Exception as _:
                raise HTTPException(status_code=500, detail="Internal Server Error :'v")

        return wrapped

    return wrapper
