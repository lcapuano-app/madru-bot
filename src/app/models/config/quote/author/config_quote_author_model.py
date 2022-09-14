from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from app.models.config.config_app_model import AppConfigDict
    

class QuoteAuthorConfigDict( TypedDict ):
    img_aplha          : int
    resize_limit_ratio : float
    rotate_degs        : int
    

@dataclass
class QuoteAuthorConfig:

    img_aplha          : int
    resize_limit_ratio : float
    rotate_degs        : int

    def __init__(self, cfg: 'AppConfigDict') -> None:
        self.img_aplha = cfg['quote']['author']['img_aplha']
        self.resize_limit_ratio = cfg['quote']['author']['resize_limit_ratio']
        self.rotate_degs = cfg['quote']['author']['rotate_degs']