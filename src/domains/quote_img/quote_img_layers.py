from PIL import Image
from PIL.Image import Image as ImageType


class QuoteImageLayers ():

    __a_background: ImageType = None
    __b_overlay: ImageType = None
    __c_quote_text: ImageType = None
    __d_walker: ImageType = None
    __e_walker: ImageType = None

    def __init__(self) -> None:
        self.__a_background: ImageType = None