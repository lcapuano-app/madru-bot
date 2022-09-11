from typing import Any

from core.types.config import ConfigApiType
from utils import DictValidator as Validator
from core.config.validators.core_config_validator_error import CoreConfigValidatorError


class CoreConfigApiValidator():


    def __init__(self, api: ConfigApiType ) -> None:
        self.__api = api


    def validate( self ) -> ConfigApiType:

        try:
            #Validator.is_instance_of_err( self.discord, self.__validator_pattern(), raise_err=True )
            return self.__api

        except ValueError as err:
            CoreConfigValidatorError.throw_error( err, where=__file__ )


    def __validator_pattern( self ) -> list[dict[str, Any]]:
        return []