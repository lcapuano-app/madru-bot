from dataclasses import dataclass
from enum import Enum
from typing import TypedDict, TYPE_CHECKING

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


class LogConfigDict( TypedDict ):
    filename : str
    level    : LogLevel
    out_dir  : str


@dataclass
class LogConfig:

    filename : str
    level    : LogLevel
    out_dir  : str

    def __init__(self, cfg: 'AppConfigDict') -> None:
        self.filename = cfg['log']['filename']
        self.out_dir = cfg['log']['out_dir']
        self.level = cfg['log']['level']