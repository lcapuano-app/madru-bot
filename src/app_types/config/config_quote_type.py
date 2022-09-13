from typing import TypedDict

from app_types.quote.quote_gen_canvas_type import QuoteGenCanvas


class ConfigQuoteAuthor ( TypedDict ):
    img_aplha          : int
    resize_limit_ratio : float
    rotate_degs        : int
    

class ConfigQuoteDecorBottom ( TypedDict ):
    color  : str
    height : int


class ConfigQuoteDecor ( TypedDict ):
    bottom: ConfigQuoteDecorBottom


class ConfigQuoteCanvas ( QuoteGenCanvas ):
    pass


class ConfigQuoteImgs ( TypedDict ):
    fallback    : str
    overlay_dir : str
    out_dir     : str


class ConfigQuoteWalker ( TypedDict ):
    asset: str
    bottom_margin_ratio: float
    proportion_ratio: float


class ConfigQuote ( TypedDict ):
    author : ConfigQuoteAuthor
    canvas : ConfigQuoteCanvas
    decor  : ConfigQuoteDecor
    imgs   : ConfigQuoteImgs
    text: dict
    walker : ConfigQuoteWalker
