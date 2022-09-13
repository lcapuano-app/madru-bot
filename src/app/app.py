from app_types.config import ConfigType


class _App:

    _instance = None
    _config: ConfigType = None
    
    @property
    def config(self) -> ConfigType:
        return self._config
        
    @config.setter
    def config( self, config: ConfigType ) -> None:
        self._config = config


def App():
    if _App._instance is None:
        _App._instance = _App()
    return _App._instance