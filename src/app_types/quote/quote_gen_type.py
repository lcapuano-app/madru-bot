from typing import TypedDict

from app_types.quote.quote_gen_img_type import QuoteGenImg


class QuoteGen ( TypedDict ):
    author : str
    img    : QuoteGenImg
    msg    : str