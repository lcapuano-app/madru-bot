import logging

from typing import Tuple
from PIL import Image, ImageOps
from PIL.Image import Image as ImageType

from definitions import AUTHOR_RESIZE_LIMIT_RATIO
from quote.layers import layers
from app_types.quote import QuoteGenReq
from app_types.config import ConfigQuote, ConfigQuoteAuthor, ConfigQuoteImgs, ConfigType


def get_author_layer( canvas: ImageType, author_asset: ImageType, cfg: ConfigType ) -> ImageType:
    
    author_cfg: ConfigQuoteAuthor = cfg['quote']['author']

    author_layer = __author_resize( canvas, author_asset, author_cfg )
    author_layer = ImageOps.grayscale( author_layer )
    author_layer = author_layer.rotate( 
        angle = author_cfg['rotate_degs'], 
        expand = 0, 
        center = None, 
        translate = None, 
        fillcolor = None
    )
    author_layer = __author_crop( canvas, author_layer )
    author_layer.putalpha( author_cfg['img_aplha'] )

    return author_layer


def get_author_asset( cfg: ConfigType, image_src: str ) -> ImageType:
    
    author_file_path: str = __get_author_file_path( cfg, image_src )
    author_asset: ImageType = None

    try:
        author_asset = Image.open( author_file_path )
    except Exception as err:
        logging.warning(err )

        try:
            __load_author_asset_from_api( cfg, author_file_path, image_src )
            author_asset = Image.open( author_file_path )
        except Exception as err:
            logging.error(err )
            author_asset = __fallback( cfg )
            
    

    return author_asset


def __load_author_asset_from_api( cfg: ConfigType, save_as: str, image_src: str ) -> ImageType:

    api_url: str = cfg['api']['assets']['get']
    api_url = api_url if api_url.endswith('/') else api_url + '/'

    url: str = api_url + image_src
   
    is_loaded: bool = layers.load_asset_from_api( url, save_as, asset_name = image_src )

    return is_loaded


def __get_author_file_path( cfg: ConfigType, image_src: str ) -> str:

    quote_cfg: ConfigQuote = cfg['quote']
    imgs_cfg: ConfigQuoteImgs = quote_cfg['imgs']
    img_file_path =  layers.get_asset_path( 
        imgs_path = imgs_cfg['overlay_dir'], 
        asset_name = image_src
    )

    return img_file_path


def __fallback( cfg: ConfigType ) -> ImageType:
    
    quote_cfg: ConfigQuote = cfg['quote']
    imgs_cfg: ConfigQuoteImgs = quote_cfg['imgs']
    img_file_name: str = imgs_cfg['fallback']
   
    img_file_path =  layers.get_asset_path( 
        imgs_path = imgs_cfg['overlay_dir'], 
        asset_name = img_file_name
    )
    
    try:
        fallback: ImageType = Image.open( img_file_path )
        return fallback

    except Exception as err:
        logging.error( err )
       
        quote_cfg: ConfigQuote = cfg['quote']
        mode, size, color = layers.parse_canvas_cfg( quote_cfg['canvas'] )
        fallback: ImageType = layers.get_pil_layer( mode, size, color )

        if fallback is not None:
            return fallback
        else:
            return Image.new( mode='RGB', size=(800,600), color='black')


def __author_crop( canvas: ImageType, author_img: ImageType) -> ImageType:
    author_w, author_h = author_img.size
    base_w, base_h = canvas.size

    crop_w = (author_w - base_w) // 2
    crop_h = (author_h - base_h) // 2
    crop_border = ( crop_w, crop_h, crop_w, crop_h ) #(left, top, right, bottom)

    author_img = ImageOps.crop( image = author_img, border = crop_border )
    return author_img



def __author_resize( canvas: ImageType, author_asset: ImageType, author_cfg: ConfigQuoteAuthor ) -> ImageType:
    
    resize_ratio: float = author_cfg['resize_limit_ratio']
    author_size: Tuple[int, int] = author_asset.size
    canvas_size: Tuple[int, int] = canvas.size
    img_size: Tuple[int, int] = __resize_it( author_size, canvas_size, resize_ratio )
    
    author_asset = author_asset.resize( img_size, Image.Resampling.BILINEAR )
    
    return author_asset


def __resize_it( 
    author_size: Tuple[ int, int ], 
    base_size: Tuple[ int, int ], 
    resize_ratio: float = 1.0 ) -> Tuple[int, int]:

    author_w, author_h = author_size
    base_w, base_h = base_size

    lim_h = base_h * resize_ratio
    lim_w = base_w * resize_ratio
    limit_size = ( lim_w, lim_h )

    if author_w >= lim_w and author_h >= lim_h:
        return __decrese_it( author_w, author_h, base_w, base_h, lim_w, lim_h )
    else:
        return __increse_it( author_size, base_size, limit_size )


def __decrese_it( 
    author_size: Tuple[ int, int ], 
    base_size: Tuple[ int, int ], 
    limit_size: Tuple[ int, int ] ) -> Tuple[int, int]:
    
    author_w, author_h = author_size
    base_w, base_h = base_size
    lim_w, lim_h = limit_size

    quo_w = base_w / author_w
    quo_h = base_h / author_h

    ratio = 1

    if quo_h > quo_w:
        ratio = (lim_w - author_w ) / author_w
    else:
        ratio = (lim_h - author_h ) / author_h

    author_h = round( author_h * ( 1 + ratio ) )
    author_w = round( author_w * ( 1 + ratio ) )

    return author_w, author_h


def __increse_it( 
    author_size: Tuple[ int, int ], 
    base_size: Tuple[ int, int ], 
    limit_size: Tuple[ int, int ] ) -> Tuple[int, int]:

    author_w, author_h = author_size
    base_w, base_h = base_size
    lim_w, lim_h = limit_size

    quo_w = base_w / author_w
    quo_h = base_h / author_h

    ratio = 1

    if quo_h > quo_w:
        ratio = (lim_h - author_h ) / author_h
    else:
        ratio = (lim_w - author_w ) / author_w

    author_h = round( author_h * ( 1 + ratio ) )
    author_w = round( author_w * ( 1 + ratio ) )
       
    return author_w, author_h
