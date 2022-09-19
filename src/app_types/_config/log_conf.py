from enum import Enum
from typing import TypedDict


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
    

class LogConf( TypedDict ):
    filename : str
    level    : LogLevel
    out_dir  : str

