from dataclasses import dataclass
from typing import TypedDict, TYPE_CHECKING
from typing_extensions import Self

from utils.validator.dicts import is_instance_raise
from app.models.config.api.api_assets.config_api_assets_model import ApiAssetsConfig, ApiAssetsConfigDict

if TYPE_CHECKING:
    from app.models.config.config_app_model import AppConfigDict


class ApiConfigDict( TypedDict ):
    assets: ApiAssetsConfigDict


@dataclass()
class ApiConfig:

    __instance : Self = None
    __assets: ApiAssetsConfig = None
    

    def __new__(cls: type[Self], *args) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self, cfg: 'AppConfigDict') -> None:
        if self.__assets is None:
            self.__assets = ApiAssetsConfig(cfg)
    

    @property
    def assets( self ) -> ApiAssetsConfig:
        return self.__assets