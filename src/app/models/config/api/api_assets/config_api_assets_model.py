from dataclasses import dataclass
from typing import TypedDict, TYPE_CHECKING
from typing_extensions import Self


if TYPE_CHECKING:
    from app.models.config.config_app_model import AppConfigDict


class ApiAssetsConfigDict( TypedDict ):
    url_get  : str
    url_post : str


@dataclass()
class ApiAssetsConfig:

    __instance : Self = None
    __url_get: str = None
    __url_post: str = None


    def __new__(cls: type[Self], *args) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self, cfg: 'AppConfigDict') -> None:

        if self.__url_get is None:
            self.__url_get = cfg['api']['assets']['url_get']

        if self.__url_post is None:    
            self.__url_post = cfg['api']['assets']['url_post']

    @property
    def url_get( self ) -> str:
        return self.__url_get

    
    @property
    def url_post( self ) -> str:
        return self.__url_post
    
