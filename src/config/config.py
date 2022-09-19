import os
import shutil

from typing import Any, Dict
from jsonc_parser.parser import JsoncParser
from app_types.config import AppConf

from utils import error, Spinner, validator
from definitions import CONFIG_FILE, CONFIG_FALLBACK
from app_types.config import AppConf
from app import App
from fn_result import Result, Ok,Err


@Spinner(text='Loading config file')
def load_config( file_path: str = None ) -> None:
    
    """
        Tries to load default.jsonc file. 

        If not found it tries to create a new one from fallback/config folder.

        Then runs this dict through `utils.validator` to check for type errors.

        If anything fails... Let it crash!! `sys.exit()`

        Else creates an instance of `App()` setting the validated dict
        
    """
    
    raw_data: Dict = None
    conf: AppConf = None

    match __load_json_c( file_path ):
        case Ok( data ): raw_data = data
        case Err( err ): __restore_default()

    conf = __validate_config( raw_data ).unwrap()

    App.set_conf(conf)
    ##App.set_conf( conf ).unwrap()
    
   

@Spinner(text='Loading default json/jsonc file')
def __load_json_c( file_path: str = None ) -> Result[Dict, Exception]:

    file_path: str = file_path if file_path is not None else CONFIG_FILE

    try:
        if not os.path.exists( file_path ):
            raise FileExistsError( file_path, 'Path does not exists' )

        data: Dict = JsoncParser.parse_file( file_path )
        
        return Ok(data)

    except Exception as err:
        return Err(err)



@Spinner(text='Restoring default json file')
def __restore_default() -> Result[None, Exception]:

    if os.path.exists( CONFIG_FILE ):
       return CONFIG_FILE 
    else:
        try:
            shutil.copy2( src=CONFIG_FALLBACK, dst=CONFIG_FILE )
            return Ok(load_config())

        except Exception as err:
            return Err(error.panic(err))



@Spinner(text='Validating config file props and types')
def __validate_config( conf: Any ) -> Result[AppConf, Exception]:
    """ 
    *** At this momment it just a type checker! ***

    Tries to parse default.jsonc(json) to a valid `AppConfigDitc`.

    It iterates over, recursively, all json props matching with the `AppConf` structure

    Raises `TypeError` with a custom (default.json tree) message
    """

    keys_stack: str = 'CFG'

    try:
        error.raise_not_dict( conf )
        error.raise_not_typeddict( AppConf )
        validator.raise_missing_properties_keys( subject = conf, target = AppConf )
    
        for key in AppConf.__annotations__.keys():
            # we do not care form 'misc' dict, parse or validade anything into misc prop
            if key == 'misc': continue

            validator.match_typed_dict( 
                subject = conf[key], 
                target = AppConf.__annotations__[key], 
                keys_stack = keys_stack + f'.{key}' )
        
        validated: AppConf = conf
        return Ok(validated)

    except Exception as err:
        return Err(err)