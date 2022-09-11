from typing import TypedDict

from core.types.quote.quote_gen_img_type import QuoteGenImgType


class QuoteGenType ( TypedDict ):
    author : str
    img    : QuoteGenImgType
    msg    : str