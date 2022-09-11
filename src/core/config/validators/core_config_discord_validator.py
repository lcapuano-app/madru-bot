from typing import Any

from core.types.config import ConfigDiscordType
from utils import DictValidator as Validator
from core.config.validators.core_config_validator_error import CoreConfigValidatorError


class CoreConfigDiscordValidator():


    def __init__(self, discord: ConfigDiscordType ) -> None:
        self.__discord = discord


    def validate( self ) -> ConfigDiscordType:

        try:
            #Validator.is_instance_of_err( self.__discord, self.__validator_pattern(), raise_err=True )
            return self.__discord

        except ValueError as err:
            CoreConfigValidatorError.throw_error( err, where=__file__ )


    def __validator_pattern( self ) -> list[dict[str, Any]]:
        return []