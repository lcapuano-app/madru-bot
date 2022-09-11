import logging

from PIL import Image
from PIL.Image import Image as ImageType
from typing import Tuple

from core.types.quote import QuoteGenCanvasType, QuoteGenModes


class BackgroundLayer:

    @staticmethod
    def create( canvas_cfg: QuoteGenCanvasType ) -> ImageType:
        """
        Creates a new canvas using PIL.
        :param canvas_cfg: `QuoteGenCanvasType`. See: 
          :ref:`types.quote.quote_gen_canvas_type`
        :returns: :py:class:`~PIL.Image.Image`.
        """
        mode: QuoteGenModes = canvas_cfg['mode']
        size: Tuple[ int, int ] = ( canvas_cfg['width'], canvas_cfg['height'] )
        color: str = canvas_cfg['color']

        try:
            background = Image.new( mode, size, color )
            return background

        except Exception as err:
            logging.critical( 'Could not create background layer', err )
            return None