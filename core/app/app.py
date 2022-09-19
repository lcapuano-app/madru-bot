from typing_extensions import Self

from models.config import AppConfig, AppConfigDict, ApiConfig, DiscordConfig, LogConfig, QuoteConfig


class App:

    __instance = None
    __config: AppConfig
    __conf_dict: AppConfigDict = None


    def __new__(cls: type[Self]) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    @property
    def config( self ):
        return self.__config


    def set_conf( self, cfg_dict: AppConfigDict ) -> None:
        if self.__conf_dict is None:
            self.__conf_dict = cfg_dict
            self.__init_app()


    def __init_app( self ) -> None:
        cfg = self.__conf_dict
        self.__config = AppConfig( 
            ApiConfig(cfg), DiscordConfig(cfg), LogConfig(cfg), QuoteConfig(cfg), misc=cfg['misc'] )

    