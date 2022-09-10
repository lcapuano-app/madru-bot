from typing import Any

from app_types.config import ConfigLogType, ConfigLogLevel
from utils import DictValidator as Validator
from app_config.validators.app_config_validator_error import AppConfigValidatorError


class AppConfigLogValidator():


    def __init__(self, log: ConfigLogType ) -> None:
        self.__log = log


    def validate( self ) -> ConfigLogType:
        
        try:
            Validator.is_instance_of_err( self.__log, self.__validator_pattern(), raise_err=True )
            """ Log level must be some integer declared into ConfigLogLevel
            We will raise an error in case it is not """
            if not ConfigLogLevel.has_value( self.__log['level'] ):
                Validator.print_and_exit(
                    prop="config.log.level",
                    missing=False,
                    should_be='<class int> 10(DEBUG) | 20(INFO) | 30(WARNING) | (40)ERROR | (50)CRITICAL',
                    where = __file__,
                    val= self.__log['level']
                )
                
            return self.__log

        except ValueError as err:
            AppConfigValidatorError.throw_error( err, where=__file__ )


    def __validator_pattern( self ) -> list[dict[str, Any]]:
        return [
            { 'key': 'level', 'typing': int },
            { 'key': 'filename', 'typing': str },
            { 'key': 'out_dir', 'typing': str }
        ]