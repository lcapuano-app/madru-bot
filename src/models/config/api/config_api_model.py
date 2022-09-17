from dataclasses import dataclass
from typing import List, TypedDict, TYPE_CHECKING

from models.config.api.api_assets.config_api_assets_model import ApiAssetsConfig, ApiAssetsConfigDict
from models.config.api.henrik.config_api_henrik_model import ApiHenrikConfig, ApiHenrikConfigDict


if TYPE_CHECKING:
    from models.config.config_app_model import AppConfigDict


class ApiConfigDict( TypedDict ):
    assets      : ApiAssetsConfigDict
    henrik      : ApiHenrikConfigDict
    user_agents : list

@dataclass()
class ApiConfig:

    assets      : ApiAssetsConfig = None
    henrik      : ApiHenrikConfig = None
    user_agents : List[str] = None
  
    def __init__(self, cfg: 'AppConfigDict') -> None:
  
        self.assets = ApiAssetsConfig(cfg)
        self.henrik = ApiHenrikConfig(cfg)
        self.user_agents = cfg['api']['user_agents']
