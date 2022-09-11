from typing import TypedDict


class QuoteGenReq ( TypedDict ):
    quote_id : str
    author   : str
    overlay  : str
    msg      : str