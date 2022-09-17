from typing import TypeVar, TypedDict


T = TypeVar("T")


class HenrikRespDict ( TypedDict ):
    status: int
    data: T