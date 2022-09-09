from enum import Enum
from typing import Any, List, Tuple, TypedDict
from typing_extensions import NotRequired
from PIL.Image import Image as ImageType

from validators import ValidateProps


################# API MODELS #################
class ApiQuoteAuthorType ( TypedDict ):
    displayName : str
    idName      : str
    quoteName   : str


class ApiQuoteImageType ( TypedDict ):
    sm : str
    qt : str


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


################ QUOTE MODELS ################
class QuoteGenImageType ( TypedDict ):
    b64  : str
    name : str
    obj  : ImageType
    url  : str


class QuoteGenModes( Enum ):
    RBG = 'RGB'
    RGBA = 'RGBA'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class QuoteGenParamsType ( TypedDict ):
    quote_id : str
    mode     : str
    size     : Tuple[ int, int ]
    color    : str


class QuoteGenType ( TypedDict ):
    author : str
    img    : QuoteGenImageType
    msg    : str

################# CFG MODELS #################

class ConfigApiType ( TypedDict ):
    pass


class ConfigDiscordType ( TypedDict ):
    pass


class ConfigLogLevel ( Enum ):
    CRITICAL = 50
    FATAL    = 50
    ERROR    = 40
    WARNING  = 30
    WARN     = 30
    INFO     = 20
    DEBUG    = 10
    NOTSET   = 0

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    @classmethod
    def get_value(self, enum_property_name):
        return getattr(self, enum_property_name)


class ConfigLogType ( TypedDict ):
    filename : str
    level    : ConfigLogLevel
    out_dir  : str


class ConfigQuoteCanvasType ( TypedDict ):
    color: str
    mode: QuoteGenModes
    height: int
    width: int


class ConfigQuoteType ( TypedDict ):
    canvas: ConfigQuoteCanvasType


class ConfigType ( TypedDict ):
    api     : ConfigApiType
    discord : ConfigDiscordType
    log     : ConfigLogType
    quote   : ConfigQuoteType


################# MODEL VALIDATORS #################

class ApiQuoteAuthorTypeValidator( ValidateProps ):

    def crash_invalid( data: Any, where: str = '' ) -> None:
        self = ApiQuoteAuthorTypeValidator

        self.exit_on_error( prop = 'displayName', obj = data, expected_type = str, where=where )
        self.exit_on_error( prop = 'idName',      obj = data, expected_type = str, where=where )
        self.exit_on_error( prop = 'quoteName',   obj = data, expected_type = str, where=where )


class ApiQuoteImageTypeValidator( ValidateProps ):

    def crash_invalid( data: Any, where: str = '' ) -> None:
        self = ApiQuoteImageTypeValidator

        self.exit_on_error( prop = 'sm', obj = data, expected_type = str, where=where )
        self.exit_on_error( prop = 'qt', obj = data, expected_type = str, where=where )


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


class QuoteGenTypeValidator( ValidateProps ):

    __props: list[str] = [ 'author', 'img', 'msg' ]

    def is_intance( obj: Any ) -> bool:
        self = QuoteGenTypeValidator

        return self.is_instance_of( subject=obj, target_keys=self.__props )


class QuoteGenParams():

    __color: str
    __quote_id: str
    __mode: QuoteGenModes
    __size: Tuple[int,int]

    def __init__(self, quote_id: str) -> None:
        self.__quote_id = quote_id
        self.__color = 'black'
        self.__mode = QuoteGenModes.RBG.value
        self.__size = (800, 600 )

    def get_params(self) -> QuoteGenParamsType:
        return {
            'color': self.__color,
            'mode': self.__mode,
            'quote_id': self.__quote_id,
            'size': self.__size
        }

    def generate( self, quote_cfg: cfg.ConfigQuoteCanvasType = None ) -> QuoteGenParamsType:
    #def generate( self, quote_cfg = None ) -> QuoteGenParamsType:

        if quote_cfg is None or quote_cfg:
            return self.get_params()

        else:
            return {
                'color': quote_cfg['color'],
                'mode': quote_cfg['mode'],
                'quote_id': self.__quote_id,
                'size': ( quote_cfg['width'], quote_cfg['height'] )
            }


