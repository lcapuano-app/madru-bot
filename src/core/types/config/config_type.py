from typing import TypedDict

from core.types.config.config_api_type import ConfigApiType
from core.types.config.config_discord_type import ConfigDiscordType
from core.types.config.config_quote_type import ConfigQuoteType
from core.types.config.config_log_type import ConfigLogType


class ConfigType ( TypedDict ):
    api     : ConfigApiType
    discord : ConfigDiscordType
    log     : ConfigLogType
    quote   : ConfigQuoteType
