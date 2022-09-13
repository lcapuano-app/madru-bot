import logging
from typing import Tuple
from PIL import Image
from PIL.Image import Image as ImageType

from definitions import TRANSPARENT
from quote.layers import layers
from app_types.quote import ColorMode
from app_types.config import ConfigQuote


def get_bottom_decor_layer( quote_cfg: ConfigQuote, walker_asset: Image, margin: int = 0 ) -> ImageType:
    
    size_w_h: Tuple[int, int] = ( quote_cfg['canvas']['width'], quote_cfg['canvas']['height'] )
    decor_color: str = quote_cfg['decor']['bottom']['color']
    decor_height: int = int( quote_cfg['decor']['bottom']['height'] )
    decor_offset_ratio: float = quote_cfg['walker']['bottom_margin_ratio']

    base_layer: ImageType = layers.get_pil_layer( ColorMode.RGBA.value, size_w_h, TRANSPARENT )
    bottom_bar: ImageType = __create_bottom_bar( base_layer, walker_asset, margin, decor_color, decor_height )
    

    try:
        offset: Tuple[int, int] = __get_bottom_bar_offset( base_layer, walker_asset, margin, decor_offset_ratio )
        base_layer.paste( bottom_bar, offset, bottom_bar )
        return base_layer

    except Exception as err:
        logging.error( err )
        return base_layer


def __create_bottom_bar( base_image: Image, walker: Image, margin: int, color: str, height: int = 2 ) -> ImageType:

    base_w, base_h = base_image.size
    walker_w, walker_h = walker.size

    decor_size_h = height
    decor_size_w = base_w - walker_w - ( margin * 3 )

    decor_size = ( decor_size_w, decor_size_h )
    decor = Image.new( mode='RGBA', size=decor_size, color=color )

    return decor


def __get_bottom_bar_offset( 
    base_image: Image, 
    walker: Image, 
    margin: int = 0, 
    bottom_ratio = 0 ) -> Tuple[int, int]:

    base_w, base_h = base_image.size
    walker_w, walker_h = walker.size

    walker_h_ratio = bottom_ratio
    decor_offset_w = margin
    decor_offset_h = (base_h - margin) - ( walker_h * walker_h_ratio)

    decor_offset_w = int(decor_offset_w)
    decor_offset_h = int( decor_offset_h)

    decor_offset = ( decor_offset_w, decor_offset_h )

    return decor_offset