from typing import TypedDict

from app_types.config.config_api_type import ConfigApi
from app_types.config.config_discord_type import ConfigDiscord
from app_types.config.config_quote_type import ConfigQuote
from app_types.config.config_log_type import ConfigLog


class ConfigType ( TypedDict ):
    api     : ConfigApi
    discord : ConfigDiscord
    log     : ConfigLog
    quote   : ConfigQuote
