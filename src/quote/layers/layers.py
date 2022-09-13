import logging
import os
import urllib.request

from typing import Tuple
from PIL import Image
from PIL.Image import Image as ImageType

from utils import files
from app_types.quote import QuoteGenCanvas, ColorMode


def get_pil_layer( mode: ColorMode, size: Tuple[int, int], color: str ) -> ImageType:
    w, h = size
    size = (int(w), int(h))
    try:
        layer = Image.new( mode, size, color )
        return layer

    except Exception as err:
        logging.error( err )
        return None


def get_asset_path( imgs_path: str, asset_name: str = ''  ) -> str:
    
    assets_path: str = files.get_dir_dot_dot_path( target_dir = imgs_path )
    return os.path.join( assets_path, asset_name )


def parse_canvas_cfg( canvas_cfg: QuoteGenCanvas ) -> Tuple[ColorMode, Tuple[int, int], str]:

    mode: ColorMode = canvas_cfg['mode']
    size: Tuple[ int, int ] = ( canvas_cfg['width'], canvas_cfg['height'] )
    color: str = canvas_cfg['color']

    return mode, size, color


def load_asset_from_api( url: str, save_as: str, asset_name: str ) -> bool:

    logging.debug('api request url: ' + url )

    try:
        dir_name: str = save_as.replace( asset_name, '' )
        if not os.path.exists( dir_name ):
            files.create_dir( dir_name )

        urllib.request.urlretrieve( url, save_as )
        return True

    except Exception as err:
        logging.error( err )
        return False


def get_margin( size: tuple[ int, int], ratio: float = 0 ) -> int:
    w, h = size
    if w > h:
        return int(h * ratio)
    else:
        return int(w * ratio)