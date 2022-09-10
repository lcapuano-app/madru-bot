from app_config.app_config_model import AppConfigModel
from app_config.app_config_controller import AppConfigController


class AppConfig ():

    __config: AppConfigModel = None


    def __init__( self ) -> None:
        pass

    @property
    def get( self ) -> AppConfigModel:

        if self.__config is None:
            self.__load_config()

        return self.__config


    def __load_config( self ) -> None:
        self.__config =  AppConfigController().set_cfg()