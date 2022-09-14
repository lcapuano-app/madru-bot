from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from app.models.config.config_app_model import AppConfigDict
    

class QuoteDecorBottomConfigDict( TypedDict ):
    color  : str
    height : int

@dataclass
class QuoteDecorBottomConfig:
    color  : str
    height : int

    def __init__(self, cfg: 'AppConfigDict') -> None:
        self.color = cfg['quote']['decor']['bottom']['color']
        self.height = cfg['quote']['decor']['bottom']['height']