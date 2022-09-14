from dataclasses import dataclass
from typing import TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.config.config_app_model import AppConfigDict

class DiscordConfigDict( TypedDict ):
    url_get: str
    url_post: str


@dataclass
class DiscordConfig:

    url_get: str
    url_post: str

    def __init__(self, cfg: 'AppConfigDict' ) -> None:
        self.url_get = cfg['discord']['url_get']
        self.url_post = cfg['discord']['url_post']