from app_types.config import AppConf
from fn_result import Result, Ok,Err


class App:

    __conf: AppConf = None


    @staticmethod
    def conf() -> Result[AppConf, Exception]:

        if App.__conf is not None:
            return Ok( App.__conf )
        else:
            return Err(AttributeError('conf has not been assigned'))


    @staticmethod
    def set_conf( conf: AppConf ) -> Result[None, Exception]:

        if App.__conf is None:
            App.__conf = conf
            return Ok(None)
        else:
            return Err(AttributeError('conf has already been assigned'))