from os import environ
from os.path import join
from dotenv import load_dotenv

from definitions import ROOT_DIR


def load_dot_env_crash() -> None:
    """ 
        Tries to access all props that we need No error handlres here!
        Let it crash!! We can continue without it 
    """
    dotenv_path = join( ROOT_DIR, '.env' )
    load_dotenv( dotenv_path )
    environ['ENV']