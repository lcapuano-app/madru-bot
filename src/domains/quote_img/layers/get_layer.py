import logging

from PIL import Image
from PIL.Image import Image as ImageType
from typing import Tuple

from core.types.quote import QuoteGenCanvasType, QuoteGenModes
from core.config import CoreConfig


class GetLayer:

    def __init__(
        self, 
        mode: QuoteGenModes = None, 
        size: Tuple[int, int] = None, 
        color: str = None  ) -> None:

        mode_dflt, size_dflt, color_dflt = self.__get_canvas_defaults()

        self.__mode = mode if mode is not None else mode_dflt
        self.__size = size if size is not None else size_dflt
        self.__color = color if color is not None else color_dflt


    def create( canvas_cfg: QuoteGenCanvasType = None ) -> ImageType:
        """
        Creates a new canvas using PIL.
        :param canvas_cfg: `QuoteGenCanvasType`. See: 
          :ref:`types.quote.quote_gen_canvas_type`
        :returns: :py:class:`~PIL.Image.Image`.
        """

        if canvas_cfg is None:
            canvas_cfg = GetLayer.__canvas_cfg

        mode: QuoteGenModes = canvas_cfg['mode']
        size: Tuple[ int, int ] = ( canvas_cfg['width'], canvas_cfg['height'] )
        color: str = canvas_cfg['color']

        try:
            background = Image.new( mode, size, color )
            return background

        except Exception as err:
            logging.critical( 'Could not create background layer', err )
            return None


    def empty( self, 
        mode: QuoteGenModes = None, 
        size: Tuple[int, int] = None, 
        color: str = None ) -> ImageType:

        mode, size, color = self.__get_missing_params( mode, size, color )
        
        return self.__get_pil_layer( mode, size, color )


    def transparent( self, size: Tuple[int, int] = None ) -> ImageType:
        mode = QuoteGenModes.RGBA
        color = 'rbga(0,0,0,0)'
        mode, size, color = self.__get_missing_params( mode, size, color )

        return self.__get_pil_layer( mode, size, color )


    def __get_pil_layer( self, mode: QuoteGenModes, size: Tuple[int, int], color: str ) -> ImageType:

        try:
            layer = Image.new( mode, size, color )
            return layer

        except Exception as err:
            logging.critical( 'Could not create empty layer', err )
            return None

    
    @staticmethod
    def parse_canvas_cfg( 
        canvas_cfg: QuoteGenCanvasType ) -> Tuple[QuoteGenModes, Tuple[int, int], str]:

        mode: QuoteGenModes = canvas_cfg['mode']
        size: Tuple[ int, int ] = ( canvas_cfg['width'], canvas_cfg['height'] )
        color: str = canvas_cfg['color']

        return mode, size, color


    @staticmethod
    def __get_canvas_defaults() -> Tuple[QuoteGenModes, Tuple[int, int], str]:
        canvas_cfg =  CoreConfig().get.quote['canvas']
        return GetLayer.parse_canvas_cfg( canvas_cfg )

    
    def __get_missing_params( 
        self, 
        mode: QuoteGenModes = None, 
        size: Tuple[int, int] = None, 
        color: str = None ) -> Tuple[QuoteGenModes, Tuple[int, int], str]:

        mode = mode if mode is not None else self.__mode
        size = size if size is not None else self.__size
        color = color if color is not None else self.__color

        return mode, size, color
