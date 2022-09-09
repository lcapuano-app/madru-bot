from PIL.Image import Image

from models import QuoteGenParamsType
from .build import QuoteCreate


class QuoteGen():

    def generate( params: QuoteGenParamsType ):
        print('no gen', params['color'])
        image = QuoteCreate.create( config=params )

    def generate_base64():
        ...

