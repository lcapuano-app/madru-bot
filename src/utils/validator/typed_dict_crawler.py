from enum import Enum
from typing import TYPE_CHECKING, Any, List, TypedDict, is_typeddict
from colorama import Fore, Style

from utils import error
from models.config.log import LogLevel


def match_typed_dict( *, subject: dict, target: TypedDict, keys_stack: str ) -> None:

    error.raise_not_dict( subject )
    error.raise_not_typeddict( target )
    raise_missing_properties_keys( subject = subject, target = target, keys_stack = keys_stack )
    
    for key in target.__annotations__.keys():
        if is_typeddict(target.__annotations__[key] ):
            match_typed_dict( 
                subject = subject[key], target = target.__annotations__[key], keys_stack = keys_stack + f'.{key}' )
        else:
            match_property_type( 
                value = subject[key], target_annt = target.__annotations__, target_key = key, keys_stack = keys_stack + f'.{key}' )


def match_property_type( *, value: Any, target_annt: dict[str, Any], target_key: str, keys_stack: str ) -> None:

    value_type = type( value )

    is_enum: bool = target_annt[target_key].__class__ is type(Enum)
    if is_enum:
        if target_annt[target_key].__name__ == LogLevel.__name__ and value_type != LogLevel.__type__:
            raise TypeError( error.pretty_error(
                f"In: '{keys_stack}' found: {value_type} ({value}) | ",
                f"Expecting {target_annt[target_key]} [0 | 10 | 20 | 30 | 40 | 50]" ) )


    elif target_annt[target_key] != type( value ):
        raise TypeError( error.pretty_error(
            f"In: '{keys_stack}' found: {value_type} ({value}) | ", f"Expecting {target_annt[target_key]}" ) )
                  

def raise_missing_properties_keys( *, subject: dict, target: TypedDict, keys_stack: str = None ) -> None:
   
    error.raise_not_dict( subject )
    error.raise_not_typeddict( target )

    target_dict = target.__annotations__
    subject_keys: List[str] = list( map( lambda key: key, subject ) )
    target_keys: List[str] = list( map( lambda key: key, target_dict ) )
    diff_keys: List[str] = list( filter( lambda key: (key not in subject_keys), target_keys ) )
   
    if len(diff_keys) > 0:
        raise TypeError( error.pretty_error(
            f" Missing properties in '{keys_stack}' to match <{target.__name__}>:", str(diff_keys) ))
    
