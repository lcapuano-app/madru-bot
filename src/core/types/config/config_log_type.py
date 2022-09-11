from typing import TypedDict

from core.types.config.config_log_level_type import ConfigLogLevel


class ConfigLogType ( TypedDict ):
    filename : str
    level    : ConfigLogLevel
    out_dir  : str
