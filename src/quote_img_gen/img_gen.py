import os

from typing import Any, TypedDict
from PIL.Image import Image as ImageType

from definitions import IMG_EXT
from app_config import AppConfig

_AppConfig = AppConfig
_IMG_EXT = IMG_EXT

del IMG_EXT, AppConfig


class QuoteImageGenImgType ( TypedDict ):
    b64  : str
    name : str
    obj  : ImageType
    url  : str


class QuoteImageGenType ( TypedDict ):
    author : str
    img    : QuoteImageGenImgType
    msg    : str

class QuoteImageGenReq ( TypedDict ):
    quote_id : str
    author   : str
    overlay  : str
    msg      : str


class QuoteImageGen:

    def __init__(self, quote: QuoteImageGenReq) -> None:
        self.__quote_req = quote

    def gen( self ) -> QuoteImageGenType:
        #app_cfg = _AppConfig().
        qt_req = self.__quote_req
        img_name = qt_req['quote_id'] + _IMG_EXT
        #file_path = os.path.join( qt_req[], img_name )
        print( 'FUNFA?', img_name)
        pass
