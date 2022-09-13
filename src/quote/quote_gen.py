import logging
import os
import urllib.request

from typing import Tuple
from PIL import Image
from PIL.Image import Image as ImageType

from app import App
from utils.files import get_dir_dot_dot_path
from app_types.quote import QuoteGenReq, QuoteGenCanvas, ColorMode
from app_types.config import ConfigQuote, ConfigQuoteImgs, ConfigQuoteWalker, ConfigType
from quote.layers import author, background, decor, layers, walker


def gen_quote_image( quote: QuoteGenReq ):

    cfg = App().config
    quote_cfg = cfg['quote']

    image_src: str = quote['overlay'] + '.png'

    margin: int = layers.get_margin( 
        size = (quote_cfg['canvas']['width'], quote_cfg['canvas']['height'] ),
        ratio = quote_cfg['canvas']['margin_ratio']
    )

    base_layer: ImageType = __get_base_layer( cfg, image_src, margin )

    

    base_layer.show()


def __get_base_layer( cfg: ConfigType, image_src: str, margin: int = 0, ) -> ImageType:

    quote_cfg = cfg['quote']

    bkg_layer: ImageType = background.get_background_layer( canvas_cfg = quote_cfg['canvas'] )
    walker_asset: ImageType = walker.get_walker_asset( cfg, bkg_layer )
    walker_layer: ImageType = walker.get_walker_layer( bkg_layer, walker_asset, margin )
    bottom_decor_layer: ImageType = decor.get_bottom_decor_layer( quote_cfg, walker_asset, margin )
    author_asset: ImageType = author.get_author_asset( cfg, image_src )
    author_layer: ImageType = author.get_author_layer( bkg_layer, author_asset, cfg )

    base_layer: ImageType = bkg_layer

    try:
        base_layer.paste( author_layer, (0, 0), author_layer )
        base_layer.paste( walker_layer, (0, 0), walker_layer )
        base_layer.paste( bottom_decor_layer, (0, 0), bottom_decor_layer )
        return base_layer

    except Exception as err:
        logging.error( err )
        return base_layer



