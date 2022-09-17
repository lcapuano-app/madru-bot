from dataclasses import dataclass
from typing import TypedDict, TYPE_CHECKING
from typing_extensions import Self

if TYPE_CHECKING:
    from models.config.config_app_model import AppConfigDict

class DiscordConfigDict( TypedDict ):
    api_ver   : int
    client_id : str
    token     : str


@dataclass
class DiscordConfig:

    api_ver: int = None
    client_id: str = None
    token: str = None


    def __init__(self, cfg: 'AppConfigDict' ) -> None:

        self.api_ver = cfg['discord']['api_ver']
        self.client_id = cfg['discord']['client_id']
        self.token = cfg['discord']['token']
