import inspect
import logging

from colorama import Fore, Style
from typing import TypedDict, is_typeddict

_TYPED_DICT_TYPE = "<class 'typing._TypedDictMeta'>"


def is_instance_raise( _obj: dict, _typed_dict: TypedDict ) -> None:

    def __pretty_error( light: str, low: str ) -> str:
        light = Fore.LIGHTYELLOW_EX + light
        low = Fore.YELLOW + low + Style.RESET_ALL
        return light + low

    if not isinstance( _obj, dict ) or not isinstance( _obj, object ):
        raise TypeError( __pretty_error( _obj, 'Argument is not a Dict or Object' ) )
    
    elif not hasattr( _typed_dict, '__annotations__'):
        raise TypeError( __pretty_error( _typed_dict, 'Argument is not a TypedDict' ) )

    else:
       
        for key in _obj:
            if key not in _typed_dict.__annotations__:
                raise TypeError( __pretty_error( key, f' Is not in {_typed_dict}') )
            
            obj_type = type(_obj[key])
            typed_dict_key = _typed_dict.__annotations__[key]
            if obj_type != typed_dict_key:
                raise TypeError( __pretty_error(f'{key} {obj_type}', f' Is not instancedsadsadsasd of {typed_dict_key}' ))

            q = _typed_dict.__annotations__[key]
            print('\n',_obj[key], type( _obj[key]))
            print('\n', key,q, q == type( _obj[key]))
            #if is_typeddict
            obj_type = type(_obj[key])

            #print( is_typeddict( _typed_dict[key] ),  _typed_dict[key])
            
            # if isinstance( obj_type, dict):
            #     obj_type = _TYPED_DICT_TYPE

            

            tt=str(type(_typed_dict.__annotations__[key]))
            aa=str(type(_obj[key]))
            import pprint
            #pprint.pprint( _typed_dict[key].__annotations__)
            #print( isinstance( _obj[key], dict), _TYPED_DICT_TYPE == tt)
        

def is_instance( _obj: dict, _typed_dict: TypedDict ):

    if not isinstance( _obj, dict ) or not isinstance( _obj, object ):
        logging.error( msg='Argument is not a Dict or Object', stack_info = inspect.stack()[1] )
        return False
    elif not hasattr( _typed_dict, '__annotations__'):
        logging.error( msg='Argument is not a TypedDict', stack_info = inspect.stack()[1] )
        return False
    else:
        print('PASSOyu')
        return True
