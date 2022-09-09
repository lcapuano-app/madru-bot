import logging

from typing import Union

from models import ApiQuoteType, QuoteGenType, QuoteGenParams
from config import Cfg
from .build.quote_get_parsed import QuoteGetParsed


class QuoteImage():

    __quote: QuoteGenType = None

    def __init__( self, quote: Union[ApiQuoteType, QuoteGenType] = None ) -> None:
        self.__quote = quote


    def get( self ):

        quote_cfg = Cfg.get_quote_cfg()
        self.__quote = QuoteGetParsed().get( quote=self.__quote )
        params = QuoteGenParams( quote_id = self.__quote['_id'] ).generate( quote_cfg=quote_cfg )
        print('esse',params)

        #QuoteGen.generate( params )
        pass


