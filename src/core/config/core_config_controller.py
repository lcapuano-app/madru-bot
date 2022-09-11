import os
import shutil

from jsonc_parser.parser import JsoncParser

from definitions import CONFIG_DEV, CONFIG_PROD, CONFIG_FAILOVER_DEV, CONFIG_FAILOVER_PROD
from core.types.config import ConfigType
from core.config.validators import CoreConfigValidator
from core.config.core_config_model import CoreConfigModel


class CoreConfigController ():

    def __init__(self) -> None:
        pass
    
    def set_cfg( self ) -> CoreConfigModel:

        file_path = self.__get_file_path()
        json_data: dict = self.__load_json_c( file_path )

        config: ConfigType = CoreConfigValidator( json_data ).validate()

        return CoreConfigModel( config )


    def __load_json_c( self, file_path: str ) -> dict:
        """
            Tries to parse .jsonc file. No error handlres here!
            Let it crash!! We can continue without it
            returns dict
        """
        data = JsoncParser.parse_file( file_path )
        return data


    def __get_file_path( self ) -> str:

        env = os.environ['ENV']
        file_path = CONFIG_DEV if env == 'DEV' else CONFIG_PROD
        file_exisits = os.path.exists( file_path )

        if file_exisits:
            return file_path

        else:
            self.__restore_default_jsonc()
            self.set_cfg()


        print('CHEGA AQUI NE')
        return file_path


    def __restore_default_jsonc( self ) -> None:

        # Create (copy) production.jsonc if not exists
        if not os.path.exists( CONFIG_PROD ):
            shutil.copy2( src=CONFIG_FAILOVER_PROD, dst=CONFIG_PROD )

        # Create (copy) default.jsonc if not exists
        if not os.path.exists( CONFIG_DEV ):
            shutil.copy2( src=CONFIG_FAILOVER_DEV, dst=CONFIG_DEV )
