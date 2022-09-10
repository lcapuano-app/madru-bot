import logging
import os
import datetime

from definitions import ROOT_DIR


class AppLogger:


    @staticmethod
    def load_config( log_level: int = 0, filename: str = 'madru-bot-log', out_dir: str = '' ) -> None:
        self = AppLogger

        level = logging.DEBUG
        full_path = self.__get_file_full_path( filename = filename, out_dir = out_dir )

        """ Log level shoud be already validated, but logging accepts only integers
            between 0 and 50 ( 0..=5) * 10
            I am just making sure that will be a valid value
            reffer to app_config/ConfigLogLevel for details.

            solving for log_level(l) = 22
                (l)22 % 10  =   2
                   2  - 10  =  -8
                   -8 - 10  = -18
                   abs(-18) =  18
                18 + (l)22  =  30

            level = 30 (logging.WARNING)
        """
        if log_level > 50:
            level = 50 # logging.CRITICAL
        else:
            log_level = int(log_level) #makes sure it is an int
            level = abs(log_level % 10 - 10) + log_level

        if log_level <= 100 and (log_level % 10) == 0:
            level = log_level

        logging.basicConfig(
            filename = full_path,
            level = level,
            format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filemode = 'a+'
        )

    @staticmethod
    def __get_file_full_path( filename: str = 'madru-bot-log', out_dir: str = '' ) -> str:
        self = AppLogger
        dir_path = self.__get_dir_path( out_dir = out_dir )
        date_filename = self.__get_file_name( filename = filename )
        file_path = os.path.join( dir_path, date_filename )

        self.__create_dir( dir_path = dir_path )

        return file_path


    @staticmethod
    def __get_file_name( filename: str = 'madru-bot-log' ) -> str:

        timestamp = str( datetime.datetime.now() )
        date_str = timestamp[0:10]
        filename = f"{date_str}-{filename }.log"

        return filename


    @staticmethod
    def __create_dir( dir_path: str = None ) -> None:

        if dir_path is None: return

        if os.path.exists( dir_path ):
            return

        os.makedirs( dir_path )


    @staticmethod
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
