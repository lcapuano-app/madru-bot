import sys

from typing import Any
from colorama import Fore, Style


def panic( err: Any, where: str = None ):

    print(f'{Fore.RED}>> !! FATAL ERROR !!')
    print(f"{Fore.YELLOW}>> { err }{Style.RESET_ALL}")

    if where is not None:
        print(f'{Fore.LIGHTYELLOW_EX}{where}{Style.RESET_ALL}')
    
    sys.exit()