import functools

from typing import Any
from halo import Halo
from colorama import Fore, Style

from fn_result import Err   


class Spinner:

    __limit = 100
    __symbol_pass =  '✅'
    __symbol_fail = '❌'

    def __init__(self, text: str = '' ) -> None:
        self.text = text


    def __call__(self, fn=None ):
  
        @functools.wraps(fn)
        def inner( *args, **kwargs ):

            stop_symbol: str = self.__symbol_pass
            spin_text = self.__norm_text( fn )
            spinner = Halo( text = spin_text )
            spinner.start()
            
            fn_result = fn(*args, **kwargs)

            if type(fn_result) == Err:
                stop_symbol = self.__symbol_fail

            #print('NEM VIM AQUI NEH?', type(fn_result), Err)
            spinner.stop_and_persist( stop_symbol )
            
            return fn_result
        
        return inner

    
    def __norm_text( self, fn ) -> str:

        fn_name: str = fn.__name__
        spin_txt_len: int = len(self.text)
        fn_name_len: int = len(fn_name)

        if fn_name_len == 0:
            return self.text

        elif spin_txt_len == 0:
            return f'[{fn_name}]'

        else:
            fn_name = f'[{fn_name}]'
            fn_name_len: int = len(fn_name)
            diff_len: int = abs( spin_txt_len + fn_name_len - self.__limit ) 
            spaces: str =  ' ' * diff_len
            
            if diff_len <= 0:
                return f'{self.text} {fn_name}'
            else:
                return f'{Fore.CYAN}{self.text}{spaces}{fn_name}{Style.RESET_ALL}'

