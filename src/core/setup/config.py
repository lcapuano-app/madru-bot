import os
import shutil
from time import sleep

from typing import TYPE_CHECKING, Any, Dict
from jsonc_parser.parser import JsoncParser

#from core import App
from utils import error, validator, Spinner
from definitions import CONFIG_FILE, CONFIG_FALLBACK
from types.config import AppConf


#@Spinner(text='Loading config file')
def load_config( file_path: str = None ) -> None:
    
    """
        Tries to load default.jsonc file. 

        If not found it tries to create a new one from fallback/config folder.

        Then runs this dict through `utils.validator` to check for type errors.

        If anything fails... Let it crash!! `sys.exit()`

        Else creates an instance of `App()` setting the validated dict
        
        :returns: `None`
    """
   
    conf = __load_json_c( file_path )
    # sleep(3)
    # __validate_config( conf )
    # App().set_conf(conf)


#@Spinner(text='Validating config file props and types')
def __validate_config( conf: Any ) -> None:
    """ 
    *** At this momment it just a type checker! ***

    Tries to parse default.jsonc(json) to a valid `AppConfigDitc`.

    It iterates over, recursively, all json props matching with the `AppConf` structure

    Raises `TypeError` with a custom (default.json tree) message
    """

    keys_stack: str = 'CFG'

    error.raise_not_dict( conf )
    error.raise_not_typeddict( AppConf )
    validator.raise_missing_properties_keys( subject = conf, target = AppConf )
   
    for key in AppConf.__annotations__.keys():
   
        # we do not care form 'misc' dict, parse or validade anything into misc prop
        if key == 'misc': continue
        validator.match_typed_dict( 
            subject = conf[key], target = AppConf.__annotations__[key], keys_stack = keys_stack + f'.{key}' )

    
def __restore_default() -> str:

    if os.path.exists( CONFIG_FILE ):
       return CONFIG_FILE 
    else:
        try:
            file_path: str = shutil.copy2( src=CONFIG_FALLBACK, dst=CONFIG_FILE )
            return file_path
        except Exception as err:
            error.panic( err, where=__file__ )


#@Spinner(text='Loading default json/jsonc file')
def __load_json_c( file_path: str = None ) -> Dict:
    
    file_path: str = file_path if file_path is not None else CONFIG_FILE

    try:
        if not os.path.exists( file_path ):
            file_path = __restore_default()

        data: Dict = JsoncParser.parse_file( file_path )
        
        return data

    except Exception as err:       
        error.panic( err, where=__file__ )