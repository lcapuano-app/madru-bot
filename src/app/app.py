from app_types.config import AppConf
from fn_result import Result, Ok,Err


class App:

    __conf: AppConf = None


    @staticmethod
    def conf() -> AppConf:
        return App.__conf


    @staticmethod
    def set_conf( conf: AppConf ) -> Result[None, Exception]:
        if App.__conf is None:
            App.__conf = conf