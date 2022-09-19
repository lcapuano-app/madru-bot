from app_types.config import AppConf
from fn_result import Result, Ok,Err


class App:

    __conf: AppConf = None


    @staticmethod
    def conf( set_conf: AppConf = None ) -> AppConf:

        if set_conf is None:
            return App.__conf

        elif App.__conf is None:
            App.__conf = set_conf

        else:
            return  App.__conf
