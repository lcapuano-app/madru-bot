from typing import TypedDict

#from models.quote_gen_models.quote_gen_params_type import QuoteGenModes


class ConfigQuoteCanvasType ( TypedDict ):
    color  : str
    mode   : str#QuoteGenModes
    height : int
    width  : int


class ConfigQuoteImgsType ( TypedDict ):
    overlay_dir : str
    out_dir     : str


class ConfigQuoteType ( TypedDict ):
    canvas : ConfigQuoteCanvasType
    imgs   : ConfigQuoteImgsType
