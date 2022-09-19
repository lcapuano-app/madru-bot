from typing import TypedDict
from PIL.Image import Image as ImageType

from app_types.quote.quote_gen_img_type import QuoteGenImg


class QuoteGenAssets( TypedDict ):
    author_asset       : ImageType
    author_layer       : ImageType
    bkg_layer          : ImageType
    bottom_decor_layer : ImageType  
    bottom_text_layer  : ImageType
    quote_text_layer   : ImageType
    walker_asset       : ImageType
    walker_layer       : ImageType


class QuoteGen ( TypedDict ):
    author : str
    img    : QuoteGenImg
    msg    : str