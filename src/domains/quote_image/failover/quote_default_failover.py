import json
import logging
import os

from models import ApiQuoteType
from utils_cstm.errors import open_with_error
from definitions import DEFAULT_QUOTE_FILE, CONFIG_DIR
from models import ApiQuoteType, ApiQuoteTypeValidator


class QuoteDefaultFailover ():

    __dflt_quote: ApiQuoteType = None

    def get_default() -> ApiQuoteType:
        QuoteDefaultFailover.__get_default_quote()
        return QuoteDefaultFailover.__dflt_quote


    def __get_default_quote() -> ApiQuoteType:
        self = QuoteDefaultFailover

        file_do_not_exists = not os.path.exists( DEFAULT_QUOTE_FILE )

        if file_do_not_exists:
            self.__rebuild_quote_default_json()


        with open_with_error( DEFAULT_QUOTE_FILE ) as (file, err):

            if err:
                logging.warning( err )
                self.__rebuild_quote_default_json()

            else:
                quote = json.load( file )
                ApiQuoteTypeValidator.crash_invalid( quote, DEFAULT_QUOTE_FILE )
                self.__dflt_quote = quote


    def __rebuild_quote_default_json() -> None:
        self = QuoteDefaultFailover

        quote = self.__get_default_failover()

        with open_with_error( DEFAULT_QUOTE_FILE, mode='w' ) as (file, err):

            if err:
                logging.warning( err )

            quote_json = json.dumps( quote, indent = 4, ensure_ascii=False )
            char_count = file.write( quote_json )

            if char_count <= 0:
                logging.warning( 'Rebuild quote.default.json FAIL' )


        self.__dflt_quote = quote
        return quote

    def __get_default_failover() -> ApiQuoteType:
        return {
            "_id": "63139372217ba7e20813b92e",
            "author": {
                "displayName": "Chaves",
                "idName": "chaves",
                "quoteName": "Chaves"
            },
            "imgs": {
                "sm": "https://lcapuano.app/misc/chaves.jpg",
                "qt": "https://lcapuano.app/misc/chaves.jpg"
            },
            "msg": "Volta o cão arrependido, com suas orelhas tão fartas, com seu osso roído e com o rabo entre as patas.",
            "type": [
                "ERROR",
                "BRONCA"
            ],
            "createdAt": "2022-09-03T17:48:34.549Z",
            "updatedAt": "2022-09-03T17:48:34.549Z",
            "__v": 0
        }
