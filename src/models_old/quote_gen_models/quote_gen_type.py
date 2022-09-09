from typing import Any, TypedDict

from models.quote_gen_models.quote_gen_img_type import QuoteGenImageType
from validators import ValidateProps


class QuoteGenType ( TypedDict ):
    author : str
    img    : QuoteGenImageType
    msg    : str


class QuoteGenTypeValidator( ValidateProps ):

    __props: list[str] = [ 'author', 'img', 'msg' ]

    def is_intance( obj: Any ) -> bool:
        self = QuoteGenTypeValidator

        return self.is_instance_of( subject=obj, target_keys=self.__props )
