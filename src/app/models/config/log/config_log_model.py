from dataclasses import dataclass
from enum import Enum
from typing import TypedDict, TYPE_CHECKING
from typing_extensions import Self

if TYPE_CHECKING:
    from app.models.config.config_app_model import AppConfigDict


class LogLevel ( Enum ):
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

    __type__ = type(0)


class LogConfigDict( TypedDict ):
    filename : str
    level    : LogLevel
    out_dir  : str


@dataclass
class LogConfig:

    __instance : Self = None
    __filename : str = None
    __level    : LogLevel = None
    __out_dir  : str = None

    def __new__(cls: type[Self], *args) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, cfg: 'AppConfigDict') -> None:

        if self.__filename is None:
            self.__filename = cfg['log']['filename']

        if self.__out_dir is None:
            self.__out_dir = cfg['log']['out_dir']

        if self.__level is None:
            self.__level = cfg['log']['level']

    
    @property
    def filename( self ) -> str:
        return self.__filename

    @property
    def level( self ) -> LogLevel:
        return self.__level

    @property
    def out_dir( self ) -> str:
        return self.__out_dir