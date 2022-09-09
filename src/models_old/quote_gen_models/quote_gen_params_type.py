from enum import Enum
from typing import Tuple, TypedDict

#from models import ConfigQuoteType

#from ..config.config_quote_type import ConfigQuoteCanvasType


class QuoteGenModes( Enum ):
    RBG = 'RGB'
    RGBA = 'RGBA'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class QuoteGenParamsType ( TypedDict ):
    quote_id : str
    mode     : str
    size     : Tuple[ int, int ]
    color    : str


class QuoteGenParams():

    __color: str
    __quote_id: str
    __mode: QuoteGenModes
    __size: Tuple[int,int]

    def __init__(self, quote_id: str) -> None:
        self.__quote_id = quote_id
        self.__color = 'black'
        self.__mode = QuoteGenModes.RBG
        self.__size = (800, 600 )

    def get_params(self) -> QuoteGenParamsType:
        return {
            'color': self.__color,
            'mode': self.__mode,
            'quote_id': self.__quote_id,
            'size': self.__size
        }

    #def generate( self, quote_cfg: ConfigQuoteCanvasType = None ) -> QuoteGenParamsType:
    def generate( self, quote_cfg = None ) -> QuoteGenParamsType:

        if quote_cfg is None or quote_cfg:
            return self.get_params()

        else:
            return {
                'color': quote_cfg['color'],
                'mode': quote_cfg['mode'],
                'quote_id': self.__quote_id,
                'size': ( quote_cfg['width'], quote_cfg['height'] )
            }
