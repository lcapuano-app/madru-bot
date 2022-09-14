import logging
import math
import textwrap

from typing import List, Tuple
from PIL import ImageDraw, ImageFont
from PIL.Image import Image as ImageType
from PIL.ImageFont import FreeTypeFont

from definitions import BOTTOM_FONT_SIZE, QUOTE_FONT_SIZE, TEXT_MULTI_WRAP, TRANSPARENT
from utils import validator
from app_types.quote import QuoteGenReq, ColorMode
from app_types.config import ConfigQuote, ConfigQuoteTexQtTxt
from quote.layers import layers
logger = logging.getLogger(__name__)

def get_bottom_text_layer( 
    quote_req: QuoteGenReq, 
    canvas: ImageType, 
    cfg: ConfigQuote,
    walker_asset: ImageType,
    margin: int ) -> ImageType:
    
    try:
        bottom_text: str = quote_req['author']
        font_color: str = cfg['text']['bottom']['font_color']
        font_face: str = cfg['text']['bottom']['font_face']

        font_size: int = __get_font_size( cfg['text']['bottom'], canvas )
        font_size = font_size if font_size > 0 else BOTTOM_FONT_SIZE
       
        text_layer: ImageType = layers.get_pil_layer( ColorMode.RGBA.value, canvas.size, TRANSPARENT )

        font_tt: FreeTypeFont = ImageFont.truetype( font_face, font_size )

        pos: Tuple[int, int] = __get_bottom_text_pos(
            text = bottom_text,
            base_img = text_layer, 
            font_tt = font_tt,
            font_size = font_size, 
            margin = margin,
            walker_asset=walker_asset
        )

        draw = ImageDraw.Draw( text_layer )
        draw.text( xy=pos, text=bottom_text, fill=font_color, font=font_tt, align='right')

        return text_layer

    except Exception as err:
        # logging.error( get_bottom_text_layer.__name__ )
        # logging.error( __file__ )
        # logging.error( err )
        # logger.exception(err)
        return canvas


def get_quote_text_layer( quote_req: QuoteGenReq, cfg: ConfigQuote, canvas: ImageType ) -> ImageType:

    try:
        qt_txt_cfg: ConfigQuoteTexQtTxt = cfg['text']['quote_txt']
        quote_text: str = quote_req['msg']
        text_layer: ImageType = layers.get_pil_layer( ColorMode.RGBA.value, canvas.size, TRANSPARENT )

        quote_text, wrapped = __adjust_quote_text( quote_text, qt_txt_cfg )
        font_size: int = __adjust_font_size( text_layer, quote_text, qt_txt_cfg, wrapped )
        font_tt: FreeTypeFont = ImageFont.truetype( qt_txt_cfg['font_face'], font_size )
        pos = __get_quote_text_pos( quote_text, text_layer, font_tt )

        draw = ImageDraw.Draw( text_layer )
        
        draw.text( 
            xy = pos, 
            text = quote_text, 
            fill = qt_txt_cfg['font_color'], 
            font=font_tt, 
            anchor = 'ms', 
            align = 'center', 
            stroke_width = qt_txt_cfg['stroke_size'], 
            stroke_fill=  qt_txt_cfg['stroke_color']
        )

        return text_layer
 
    except Exception as err:
        # logging.error( get_bottom_text_layer.__name__ )
        # logging.error( __file__ )
        # logging.error( err )
        return canvas


def __get_font_size( cfg: ConfigQuoteTexQtTxt, canvas: ImageType ) -> int:
    validator.is_instance( cfg, ConfigQuote )
    #print( '------------------', ConfigQuoteTexQtTxt.__annotations__)
    try:
        
        if cfg['font_size'] > 0:
            return cfg['font_size']
        else:
            width, _ = canvas.size
            factor: float = cfg['size_factor']
            font_size: int = int( width * factor )
            return font_size

    except Exception as err:
        
        # logging.error( get_bottom_text_layer.__name__ )
        # logging.error( __file__ )
        # logging.error( err )
        return 0
        

def __get_bottom_text_pos( 
    text: str, 
    base_img: ImageType, 
    font_tt: FreeTypeFont,
    font_size: int,
    margin: int, 
    walker_asset: ImageType ) -> Tuple[int, int]:
    
    try:
        txt_w, txt_h = ImageDraw.Draw( base_img ).textsize( text, font_tt )
        img_w, img_h = base_img.size
        walker_w, walker_h = walker_asset.size

        x = int(img_w - txt_w - font_size - walker_w - margin)
        y = int(img_h - txt_h - font_size - margin)

        return x, y
    
    except Exception as err:
        # logging.error( get_bottom_text_layer.__name__ )
        # logging.error( __file__ )
        # logging.error( err )
        return (0, 0)


def __adjust_quote_text( text: str, txt_cfg: ConfigQuoteTexQtTxt ) -> Tuple[ str, List[str] ]:

    try:
        text = '“' + text + '”'
        wrap_width: int = __get_text_wrap_width( txt_cfg )
        wrapped = textwrap.wrap( text, wrap_width )
        text = '\n'.join( wrapped )

        return text, wrapped
    
    except Exception as err:
        # logging.error( get_bottom_text_layer.__name__ )
        # logging.error( __file__ )
        # logging.error( err )
        return text, [text ]


def __get_text_wrap_width( txt_cfg: ConfigQuoteTexQtTxt ) -> int:

    try:
        wrap_width: int = txt_cfg['wrap']
        
        if isinstance( wrap_width, int ) and wrap_width > 0:
            return wrap_width
        else:
            return TEXT_MULTI_WRAP

    except Exception as err:
        # logging.error( get_bottom_text_layer.__name__ )
        # logging.error( __file__ )
        # logging.error( err )
        return TEXT_MULTI_WRAP


def __adjust_font_size( canvas: ImageType, text: str, txt_cfg: ConfigQuoteTexQtTxt, wrapped: List[str] = [] ) -> int:

    try:
        font_face: str = txt_cfg['font_face']
        font_size: int = __get_font_size( txt_cfg['font_size'], canvas )
        font_size = font_size if font_size > 0 else QUOTE_FONT_SIZE

        canvas_x: int = canvas.size[0]
        font_tt: FreeTypeFont = ImageFont.truetype( font_face, font_size )
        txt_w, txt_h = ImageDraw.Draw( canvas ).textsize(text, font_tt )

        txt_img_limit = canvas_x - (canvas_x // 5)
        safe_font_size = font_size

        if len(wrapped) > 1:
            txt_img_limit = canvas_x - (canvas_x // 7)

        while txt_w < txt_img_limit:
            font_tt = ImageFont.truetype( font_face, int(font_size) )
            txt_w, txt_h = ImageDraw.Draw( canvas ).textsize( text, font_tt )

            if txt_w < txt_img_limit:
                safe_font_size = font_size

            font_size *= 1.1

        return math.ceil(safe_font_size)

    except Exception as err:
        logging.error( get_bottom_text_layer.__name__ )
        logging.error( __file__ )
        logging.error( err )
        return font_size


def __get_quote_text_pos( text: str, canvas: ImageType, font_tt: FreeTypeFont ) -> Tuple[int, int]:
    try:
        txt_w, txt_h = ImageDraw.Draw( canvas ).textsize( text, font_tt )
        img_w, img_h = canvas.size

        x = img_w // 2
        y =   (img_h - txt_h) // 2

        return x,y

    except Exception as err:
        # logging.error( get_bottom_text_layer.__name__ )
        # logging.error( __file__ )
        # logging.error( err )
        return 0, 0
    