from typing import TypedDict

from app_types.config.config_api_type import ConfigApiType
from app_types.config.config_discord_type import ConfigDiscordType
from app_types.config.config_quote_type import ConfigQuoteType
from app_types.config.config_log_type import ConfigLogType


class ConfigType ( TypedDict ):
    api     : ConfigApiType
    discord : ConfigDiscordType
    log     : ConfigLogType
    quote   : ConfigQuoteType
