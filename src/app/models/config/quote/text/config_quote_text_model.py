from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

from app.models.config.quote.text.config_quote_text_bottom_model import ( 
    QuoteTextBottomConfig, QuoteTextBottomConfgiDict )
from app.models.config.quote.text.config_quote_text_center_model import (
    QuoteTextCenterConfig, QuoteTextCenterConfigDict
)

if TYPE_CHECKING:
    from app.models.config.config_app_model import AppConfigDict
    

class QuoteTextsConfigDict( TypedDict ):
    bottom : QuoteTextBottomConfgiDict
    center : QuoteTextCenterConfigDict

    
@dataclass
class QuoteTextsConfig:
    bottom : QuoteTextBottomConfig
    center : QuoteTextCenterConfig

    def __init__(self, cfg: 'AppConfigDict') -> None:
        self.bottom = QuoteTextBottomConfig( cfg )
        self.center = QuoteTextCenterConfig( cfg )