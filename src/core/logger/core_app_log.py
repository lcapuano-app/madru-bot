import logging
import os.path

from definitions import ROOT_DIR
from core.logger.core_assert_log_level import CoreAssertLogLevel
from utils.files import create_dir, get_dir_dot_dot_path, get_timestamp_filename


class CoreAppLog:

    __is_set: bool = False

    @staticmethod
    def set_logging( level: int = 0, filename: str = 'log', output_dir: str = '' ) -> None:
        self = CoreAppLog

        if self.__is_set:
            return
        
        else:
            self.__setup( level, filename, output_dir )
            return


    def __setup( level: int = 0, filename: str = 'log', output_dir: str = '' ) -> None:
        self = CoreAppLog
        

        level = CoreAssertLogLevel( level ).get_asserted()
        output_dir = self.__create_output_dir( output_dir=output_dir )
        filename = get_timestamp_filename( filename=filename, ext='log' )
        filename = os.path.join( output_dir, filename )
       
        logging.basicConfig(
            filename = filename,
            level = level,
            format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filemode = 'a+'
        )

        self.__is_set = True


    def __create_output_dir( output_dir: str ) -> str:
        output_path: str = get_dir_dot_dot_path( target_dir=output_dir, root_dir=ROOT_DIR )
        create_dir( target_dir=output_path )
        return output_path