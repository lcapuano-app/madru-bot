from typing import TypedDict

from core.types.quote.quote_gen_canvas_type import QuoteGenCanvasType


class ConfigQuoteCanvasType ( QuoteGenCanvasType ):
   pass


class ConfigQuoteImgsType ( TypedDict ):
    overlay_dir : str
    out_dir     : str


class ConfigQuoteType ( TypedDict ):
    canvas : ConfigQuoteCanvasType
    imgs   : ConfigQuoteImgsType
