from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

from models.config.quote.decor.config_quote_decor_bottom_model import QuoteDecorBottomConfig, QuoteDecorBottomConfigDict

if TYPE_CHECKING:
    from models.config.config_app_model import AppConfigDict
    

class QuoteDecorConfigDict( TypedDict ):
    bottom: QuoteDecorBottomConfigDict

@dataclass
class QuoteDecorConfig:
    bottom: QuoteDecorBottomConfig

    def __init__(self, cfg: 'AppConfigDict') -> None:
        self.bottom = QuoteDecorBottomConfig(cfg)