from dataclasses import dataclass
from typing import TypedDict, TYPE_CHECKING
from typing_extensions import Self


if TYPE_CHECKING:
    from models.config.config_app_model import AppConfigDict


class ApiAssetsConfigDict( TypedDict ):
    url_get  : str
    url_post : str


@dataclass()
class ApiAssetsConfig:

    url_get: str = None
    url_post: str = None


    def __init__(self, cfg: 'AppConfigDict') -> None:

        self.url_get = cfg['api']['assets']['url_get']
        self.url_post = cfg['api']['assets']['url_post']
