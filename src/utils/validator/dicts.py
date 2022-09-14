import inspect
import logging

from typing import Any, TypedDict


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
