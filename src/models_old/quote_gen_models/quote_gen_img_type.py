from typing import TypedDict

from PIL.Image import Image as ImageType


class QuoteGenImageType ( TypedDict ):
    b64  : str
    name : str
    obj  : ImageType
    url  : str
