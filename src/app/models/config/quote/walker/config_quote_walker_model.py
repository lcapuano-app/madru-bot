from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from app.models.config.config_app_model import AppConfigDict
    

class QuoteWalkerConfigDict( TypedDict ):
    asset               : str
    bottom_margin_ratio : float
    proportion_ratio    : float

@dataclass
class QuoteWalkerConfig:
    asset               : str
    bottom_margin_ratio : float
    proportion_ratio    : float

    def __init__(self, cfg: 'AppConfigDict') -> None:
        self.asset = cfg['quote']['walker']['asset']
        self.bottom_margin_ratio = cfg['quote']['walker']['bottom_margin_ratio']
        self.proportion_ratio = cfg['quote']['walker']['proportion_ratio']