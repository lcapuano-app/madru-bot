from typing import Any

from core.types.config import ConfigQuoteType
from utils import DictValidator as Validator
from core.config.validators.core_config_validator_error import CoreConfigValidatorError
from core.config.validators.core_config_quote_canvas_validator import CoreConfigQuoteCanvasValidator
from core.config.validators.core_config_quote_imgs_validator import CoreConfigQuoteImgsValidator


class CoreConfigQuoteValidator():


    def __init__(self, quote: ConfigQuoteType ) -> None:
        self.__quote = quote


    def validate( self ) -> ConfigQuoteType:

        try:
            Validator.is_instance_of_err( self.__quote, self.__validator_pattern(), raise_err=True )
            self.__quote['canvas'] = CoreConfigQuoteCanvasValidator( self.__quote['canvas'] ).validate()
            self.__quote['imgs'] = CoreConfigQuoteImgsValidator( self.__quote['imgs'] ).validate()
            return self.__quote
            
        except ValueError as err:
            CoreConfigValidatorError.throw_error( err, where=__file__ )


    def __validator_pattern( self ) -> list[dict[str, Any]]:
        return [
            { 'key': 'canvas', 'typing': dict },
            { 'key': 'decor', 'typing': dict },
            { 'key': 'imgs', 'typing': dict },
            { 'key': 'walker', 'typing': dict }
        ]