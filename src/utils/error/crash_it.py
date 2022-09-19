import sys

from typing import Any as __Any, is_typeddict as __is_typeddict
from colorama import Fore as __Fore, Style as __Style


def panic( err: __Any, where: str = None ):

    print(f'{__Fore.RED}>> !! FATAL ERROR !!')
    print(f"{__Fore.YELLOW}>> { err }{__Style.RESET_ALL}")

    if where is not None:
        print(f'{__Fore.LIGHTYELLOW_EX}{where}{__Style.RESET_ALL}')
    
    sys.exit()


def raise_not_dict( _dict, / ) -> None:
    if not isinstance( _dict, dict ):
        raise TypeError( pretty_error(str(type(_dict)), f" Is not instance of <class 'dict'>" ))


def raise_not_typeddict( _cls, / ) -> None:
    if not __is_typeddict( _cls ):
        raise TypeError( pretty_error(str(type(_cls)), f" Is not instance of <class 'TypedDict'>" ))


def pretty_error( light: str, low: str, console_log: bool = False ) -> str:

    if console_log:
        print(f'{__Fore.RED}>>>>>> !!! CONFIG PARSER ERROR !!! <<<<<<{__Style.RESET_ALL}')
        
    light: str = f'{__Fore.LIGHTRED_EX}>> {light}'
    low: str = __Fore.RED + low + __Style.RESET_ALL
    return f'{light}{low}'