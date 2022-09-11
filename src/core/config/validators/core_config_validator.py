from typing import Any

from core.types.config import ConfigType
from utils import DictValidator as Validator
from core.config.validators.core_config_validator_error import CoreConfigValidatorError
from core.config.validators.core_config_api_validator import CoreConfigApiValidator
from core.config.validators.core_config_discord_validator import CoreConfigDiscordValidator
from core.config.validators.core_config_log_validator import CoreConfigLogValidator
from core.config.validators.core_config_quote_validator import CoreConfigQuoteValidator


class CoreConfigValidator:



    def __init__( self, config: ConfigType ) -> None:
        self.__config = config


    def validate( self ) -> ConfigType:

        try:
            Validator.is_instance_of_err( self.__config, self.__validator_pattern(), raise_err=True )
            cfg = self.__config
            cfg['api'] = CoreConfigApiValidator( cfg['api'] ).validate()
            cfg['discord'] = CoreConfigDiscordValidator( cfg['discord'] ).validate()
            cfg['log'] = CoreConfigLogValidator( cfg['log'] ).validate()
            cfg['quote'] = CoreConfigQuoteValidator( cfg['quote'] ).validate()

            return self.__config
            
        except ValueError as err:
            CoreConfigValidatorError.throw_error( err, where=__file__ )


    def __validator_pattern( self ) -> list[dict[str, Any]]:
        return [
            { 'key': 'api', 'typing': dict },
            { 'key': 'discord', 'typing': dict },
            { 'key': 'log', 'typing': dict },
            { 'key': 'quote', 'typing': dict }
        ]