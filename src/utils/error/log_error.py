from functools import partial, wraps
import functools
import logging
from typing import Any

""" def exception_handler( on_error: Any = None ):
    tt = logging.getLevelName( level )
    print('=================== TO POR AQUI?', tt)
    def wrapper( fn ):

        @functools.wraps( fn )
        def inner( *args, **kwargs ):
            try:
                fn(*args, **kwargs)
            except Exception as err:
                print(err)
                return err
        return inner

    return wrapper """


""" def exception_handler( on_error: Any = None ):
    tt = logging.getLevelName( level )
    print('=================== TO POR AQUI?', tt)
    def wrapper( fn ):

        @functools.wraps( fn )
        def inner( *args, **kwargs ):
            try:
                fn(*args, **kwargs)
            except Exception as err:
                print(err)
                return err
        return inner

    return wrapper """
def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as err:
            print(err)
    return inner_function
""" def exception_handler(func, level):
    print('=================== TO POR AQUI?', level)
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as err:
            print(err)
    return inner_function
 """
