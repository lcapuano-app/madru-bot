from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict
from typing_extensions import Self


from app.models.config.quote.author.config_quote_author_model import QuoteAuthorConfig, QuoteAuthorConfigDict
from app.models.config.quote.canvas.config_quote_canvas_model import QuoteCanvasConfig, QuoteCanvasConfigDict
from app.models.config.quote.decor.config_quote_decor_model import QuoteDecorConfig, QuoteDecorConfigDict
from app.models.config.quote.imgs.config_quote_imgs_model import QuoteImgsConfig, QuoteImgsConfigDict
from app.models.config.quote.text.config_quote_text_model import QuoteTextsConfig, QuoteTextsConfigDict
from app.models.config.quote.walker.config_quote_walker_model import QuoteWalkerConfig, QuoteWalkerConfigDict


if TYPE_CHECKING:
    from app.models.config.config_app_model import AppConfigDict
    
class QuoteConfigDict( TypedDict ):
    author : QuoteAuthorConfigDict
    canvas : QuoteCanvasConfigDict
    decor  : QuoteDecorConfigDict
    imgs   : QuoteImgsConfigDict
    text   : QuoteTextsConfigDict
    walker : QuoteWalkerConfigDict


@dataclass()
class QuoteConfig:
    
    __instance : Self = None

    __author : QuoteAuthorConfig = None
    __canvas : QuoteCanvasConfig = None
    __decor  : QuoteDecorConfig = None
    __imgs   : QuoteImgsConfig = None
    __text   : QuoteTextsConfig = None
    __walker : QuoteWalkerConfig = None


    def __new__(cls: type[Self], *args) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self, cfg: 'AppConfigDict') -> None:

        self.__author = QuoteAuthorConfig(cfg) if self.__author is None else self.__author
        self.__canvas = QuoteCanvasConfig(cfg) if self.__canvas is None else self.__canvas
        self.__decor = QuoteDecorConfig(cfg) if self.__decor is None else self.__decor
        self.__imgs = QuoteImgsConfig(cfg) if self.__imgs is None else self.__imgs
        self.__text = QuoteTextsConfig(cfg) if self.__text is None else self.__text
        self.__walker = QuoteWalkerConfig(cfg) if self.__walker is None else self.__walker


    @property
    def author( self ) -> QuoteAuthorConfig:
        return self.__author
    
    @property
    def canvas( self ) -> QuoteCanvasConfig:
        return self.__canvas

    @property
    def decor( self ) -> QuoteDecorConfig:
        return self.__decor

    @property
    def imgs( self ) -> QuoteImgsConfig:
        return self.__imgs

    @property
    def text( self ) -> QuoteTextsConfig:
        return self.__text

    @property
    def author( self ) -> QuoteAuthorConfig:
        return self.__author

    @property
    def walker( self ) -> QuoteWalkerConfig:
        return self.__walker