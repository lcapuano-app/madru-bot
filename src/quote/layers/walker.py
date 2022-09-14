import logging
from time import sleep
from typing import Tuple
from PIL import Image
from PIL.Image import Image as ImageType

from definitions import TRANSPARENT
from quote.layers import layers
from app_types.config import ConfigQuote, ConfigQuoteImgs, ConfigQuoteWalker, ConfigType
from app_types.quote import ColorMode


def get_walker_layer( canvas: ImageType, walker_asset: ImageType,  margin: int = 0 ) -> ImageType:

    try:
        base_layer: ImageType = layers.get_pil_layer( ColorMode.RGBA.value, canvas.size, TRANSPARENT )
        offset: tuple[int, int] = __get_offset( base_layer, walker_asset, margin )
        base_layer.paste( walker_asset, offset, walker_asset )

        return base_layer

    except Exception as err:
        logging.error( err )
        return canvas


def get_walker_asset( cfg: ConfigType, canvas: ImageType ) -> ImageType:
 
    walker_file_path: str = __get_walker_file_path( cfg )
    walker_asset: ImageType = None

    try:
        walker_asset = Image.open( walker_file_path )

    except Exception as err:
        logging.warning(err )
            
        try:
            __load_wallker_asset_from_api( cfg, walker_file_path )
            walker_asset = Image.open( walker_file_path )
        except Exception as err:
            logging.error(err )
            walker_asset = __fallback( cfg )
        
       
    return walker_asset
        

def __get_offset( canvas: ImageType, walker: ImageType, margin: int ) -> Tuple[int, int]:

    base_w, base_h = canvas.size
    walker_w, walker_h = walker.size
    
    paste_w = base_w - walker_w - margin
    paste_h = base_h - walker_h - margin
    
    paste_w = int( paste_w )
    paste_h = int( paste_h )
    
    offset = ( paste_w, paste_h )

    return offset


def __get_walker_file_path( cfg: ConfigType ) -> str:

    quote_cfg: ConfigQuote = cfg['quote']
    imgs_cfg: ConfigQuoteImgs = quote_cfg['imgs']
    walker_cfg: ConfigQuoteWalker = quote_cfg['walker']
    walker_file =  layers.get_asset_path( 
        imgs_path = imgs_cfg['overlay_dir'], 
        asset_name = walker_cfg['asset'] 
    )

    return walker_file


def __load_wallker_asset_from_api( cfg: ConfigType, save_as: str ) -> bool:
    
    api_url: str = cfg['api']['assets']['get']
    api_url = api_url if api_url.endswith('/') else api_url + '/'

    walker_png: str = cfg['quote']['walker']['asset']

    url: str = api_url + walker_png
        
    is_loaded: bool = layers.load_asset_from_api( url, save_as, asset_name = walker_png)

    return is_loaded
    

def __fallback( cfg: ConfigType ) -> ImageType:
    
    quote_cfg: ConfigQuote = cfg['quote']
    mode, size, color = layers.parse_canvas_cfg( quote_cfg['canvas'] )
    w, h = size
    h = int(h * cfg['quote']['walker']['proportion_ratio'])
    w = int(h / 2)

    fallback: ImageType = layers.get_pil_layer( mode, (w, h), color= 'black' )

    if fallback is not None:
        return fallback
    else:
        fallback = Image.new( mode='RGBA', size=(w, h), color='black' )
        return fallback