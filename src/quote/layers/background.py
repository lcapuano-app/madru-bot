from PIL.Image import Image as ImageType

from quote.layers import layers
from app_types.quote import QuoteGenCanvas


def get_background_layer( canvas_cfg: QuoteGenCanvas ) -> ImageType:

    mode, size, color = layers.parse_canvas_cfg( canvas_cfg )
    background = layers.get_pil_layer( mode, size, color )

    return background