from app_types.config import (
    ConfigApiType,
    ConfigDiscordType,
    ConfigLogType,
    ConfigQuoteType,
    ConfigType
)

class AppConfigModel ():

    __cfg: ConfigType
    __api: ConfigApiType
    __discord: ConfigDiscordType
    __log: ConfigLogType
    __quote: ConfigQuoteType
    

    def __init__(self, config: ConfigType ) -> None:

        self.__cfg = config
        self.__api = config['api']
        self.__discord = config['discord']
        self.__log = config['log']
        self.__quote = config['quote']

    @property
    def cfg( self ) -> ConfigType:
        return self.__cfg


    @property
    def api( self ) -> ConfigLogType:
        return self.__api


    @property
    def api( self ) -> ConfigDiscordType:
        return self.__discord


    @property
    def log( self ) -> ConfigLogType:
        return self.__log


    @property
    def quote( self ) -> ConfigQuoteType:
        return self.__quote
