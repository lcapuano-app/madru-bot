import os
from pprint import pprint
import shutil
import sys

from typing import TypedDict
from enum import Enum
from jsonc_parser.parser import JsoncParser
from colorama import Fore, Style

from definitions import CONFIG_DEV, CONFIG_PROD, CONFIG_FAILOVER_DEV, CONFIG_FAILOVER_PROD
from utils.dict_validator import DictValidator as Validator


class ConfigApiType ( TypedDict ):
    pass

class ConfigDiscordType ( TypedDict ):
    pass

class ConfigLogLevel ( Enum ):
    CRITICAL = 50
    FATAL    = 50
    ERROR    = 40
    WARNING  = 30
    WARN     = 30
    INFO     = 20
    DEBUG    = 10
    NOTSET   = 0

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    @classmethod
    def get_value(self, enum_property_name):
        return getattr(self, enum_property_name)

class ConfigLogType ( TypedDict ):
    filename : str
    level    : ConfigLogLevel
    out_dir  : str


class ConfigQuoteCanvasType ( TypedDict ):
    color: str
    mode: str
    height: int
    width: int


class ConfigQuoteType ( TypedDict ):
    canvas: ConfigQuoteCanvasType
    decor: dict
    out_dir: str
    walker: dict

class ConfigType ( TypedDict ):
    api     : ConfigApiType
    discord : ConfigDiscordType
    log     : ConfigLogType
    quote   : ConfigQuoteType


class AppConfig ():

    __config: ConfigType = None


    def __init__( self ) -> None:

        self.__config_api = None
        self.__config_discord = None
        self.__config_quote = None
        self.__config_log = None
        self.__set_validator_patterns()

    @property
    def config( self ) -> ConfigType:

        if self.__config is None:
            self.__load_config()

        return self.__config


    @property
    def cfg_log( self ) -> ConfigLogType:
        return self.config['log']


    @property
    def cfg_quote( self ) -> ConfigQuoteType:
        return self.config['quote']


    @property
    def cfg_quote_canvas( self ) -> ConfigQuoteCanvasType:
        return self.config['quote']['canvas']


    def __load_config( self ) -> None:

        file_path = self.__get_file_path()

        self.__config = self.__load_json_c( file_path )
        self.__validate()
        self.__config_api: ConfigApiType = self.__config['api']
        self.__config_discord: ConfigDiscordType = self.__config['discord']
        self.__config_quote: ConfigQuoteType = self.__config['quote']

        self.__config_quote


    def __get_file_path( self ) -> str:

        env = os.environ['ENV']
        file_path = CONFIG_DEV if env == 'DEV' else CONFIG_PROD
        file_exisits = os.path.exists( file_path )

        if file_exisits:
            return file_path

        else:
            self.__restore_default_jsonc()


        return file_path


    def __restore_default_jsonc( self ) -> None:

        # Create (copy) production.jsonc if not exists
        if not os.path.exists( CONFIG_PROD ):
            shutil.copy2( src=CONFIG_FAILOVER_PROD, dst=CONFIG_PROD )

        # Create (copy) default.jsonc if not exists
        if not os.path.exists( CONFIG_DEV ):
            shutil.copy2( src=CONFIG_FAILOVER_DEV, dst=CONFIG_DEV )


    def __load_json_c( self, file_path: str ) -> dict:
        """
            Tries to parse .jsonc file. No error handlres here!
            Let it crash!! We can continue without it
            returns dict
        """
        data = JsoncParser.parse_file( file_path )
        return data


    def __validate( self ) -> None:
        cfg = self.__config

        if cfg is None:
            return False

        """ We can not continue if there were any erros into cfg object.
        Rasing errors (True) will crash the app """
        raise_errors = True

        """ Validating every nested level of the default/production object
        Validator will be called for eache one
        If there is an error wi will raise and crash the app"""
        try:
            # config
            Validator.is_instance_of_err( cfg, self.__config_pattern, raise_errors )

            # config >> api
            #Validator.is_instance_of_err( cfg['api'], self.__co, raise_errors )

            # config >> log
            Validator.is_instance_of_err( cfg['log'], self.__config_log_pattern, raise_errors )

            """ Log level must be some integer declared into ConfigLogLevel
            We will raise an error in case it is not """
            if not ConfigLogLevel.has_value( cfg['log']['level'] ):
                Validator.print_and_exit(
                    prop="config.log.level",
                    missing=False,
                    should_be='<class int> 10(DEBUG) | 20(INFO) | 30(WARNING) | (40)ERROR | (50)CRITICAL',
                    where = __file__,
                    val= cfg['log']['level']
                )

            # config >> quote
            Validator.is_instance_of_err( cfg['quote'], self.__config_quote_pattern, raise_errors )

            # config >> quote >> canvas
            Validator.is_instance_of_err( cfg['quote']['canvas'], self.__config_quote_canvas_pattern, raise_errors )
            """ Canvas mode must be RGB or RGBA, Validator checks for a string.
            Now we apply this constraint (default RGB) """
            curr_mode = self.__config['quote']['canvas']['mode']
            mode_constrained = curr_mode if curr_mode == 'RGBA' else 'RGB'
            self.__config['quote']['canvas']['mode'] = mode_constrained


        except ValueError as err:
            print(f'{Fore.RED}>> !! FATAL ERROR !!{Style.RESET_ALL}')
            print(f"{Fore.YELLOW}>> { err.args[0] }")
            pprint(err.args[1], indent=4)
            sys.exit()


    def __set_validator_patterns( self ) -> None:

        # config
        self.__config_pattern = [
            { 'key': 'api', 'typing': dict },
            { 'key': 'discord', 'typing': dict },
            { 'key': 'log', 'typing': dict },
            { 'key': 'quote', 'typing': dict }
        ]

         # config >> log
        self.__config_log_pattern = [
            { 'key': 'level', 'typing': int },
            { 'key': 'filename', 'typing': str },
            { 'key': 'out_dir', 'typing': str }
        ]

        # config >> quote
        self.__config_quote_pattern = [
            { 'key': 'canvas', 'typing': dict },
            { 'key': 'decor', 'typing': dict },
            { 'key': 'out_dir', 'typing': str },
            { 'key': 'walker', 'typing': dict }
        ]

        # config >> quote >> canvas
        self.__config_quote_canvas_pattern = [
            { 'key': 'color', 'typing': str },
            { 'key': 'mode', 'typing': str },
            { 'key': 'height', 'typing': int },
            { 'key': 'width', 'typing': int }
        ]
