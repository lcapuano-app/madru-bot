from colorama import init as init_colorama

from setup.setup_dot_env import load_dot_env_crash
from setup.setup_core_config import get_core_config
from setup.setup_core_logger import set_core_logger

# Starts colorama. I'm a pretty pretty girl :)
init_colorama()


def init() -> None:
    """ 
    It may crash `(sys.exit)` in any steps of it.\n
        :(1) - loads dot env and test it
        :(2) - loads core config, validate then returns
        :(3) - use this config for seting up logging
    """
    load_dot_env_crash()
    cfg = get_core_config()
    set_core_logger( cfg )