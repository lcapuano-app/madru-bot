from typing import Any

from core.types.config import ConfigQuoteCanvasType
from utils import DictValidator as Validator
from core.config.validators.core_config_validator_error import CoreConfigValidatorError


class CoreConfigQuoteCanvasValidator():


    def __init__(self, canvas: ConfigQuoteCanvasType ) -> None:
        self.__canvas = canvas


    def validate( self ) -> ConfigQuoteCanvasType:

        try:
            Validator.is_instance_of_err( self.__canvas, self.__validator_pattern(), raise_err=True )
            """ Canvas mode must be RGB or RGBA, Validator checks for a string.
            Now we apply this constraint (default RGB) """
            curr_mode = self.__canvas['mode']
            mode_constrained = curr_mode if curr_mode == 'RGBA' else 'RGB'
            self.__canvas['mode'] = mode_constrained
            return self.__canvas

        except ValueError as err:
            CoreConfigValidatorError.throw_error( err, where=__file__ )


    def __validator_pattern( self ) -> list[dict[str, Any]]:
        return [
            { 'key': 'color', 'typing': str },
            { 'key': 'mode', 'typing': str },
            { 'key': 'height', 'typing': int },
            { 'key': 'width', 'typing': int }
        ]