from typing import Any

from core.types.config import ConfigQuoteImgsType
from utils import DictValidator as Validator
from core.config.validators.core_config_validator_error import CoreConfigValidatorError


class CoreConfigQuoteImgsValidator():


    def __init__(self, imgs: ConfigQuoteImgsType ) -> None:
        self.__imgs = imgs


    def validate( self ) -> ConfigQuoteImgsType:
        
        try:
            Validator.is_instance_of_err( self.__imgs, self.__validator_pattern(), raise_err=True )
            return self.__imgs

        except ValueError as err:
            CoreConfigValidatorError.throw_error( err, where=__file__ )


    def __validator_pattern( self ) -> list[dict[str, Any]]:
        return [
            { 'key': 'overlay_dir', 'typing': str },
            { 'key': 'out_dir', 'typing': str }
        ]