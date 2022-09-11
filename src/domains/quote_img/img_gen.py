import os

from typing import Any, TypedDict
from PIL.Image import Image as ImageType

from definitions import IMG_EXT
from core.config import CoreConfig
from core.types.quote import QuoteGenType, QuoteGenReq
from core.types.config import ConfigQuoteType
from domains.quote_img.layers.background_layer import BackgroundLayer


class QuoteImageGen():

    def __init__(self, quote: QuoteGenReq) -> None:
        self.__quote_req = quote

    

    def gen( self ) -> QuoteGenType:
        quote_config = CoreConfig().get.quote
        
        imgs_cfg = quote_config['imgs']

        qt_req = self.__quote_req
        img_name = qt_req['quote_id'] + IMG_EXT

        #file_path = os.path.join( qt_req[], img_name )
        #print( 'FUNFA?', core_config.cfg)
        #im2=Canvas.create()
        im = BackgroundLayer.create( quote_config['canvas'] )
        im.show()


