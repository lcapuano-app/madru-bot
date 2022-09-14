from dataclasses import asdict, dataclass
from typing import TypedDict

from app.models.config.api import ApiConfig, ApiConfigDict
from app.models.config.discord import DiscordConfig, DiscordConfigDict
from app.models.config.log import LogConfig, LogConfigDict
from app.models.config.quote.config_quote_model import QuoteConfig, QuoteConfigDict


class AppConfigDict( TypedDict ):
    api     : ApiConfigDict
    discord : DiscordConfigDict
    log     : LogConfigDict
    quote   : QuoteConfigDict


@dataclass( frozen=True )
class AppConfig:

    api     : ApiConfig
    discord : DiscordConfig
    log     : LogConfig
    quote   : QuoteConfig
