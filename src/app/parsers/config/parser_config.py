## cfg .json ou .jsonC
## Checar contra AppCOnfigDict KEY valuee type

from enum import Enum
from typing import Any, List, TypedDict, is_typeddict
from colorama import Fore, Style

from app.models.config import AppConfigDict, LogLevel


def parse_to_app( conf: dict ) -> None:
    """ 
    *** At this momment it just a type checker! ***

    Tries to parse default.jsonc(json) to a valid `AppConfigDitc`.

    It iterates over, recursively, all json props matching with the `AppConfigDict` structure

    Raises `TypeError` with a custom (default.json tree) message
    """

    keys_stack: str = 'CFG'

    __raise_not_dict( conf )
    __raise_not_typeddict( AppConfigDict )
    __raise_missing_properties_keys( subject = conf, target = AppConfigDict )
    
    for key in AppConfigDict.__annotations__.keys():
        
        # we do not care, parse or validade anything into misc prop
        if key == 'misc': continue
        __match_typed_dict( 
            subject = conf[key], target = AppConfigDict.__annotations__[key], keys_stack = keys_stack + f'.{key}' )
         

def __match_typed_dict( *, subject: dict, target: TypedDict, keys_stack: str ) -> None:

    __raise_not_dict( subject )
    __raise_not_typeddict( target )
    __raise_missing_properties_keys( subject = subject, target = target, keys_stack = keys_stack )
    
    for key in target.__annotations__.keys():
        if is_typeddict(target.__annotations__[key] ):
            __match_typed_dict( 
                subject = subject[key], target = target.__annotations__[key], keys_stack = keys_stack + f'.{key}' )
        else:
            __match_property_type( 
                value = subject[key], target_annt = target.__annotations__, target_key = key, keys_stack = keys_stack + f'.{key}' )


def __match_property_type( *, value: Any, target_annt: dict[str, Any], target_key: str, keys_stack: str ) -> None:

    value_type = type( value )

    is_enum: bool = target_annt[target_key].__class__ is type(Enum)
    if is_enum:
        if target_annt[target_key].__name__ == LogLevel.__name__ and value_type != LogLevel.__type__:
            raise TypeError( __pretty_error(
                f"In: '{keys_stack}' found: {value_type} ({value}) | ",
                f"Expecting {target_annt[target_key]} [0 | 10 | 20 | 30 | 40 | 50]" ) )


    elif target_annt[target_key] != type( value ):
        raise TypeError( __pretty_error(
            f"In: '{keys_stack}' found: {value_type} ({value}) | ", f"Expecting {target_annt[target_key]}" ) )
                  

def __raise_missing_properties_keys( *, subject: dict, target: TypedDict, keys_stack: str = None ) -> None:
   
    __raise_not_dict( subject )
    __raise_not_typeddict( target )

    target_dict = target.__annotations__
    subject_keys: List[str] = list( map( lambda key: key, subject ) )
    target_keys: List[str] = list( map( lambda key: key, target_dict ) )
    diff_keys: List[str] = list( filter( lambda key: (key not in subject_keys), target_keys ) )
   
    if len(diff_keys) > 0:
        raise TypeError( __pretty_error(
            f" Missing properties in '{keys_stack}' to match <{target.__name__}>:", str(diff_keys) ))
    

def __raise_not_dict( _dict, / ) -> None:
    if not isinstance( _dict, dict ):
        raise TypeError( __pretty_error(str(type(_dict)), f" Is not instance of <class 'dict'>" ))


def __raise_not_typeddict( _cls, / ) -> None:
    if not is_typeddict( _cls ):
        raise TypeError( __pretty_error(str(type(_cls)), f" Is not instance of <class 'TypedDict'>" ))


def __pretty_error( light: str, low: str ) -> str:
    print(f'{Fore.RED}>>>>>> !!! CONFIG PARSER ERROR !!! <<<<<<{Style.RESET_ALL}')
    light: str = f'{Fore.LIGHTRED_EX}>> {light}'
    low: str = Fore.RED + low + Style.RESET_ALL
    return f'{light}{low}'