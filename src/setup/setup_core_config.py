from core.config import CoreConfig


def get_core_config() -> CoreConfig:
    """ 
    Just get the config loaded by `default.jsonc`. 
    I itmove to its own class :ref: `CoreConfig`.\n
    ::returs: `CoreConfig`
    """
    core_config = CoreConfig().get
    return core_config