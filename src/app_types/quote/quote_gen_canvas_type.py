from typing import TypedDict

from app_types.quote.quote_gen_modes_type import ColorMode


class QuoteGenCanvas ( TypedDict ):
    color        : str
    margin_ratio : float
    mode         : ColorMode
    height       : int
    width        : int