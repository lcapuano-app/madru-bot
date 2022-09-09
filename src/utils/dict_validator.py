import logging
import sys

from typing import Any
from colorama import Fore, Style


class DictValidator:


    @staticmethod
    def exit_on_error( self, prop: str, obj: object, expected_type: Any, where: str = '' ) -> None:

        if prop not in obj:
            self.print_and_exit( prop=prop, where=where )

        if isinstance( obj[prop], expected_type ) == False:
            self.print_and_exit( prop=prop, val=obj[prop], missing=False,  should_be=expected_type, where=where)


    @staticmethod
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


    @staticmethod
    def is_instance_of( subject: object | dict, target_pattern: list[dict[str, Any]] = [] ) -> bool:

        self = DictValidator

        if not self.__valid_subject( subject ):
            return False

        else:
            is_instance, errors = self.__subject_typing_has_errors( subject, target_pattern )

            return False if errors else is_instance


    @staticmethod
    def is_instance_of_err(
        subject: object | dict,
        target_pattern: list[dict[str, Any]] = [],
        raise_err: bool = False
    ) -> tuple[bool, list]:

        self = DictValidator

        if not self.__valid_subject( subject ):
            if raise_err: raise ValueError('No subject to check')
            else: return (False,['No subject to check'])

        else:
            is_instance, errors = self.__subject_typing_has_errors( subject, target_pattern )

            if raise_err and errors:
                raise ValueError( 'Not instance of', errors )
            else:
                return (is_instance, errors)


    def __subject_typing_has_errors( subject: object | dict, target_pattern: list[dict[str, Any]] ) -> tuple[bool, list]:

        errors = []

        for target in target_pattern:

            # Prop does not exists
            if target['key'] not in subject:
                errors.append({
                    "detail": f"Missing key '{target['key']}' from subject",
                    "found": subject.keys(),
                    "expected": { "key": target['key'], "typing": target['typing'] },
                })
            # Exisist but types does not match
            elif (target['key'] in subject) and ( type(subject[target['key']]) != target['typing'] ):
                errors.append({
                    "detail": f"Invalid typing ({type(subject[target['key']])}) for '{target['key']}'",
                    "found": { "key": subject[target['key']], "typing": type(subject[target['key']]) },
                    "expected": { "key": target['key'], "typing": target['typing'] },
                })


        result: tuple[bool, list] = ( len( errors ) > 0, errors ) if errors else ( True, [] )

        return result


    def __valid_subject( subject: object | dict ) -> bool:

        if isinstance( subject, object ) or isinstance( subject, dict ):
            return True
        else:
            return False
