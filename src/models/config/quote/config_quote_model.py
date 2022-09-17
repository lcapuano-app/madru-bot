from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict
from typing_extensions import Self


from models.config.quote.author.config_quote_author_model import QuoteAuthorConfig, QuoteAuthorConfigDict
from models.config.quote.canvas.config_quote_canvas_model import QuoteCanvasConfig, QuoteCanvasConfigDict
from models.config.quote.decor.config_quote_decor_model import QuoteDecorConfig, QuoteDecorConfigDict
from models.config.quote.imgs.config_quote_imgs_model import QuoteImgsConfig, QuoteImgsConfigDict
from models.config.quote.text.config_quote_text_model import QuoteTextsConfig, QuoteTextsConfigDict
from models.config.quote.walker.config_quote_walker_model import QuoteWalkerConfig, QuoteWalkerConfigDict


if TYPE_CHECKING:
    from models.config.config_app_model import AppConfigDict
    
class QuoteConfigDict( TypedDict ):
    author : QuoteAuthorConfigDict
    canvas : QuoteCanvasConfigDict
    decor  : QuoteDecorConfigDict
    imgs   : QuoteImgsConfigDict
    text   : QuoteTextsConfigDict
    walker : QuoteWalkerConfigDict


@dataclass()
class QuoteConfig:

    author : QuoteAuthorConfig = None
    canvas : QuoteCanvasConfig = None
    decor  : QuoteDecorConfig = None
    imgs   : QuoteImgsConfig = None
    text   : QuoteTextsConfig = None
    walker : QuoteWalkerConfig = None


    def __init__(self, cfg: 'AppConfigDict') -> None:

        self.author = QuoteAuthorConfig(cfg)
        self.canvas = QuoteCanvasConfig(cfg)
        self.decor = QuoteDecorConfig(cfg)
        self.imgs = QuoteImgsConfig(cfg)
        self.text = QuoteTextsConfig(cfg)
        self.walker = QuoteWalkerConfig(cfg)
