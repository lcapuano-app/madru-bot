import logging
import os
import datetime

from models import ConfigLogLevel
from definitions import ROOT_DIR


class LoggerInit():

    def load_config( log_level: int = 0, filename: str = 'madru-bot-log', out_dir: str = '' ) -> None:
        self = LoggerInit

        level = logging.NOTSET
        full_path = self.__get_file_full_path( filename = filename, out_dir = out_dir )

        if ConfigLogLevel.has_value( log_level ):
            level = log_level

        logging.basicConfig(
            filename = full_path,
            level = level,
            format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filemode = 'a+'
        )

    def __get_file_full_path( filename: str = 'madru-bot-log', out_dir: str = '' ) -> str:
        self = LoggerInit

        dir_path = self.__get_dir_path( out_dir = out_dir )
        date_filename = self.__get_file_name( filename = filename )
        file_path = os.path.join( dir_path, date_filename )

        self.__create_dir( dir_path = dir_path )

        return file_path

    def __get_file_name( filename: str = 'madru-bot-log' ) -> str:

        timestamp = str( datetime.datetime.now() )
        date_str = timestamp[0:10]
        filename = f"{date_str}-{filename }.log"

        return filename

    def __create_dir(  dir_path: str = None ) -> None:

        if dir_path is None: return

        if os.path.exists( dir_path ):
            return

        os.makedirs( dir_path )


    def __get_dir_path( out_dir: str = None ) -> str:

        if out_dir is None: return

        path = ROOT_DIR
        splited_path = out_dir.split( os.path.sep )
        up_levels = splited_path.count('..')

        counter = 0
        while up_levels > counter:
            path = os.path.dirname( path )
            up_levels = splited_path.count('..')
            counter += 1

        splited_path = list( filter( lambda splt: (splt != '..'), splited_path ) )
        path = os.path.join( path, *splited_path)

        return path
