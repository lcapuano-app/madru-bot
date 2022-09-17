from dataclasses import dataclass
from typing import TypedDict, TYPE_CHECKING
from typing_extensions import Self


if TYPE_CHECKING:
    from models.config.config_app_model import AppConfigDict


class ApiHenrikConfigDict( TypedDict ):
    rank : str
   

@dataclass()
class ApiHenrikConfig:

    rank: str = None

    def __init__(self, cfg: 'AppConfigDict') -> None:

        self.rank = cfg['api']['henrik']['rank']

