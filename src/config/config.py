import os

from jsonc_parser.parser import JsoncParser

from definitions import CONFIG_DEV, CONFIG_PROD
from models.config import ConfigType
from validators import LogConfigValidator, QuoteConfigValidator


class AppConfig:

    __config: ConfigType = None

    def __init__(self) -> None:
        env = os.environ['ENV']
        file_path = CONFIG_DEV if env == 'DEV' else CONFIG_PROD
        data = AppConfig.__load_json_c( file_path )

        QuoteConfigValidator.crash_invalid( data )
        LogConfigValidator.crash_invalid( data )

        AppConfig.__config = data



    def get_cfg() -> ConfigType:

        if AppConfig.__config is not None:
            return AppConfig.__config

        AppConfig.__init__( AppConfig )

        return AppConfig.__config

    def get_quote_cfg():
        self = AppConfig
        return self.get_cfg()['quote']

    def get_log_cfg():
        self = AppConfig
        return self.get_cfg()['log']



    def __load_json_c( file_path: str ) -> dict:

        """
        Tries to parse .jsonc file
        No error handlres here!
        Let it crash!!
        We can continue without it """
        data = JsoncParser.parse_file( file_path )
        return data
