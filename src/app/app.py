from app.models.config import AppConfig, AppConfigDict, ApiConfig, DiscordConfig, LogConfig, QuoteConfig


class _App:

    _instance = None
    __config: AppConfig
    __cfg_dict: AppConfigDict


    @property
    def cfg_dict( self ) -> AppConfigDict:
        return self.__cfg_dict


    @cfg_dict.setter
    def cfg_dict( self, cfg_dict: AppConfigDict ) -> None:
        self.__cfg_dict = cfg_dict
        self.__init_app()

    @property
    def config( self ):
        return self.__config


    def __init_app( self ) -> None:
        cfg = self.__cfg_dict
        self.__config = AppConfig( 
            ApiConfig(cfg), DiscordConfig(cfg), LogConfig(cfg), QuoteConfig(cfg) )



def App():
    if _App._instance is None:
        _App._instance = _App()
    return _App._instance