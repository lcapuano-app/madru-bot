import os
import shutil

from jsonc_parser.parser import JsoncParser

from app import App
from utils import error
from definitions import CONFIG_FILE, CONFIG_FALLBACK


def load_config( file_path: str = None ) -> None:
    """
        Tries to load default.jsonc file. 
        If not found it tries to create a new one from fallback/config folder.

        If anything fails... Let it crash!! `sys.exit()`
        
        :returns: `dict`
    """
    cfg = __load_json_c( file_path )
    ##App().set_config(cfg)
    #App().config = cfg
    App().cfg_dict = cfg
    

def __restore_default() -> str:

    if os.path.exists( CONFIG_FILE ):
       return CONFIG_FILE 
    else:
        try:
            file_path = shutil.copy2( src=CONFIG_FALLBACK, dst=CONFIG_FILE )
            return file_path
        except Exception as err:
            error.panic( err, where=__file__ )


def __load_json_c( file_path: str = None ) -> dict:
    
    file_path = file_path if file_path is not None else CONFIG_FILE

    try:
        if not os.path.exists( file_path ):
            file_path = __restore_default()

        data = JsoncParser.parse_file( file_path )
        return data

    except Exception as err:
        error.panic( err, where=__file__ )