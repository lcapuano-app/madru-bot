from typing import TypedDict

from models.config.config_api_type import ConfigApiType
from models.config.config_discord_type import ConfigDiscordType
from models.config.config_quote_type import ConfigQuoteType
from models.config.config_log_type import ConfigLogType


class ConfigType ( TypedDict ):
    api     : ConfigApiType
    discord : ConfigDiscordType
    log     : ConfigLogType
    quote   : ConfigQuoteType
