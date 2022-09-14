from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from app.models.config.config_app_model import AppConfigDict
    

class QuoteCanvasConfigDict( TypedDict ):
    color        : str
    height       : int
    margin_ratio : float
    mode         : str
    width        : int

@dataclass
class QuoteCanvasConfig:

    color        : str
    height       : int
    margin_ratio : float
    mode         : str
    width        : int

    def __init__(self, cfg: 'AppConfigDict') -> None:

        self.color = cfg['quote']['canvas']['color']
        self.height = cfg['quote']['canvas']['height']
        self.margin_ratio = cfg['quote']['canvas']['margin_ratio']
        self.mode = cfg['quote']['canvas']['mode']
        self.width = cfg['quote']['canvas']['width']

        