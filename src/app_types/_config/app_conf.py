from enum import Enum
from typing import Dict, TypedDict

from app_types.config import ApiConf, DiscordConf, LogConf, QuoteConf


class AppConf( TypedDict ):
    api     : ApiConf
    discord : DiscordConf
    log     : LogConf
    quote   : QuoteConf
    misc    : Dict
