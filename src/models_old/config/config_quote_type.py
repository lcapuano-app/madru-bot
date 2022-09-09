from typing import TypedDict

from models.quote_gen_models.quote_gen_params_type import QuoteGenModes


class ConfigQuoteCanvasType ( TypedDict ):
    color: str
    mode: QuoteGenModes
    height: int
    width: int


class ConfigQuoteType ( TypedDict ):
    canvas: ConfigQuoteCanvasType
