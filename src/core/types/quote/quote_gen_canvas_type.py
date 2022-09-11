from typing import TypedDict

from core.types.quote.quote_gen_modes_type import QuoteGenModes


class QuoteGenCanvasType ( TypedDict ):
    color  : str
    mode   : QuoteGenModes
    height : int
    width  : int