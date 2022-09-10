import sys

from pprint import pprint
from colorama import Fore, Style


class AppConfigValidatorError:

    @staticmethod
    def throw_error( err: ValueError, where: str = '' ) -> None:

        print(f'{Fore.RED}>> !! FATAL ERROR !!{Style.RESET_ALL}')
        print( f'{Fore.LIGHTYELLOW_EX}>> {where}{Style.RESET_ALL}' )
        print(f"{Fore.YELLOW}>> { err.args[0] }")
        pprint(err.args[1], indent=4)
        sys.exit()