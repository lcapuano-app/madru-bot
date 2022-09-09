from enum import Enum
from typing import Any, List, TypedDict
from typing_extensions import NotRequired

from models.api_models.api_quote.api_quote_author_type import ApiQuoteAuthorType, ApiQuoteAuthorTypeValidator
from models.api_models.api_quote.api_quote_image_type import ApiQuoteImageType, ApiQuoteImageTypeValidator
from validators import ValidateProps


class ApiQuoteCateg( Enum ):
    ALEATORIA = 'ALEATORIA'
    BRONCA    = 'BRONCA'
    ERROR     = 'ERROR'
    OK        = 'OK'
    OPCOES    = 'OPCOES'
    RECLAMA   = 'RECLAMA'
    SARRO     = 'SARRO'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class ApiQuoteType ( TypedDict ):
    _id       : NotRequired[str]
    author    : ApiQuoteAuthorType
    imgs      : ApiQuoteImageType
    msg       : str
    type      : List[ApiQuoteCateg]
    createdAt : NotRequired[str]
    updatedAt : NotRequired[str]


class ApiQuoteTypeValidator( ValidateProps ):

    __props: list[str] = [
        'author',
        'imgs',
        'msg',
        'type',
    ]

    def is_intance( obj: Any ) -> bool:
        self = ApiQuoteTypeValidator

        return self.is_instance_of( subject=obj, target_keys=self.__props )

    def crash_invalid( data: Any, where: str = '' ) -> None:
        self = ApiQuoteTypeValidator

        self.exit_on_error( prop='author', obj=data, expected_type=object, where=where )
        self.exit_on_error( prop='imgs',   obj=data, expected_type=object, where=where )
        self.exit_on_error( prop='msg',    obj=data, expected_type=str,    where=where )
        self.exit_on_error( prop='type',   obj=data, expected_type=object, where=where )

        self.__crash_categs( data=data, where=where )

        ApiQuoteAuthorTypeValidator.crash_invalid( data=data['author'], where=where )
        ApiQuoteImageTypeValidator.crash_invalid( data=data['imgs'], where=where )

    def __crash_categs( data: Any, where: str = '') -> None:
        self = ApiQuoteTypeValidator

        categs: List[ApiQuoteCateg] = data['type']

        for cat in categs:
            if not ApiQuoteCateg.has_value( cat ):
                self.print_and_exit(
                    prop=f'type ({cat})',
                    missing=False,
                    should_be='<list str> ALEATORIA | BRONCA | ERROR | OK | OPCOES | SARRO | RECLAMA',
                    where=where
                )

