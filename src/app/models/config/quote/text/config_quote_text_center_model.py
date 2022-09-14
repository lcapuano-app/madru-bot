from dataclasses import dataclass
from typing import TYPE_CHECKING

from app.models.config.quote.text.config_quote_text_bottom_model import (
    QuoteTextBottomConfgiDict, QuoteTextBottomConfig )

if TYPE_CHECKING:
    from app.models.config.config_app_model import AppConfigDict
    

class QuoteTextCenterConfigDict( QuoteTextBottomConfgiDict ):
    stroke_color : str
    stroke_size  : int
    wrap         : int


@dataclass
class QuoteTextCenterConfig( QuoteTextBottomConfig ):
    stroke_color : str
    stroke_size  : int
    wrap         : int

    def __init__(self, cfg: 'AppConfigDict') -> None:
    
        self.font_color = cfg['quote']['text']['center']['font_color']
        self.font_face = cfg['quote']['text']['center']['font_face']
        self.font_size = cfg['quote']['text']['center']['font_size']
        self.size_factor = cfg['quote']['text']['center']['size_factor']

        self.stroke_color = cfg['quote']['text']['center']['stroke_color']
        self.stroke_size = cfg['quote']['text']['center']['stroke_size']
        self.wrap = cfg['quote']['text']['center']['wrap']