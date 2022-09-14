from dataclasses import dataclass
from typing import TypedDict, TYPE_CHECKING

from app.models.config.api.api_assets.config_api_assets_model import ApiAssetsConfig, ApiAssetsConfigDict

if TYPE_CHECKING:
    from app.models.config.config_app_model import AppConfigDict


class ApiConfigDict( TypedDict ):
    assets: ApiAssetsConfigDict


@dataclass()
class ApiConfig:

    assets: ApiAssetsConfig

    def __init__(self, cfg: 'AppConfigDict') -> None:
        self.assets = ApiAssetsConfig(cfg)