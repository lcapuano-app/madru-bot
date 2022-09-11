from core.config.core_config_model import CoreConfigModel
from core.config.core_config_controller import CoreConfigController


class CoreConfig ():

    __config: CoreConfigModel = None


    def __init__( self ) -> None:
        pass

    @property
    def get( self ) -> CoreConfigModel:

        if self.__config is None:
            self.__load_config()

        return self.__config


    def __load_config( self ) -> None:
        self.__config =  CoreConfigController().set_cfg()