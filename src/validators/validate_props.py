import logging
import sys

from typing import Any
from colorama import Fore, Style


class ValidateProps:

    def is_instance_of( subject: object, target_obj: object = None, target_keys: list[str] = []  ) -> bool:

        if not isinstance( subject, object ):
            return False

        else:
            subject_keys: list[str] = list(map( lambda key: key, subject ))

            if target_obj is not None and isinstance( target_obj, object ):
                target_keys = list(map( lambda key: key, target_obj ))

            if len(target_keys) == 0 or len(subject_keys) == 0:
                return False

            else:

                res_keys = list(filter( lambda target_key: (target_key in subject_keys), target_keys ))

                if len(res_keys) != len(target_keys):
                    return False

                else:
                    return True


    def exit_on_error( prop: str, obj: object, expected_type: Any, where: str = '' ) -> None:
        self = ValidateProps

        if prop not in obj:
            self.print_and_exit( prop=prop, where=where )

        if isinstance( obj[prop], expected_type ) == False:
            self.print_and_exit( prop=prop, val=obj[prop], missing=False,  should_be=expected_type, where=where)


    def print_and_exit( prop: str, val: Any = '', missing: bool = True, should_be: str = '', where: str = '' ) -> None:

        missing_msg = f'Missing "{prop}" property => {where}'
        invalid_msg = f'Invalid "{prop}" value. => {where}.'

        msg = missing_msg if missing else invalid_msg

        print(f'{Fore.RED}>> !! FATAL ERROR !!')
        print(f"{Fore.YELLOW}>> { msg }{Style.RESET_ALL}")

        if missing is False:
            print(f'{Fore.GREEN}>> Expected => {should_be}.' )
            print(f'{Style.RESET_ALL}>> Found => {val}')

        logging.critical( msg )

        sys.exit()
