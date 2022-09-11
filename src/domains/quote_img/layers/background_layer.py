import logging

from PIL import Image
from PIL.Image import Image as ImageType
from typing import Tuple

from core.types.quote import QuoteGenCanvasType, QuoteGenModes
from domains.quote_img.layers.get_layer import GetLayer


class BackgroundLayer:

    @staticmethod
    def create( canvas_cfg: QuoteGenCanvasType = None ) -> ImageType:
        """
        Creates a new background using PIL.

        :returns: :py:class:`~PIL.Image.Image`.
        """
        get_layer = GetLayer()
        mode, size, color = get_layer.parse_canvas_cfg( canvas_cfg )
        background = get_layer.empty( mode, size, color )

        return background