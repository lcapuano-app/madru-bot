from typing import Any

from app_types.config import ConfigType
from utils import DictValidator as Validator
from app_config.validators.app_config_validator_error import AppConfigValidatorError
from app_config.validators.app_config_api_validator import AppConfigApiValidator
from app_config.validators.app_config_discord_validator import AppConfigDiscordValidator
from app_config.validators.app_config_log_validator import AppConfigLogValidator
from app_config.validators.app_config_quote_validator import AppConfigQuoteValidator


class AppConfigValidator:



    def __init__( self, config: ConfigType ) -> None:
        self.__config = config


    def validate( self ) -> ConfigType:

        try:
            Validator.is_instance_of_err( self.__config, self.__validator_pattern(), raise_err=True )
            cfg = self.__config
            cfg['api'] = AppConfigApiValidator( cfg['api'] ).validate()
            cfg['discord'] = AppConfigDiscordValidator( cfg['discord'] ).validate()
            cfg['log'] = AppConfigLogValidator( cfg['log'] ).validate()
            cfg['quote'] = AppConfigQuoteValidator( cfg['quote'] ).validate()

            return self.__config
            
        except ValueError as err:
            AppConfigValidatorError.throw_error( err, where=__file__ )


    def __validator_pattern( self ) -> list[dict[str, Any]]:
        return [
            { 'key': 'api', 'typing': dict },
            { 'key': 'discord', 'typing': dict },
            { 'key': 'log', 'typing': dict },
            { 'key': 'quote', 'typing': dict }
        ]