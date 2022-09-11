from PIL import Image
from PIL.Image import Image as ImageType


class WalkerLayer:

    def create( canvas: ImageType ) -> tuple[ ImageType, ImageType ]:

        """
        Creates a new image with walker asset.
        :param canvas_cfg: Canvas created usil PIL.
        :returns: A 2-tuple, containing (walker_img: :py:class:`~PIL.Image.Image`, walker_canvas :py:class:`~PIL.Image.Image`).
        """