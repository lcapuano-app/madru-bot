import os
import shutil
from time import sleep
from typing import Dict

from jsonc_parser.parser import JsoncParser

from app import App
from app.models.config.quote import QuoteConfig
from app.parsers import parse_to_app
from utils import error
from definitions import CONFIG_FILE, CONFIG_FALLBACK


def load_config( file_path: str = None ) -> None:
    """
        Tries to load default.jsonc file. 
        If not found it tries to create a new one from fallback/config folder.

        If anything fails... Let it crash!! `sys.exit()`
        
        :returns: `dict`
    """
    conf = __load_json_c( file_path )
    
    parse_to_app( conf )
    a = App()
    b = App()
    App().set_conf(conf)
    print(App().config.api.assets.url_get)
    QuoteConfig({ 
        'api':{
            'assets': {
                'url_get': 'doiahjhdiosad',
                'url_post': 'postpostpost'
            }
        }
    }) 
    #App().config.api.assets.url_get = 'doakjshojdhsa'
    b = App()
    b.set_conf(conf)
    print(f'{a is b=}')
    print(App().config.quote.author)
    # print(App().config.api.assets)
    # a.cfg_dict = 2
    # print(a.config)
    #App().cfg_dict = conf
    
    

def __restore_default() -> str:

    if os.path.exists( CONFIG_FILE ):
       return CONFIG_FILE 
    else:
        try:
            file_path: str = shutil.copy2( src=CONFIG_FALLBACK, dst=CONFIG_FILE )
            return file_path
        except Exception as err:
            error.panic( err, where=__file__ )


def __load_json_c( file_path: str = None ) -> Dict:
    
    file_path: str = file_path if file_path is not None else CONFIG_FILE

    try:
        if not os.path.exists( file_path ):
            file_path = __restore_default()

        data: Dict = JsoncParser.parse_file( file_path )
        return data

    except Exception as err:
        error.panic( err, where=__file__ )