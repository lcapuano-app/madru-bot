import logging
import os
import urllib.request

from typing import Tuple
from PIL import Image
from PIL.Image import Image as ImageType

from app import App
from app_types.quote import QuoteGenReq, QuoteGenAssets
from app_types.config import ConfigType, ConfigQuote
from quote.layers import author, background, decor, layers, walker, texts


def gen_quote_image( quote: QuoteGenReq ):

    cfg = App().__config
    quote_cfg = cfg['quote']

    image_src: str = quote['overlay'] + '.png'

    margin: int = layers.get_margin( 
        size = (quote_cfg['canvas']['width'], quote_cfg['canvas']['height'] ),
        ratio = quote_cfg['canvas']['margin_ratio']
    )

    gen_assets: QuoteGenAssets = __get_base_assets( cfg, image_src, margin )
    base_layer: ImageType = __get_base_layer( gen_assets )

    """ bottom_text_layer: ImageType = texts.get_bottom_text_layer(
        quote_req = quote,
        canvas = base_layer,
        cfg = quote_cfg,
        walker_asset = gen_assets['walker_asset'],
        margin = margin
    ) """
    bottom_text_layer, quote_text_layer = __get_texts_layers( gen_assets, quote, quote_cfg, margin )

    gen_assets['bottom_text_layer'] = bottom_text_layer if bottom_text_layer is not None else base_layer
    gen_assets['quote_text_layer'] = quote_text_layer if quote_text_layer is not None else base_layer
    

    base_layer.paste( gen_assets['bottom_text_layer'], (0,0), gen_assets['bottom_text_layer'] )
    base_layer.paste( gen_assets['quote_text_layer'], (0,0), gen_assets['quote_text_layer'] )
    #base_layer.show()

def __get_base_assets( cfg: ConfigType, image_src: str, margin: int = 0, ) -> QuoteGenAssets:

    quote_cfg = cfg['quote']
    gen_assets: QuoteGenAssets = {}

    try:
        bkg_layer: ImageType = background.get_background_layer( canvas_cfg = quote_cfg['canvas'] )
        gen_assets['bkg_layer'] = bkg_layer

        walker_asset: ImageType = walker.get_walker_asset( cfg, bkg_layer )
        gen_assets['walker_asset'] = walker_asset

        walker_layer: ImageType = walker.get_walker_layer( bkg_layer, walker_asset, margin )
        gen_assets['walker_layer'] = walker_layer

        bottom_decor_layer: ImageType = decor.get_bottom_decor_layer( quote_cfg, walker_asset, margin )
        gen_assets['bottom_decor_layer'] = bottom_decor_layer

        author_asset: ImageType = author.get_author_asset( cfg, image_src )
        gen_assets['author_asset'] = author_asset

        author_layer: ImageType = author.get_author_layer( bkg_layer, author_asset, cfg )
        gen_assets['author_layer'] = author_layer

        return gen_assets
    
    except Exception as err:
        logging.error(err)
        return gen_assets


def __get_base_layer( gen_assets: QuoteGenAssets ) -> ImageType:

    base_layer: ImageType = gen_assets['bkg_layer']
    size: tuple[int, int] = (0, 0)

    try:
        base_layer.paste( gen_assets['author_layer'], size, gen_assets['author_layer'] )
        base_layer.paste( gen_assets['walker_layer'], size, gen_assets['walker_layer'] )
        base_layer.paste( gen_assets['bottom_decor_layer'], size, gen_assets['bottom_decor_layer'] )
        return base_layer

    except Exception as err:
        logging.error( err )
        return base_layer


def __get_texts_layers( 
    gen_assets: QuoteGenAssets, 
    quote: QuoteGenReq, 
    quote_cfg: ConfigQuote, 
    margin: int = 0 ) -> Tuple[ ImageType, ImageType ]:

    bottom_text_layer: ImageType = None
    quote_text_layer: ImageType = None

    try:
        bottom_text_layer = texts.get_bottom_text_layer(
            quote_req = quote,
            canvas = gen_assets['bkg_layer'],
            cfg = quote_cfg,
            walker_asset = gen_assets['walker_asset'],
            margin = margin
        )
    except Exception as err:
        logging.error( err )

    try:
        quote_text_layer = texts.get_quote_text_layer( quote, quote_cfg, gen_assets['bkg_layer'] )

    except Exception as err:
        logging.error( err )

    return bottom_text_layer, quote_text_layer

