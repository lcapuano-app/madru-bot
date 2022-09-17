from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from models.config.config_app_model import AppConfigDict
    

class QuoteImgsConfigDict( TypedDict ):
    fallback    : str
    overlay_dir : str
    out_dir     : str
    
@dataclass
class QuoteImgsConfig:
    fallback    : str
    overlay_dir : str
    out_dir     : str

    def __init__(self, cfg: 'AppConfigDict') -> None:

        self.fallback = cfg['quote']['imgs']['fallback']
        self.overlay_dir = cfg['quote']['imgs']['overlay_dir']
        self.out_dir = cfg['quote']['imgs']['out_dir']