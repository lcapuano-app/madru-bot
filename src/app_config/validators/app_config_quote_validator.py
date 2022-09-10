from typing import Any

from app_types.config import ConfigQuoteType
from utils import DictValidator as Validator
from app_config.validators.app_config_validator_error import AppConfigValidatorError
from app_config.validators.app_config_quote_canvas_validator import AppConfigQuoteCanvasValidator

class AppConfigQuoteValidator():


    def __init__(self, quote: ConfigQuoteType ) -> None:
        self.__quote = quote


    def validate( self ) -> ConfigQuoteType:

        try:
            Validator.is_instance_of_err( self.__quote, self.__validator_pattern(), raise_err=True )
            self.__quote['canvas'] = AppConfigQuoteCanvasValidator( self.__quote['canvas'] ).validate()

            return self.__quote
            
        except ValueError as err:
            AppConfigValidatorError.throw_error( err, where=__file__ )


    def __validator_pattern( self ) -> list[dict[str, Any]]:
        return [
            { 'key': 'canvas', 'typing': dict },
            { 'key': 'decor', 'typing': dict },
            { 'key': 'out_dir', 'typing': str },
            { 'key': 'walker', 'typing': dict }
        ]