from enum import Enum


class QuoteGenModes( Enum ):
    RBG = 'RGB'
    RGBA = 'RGBA'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_