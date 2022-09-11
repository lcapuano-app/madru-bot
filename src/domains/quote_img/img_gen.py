import os

from typing import Any, TypedDict
from PIL.Image import Image as ImageType

from definitions import IMG_EXT
from core.config import CoreConfig
from core.types.quote import QuoteGenType, QuoteGenReq


class QuoteImageGen:

    def __init__(self, quote: QuoteGenReq) -> None:
        self.__quote_req = quote

    def gen( self ) -> QuoteGenType:
        #core_config = CoreConfig().
        qt_req = self.__quote_req
        img_name = qt_req['quote_id'] + IMG_EXT
        #file_path = os.path.join( qt_req[], img_name )
        print( 'FUNFA?', img_name)
        pass
