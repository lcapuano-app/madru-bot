from dataclasses import dataclass
from enum import Enum
from typing import TypedDict, TYPE_CHECKING
from typing_extensions import Self

if TYPE_CHECKING:
    from models.config.config_app_model import AppConfigDict


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

    filename : str = None
    level    : LogLevel = None
    out_dir  : str = None


    def __init__(self, cfg: 'AppConfigDict') -> None:

        self.filename = cfg['log']['filename']
        self.out_dir = cfg['log']['out_dir']
        self.level = cfg['log']['level']
