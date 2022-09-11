from typing import Any

from utils.math import try_parse_int

class CoreAssertLogLevel:

    def __init__(self, level: int ) -> None:
        self.__level = level

    def get_asserted( self ) -> int:
        
        level: int = self.__level

        level = try_parse_int( level )

        if level == 0:
            return 0 # logging.NOTSET value

        elif level >= 50:
            return 50 # logging.CRITICAL value

        elif level % 10  == 0:
            return level # level is equal to 10|20|30|40 (logging consts )

        else:
            mod = 10
            level = abs(level % mod - mod) + level # closest value to logging consts (round up, 22 => 30)
            return level