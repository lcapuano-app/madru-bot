from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from models.config.config_app_model import AppConfigDict
    

class QuoteTextBottomConfgiDict( TypedDict ):
    font_color  : str
    font_face   : str
    font_size   : int
    size_factor : float


@dataclass
class QuoteTextBottomConfig:
    font_color  : str
    font_face   : str
    font_size   : int
    size_factor : float

    def __init__(self, cfg: 'AppConfigDict') -> None:
        self.font_color = cfg['quote']['text']['bottom']['font_color']
        self.font_face = cfg['quote']['text']['bottom']['font_face']
        self.font_size = cfg['quote']['text']['bottom']['font_size']
        self.size_factor = cfg['quote']['text']['bottom']['size_factor']