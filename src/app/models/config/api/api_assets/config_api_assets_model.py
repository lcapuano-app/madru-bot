from dataclasses import dataclass
from typing import TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.config.config_app_model import AppConfigDict


class ApiAssetsConfigDict( TypedDict ):
    url_get  : str
    url_post : str


@dataclass()
class ApiAssetsConfig:

    url_get: str
    url_post: str

    def __init__(self, cfg: 'AppConfigDict') -> None:
        self.url_get = cfg['api']['assets']['url_get']
        self.url_post = cfg['api']['assets']['url_post']
