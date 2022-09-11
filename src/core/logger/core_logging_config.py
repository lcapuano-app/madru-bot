import logging


class CoreLoggingConfig:


    @staticmethod
    def set_base_config( filename: str, level: int ):

        logging.basicConfig(
            filename = filename,
            level = level,
            format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filemode = 'a+'
        )