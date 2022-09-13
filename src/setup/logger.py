import logging
import os

from app import App
from utils.math import try_parse_int
from utils.files import create_dir, get_dir_dot_dot_path, get_timestamp_filename
from definitions import MAIN_DIR


def load_logger() -> None:

    log_cfg = App().config['log']
    level = __get_assert_level( level = log_cfg['level'] )
    output_dir = __create_output_dir( output_dir = log_cfg['out_dir'] )
    filename = get_timestamp_filename( filename = log_cfg['filename'] )
    file_path = os.path.join( output_dir, filename )

    logging.basicConfig(
        filename = file_path,
        level = level,
        format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filemode = 'a+'
    )


def __get_assert_level( level: int = 0 ) -> int:

    level = try_parse_int( level )

    if level == 0:
        return logging.NOTSET

    elif level >= 50:
        return logging.CRITICAL

    elif level % 10  == 0:
        return level # level is equal to 10|20|30|40 (logging consts )

    else:
        mod = 10
        level = abs(level % mod - mod) + level # closest value to logging consts (round up, 22 => 30)
        return level


def __create_output_dir( output_dir: str ) -> str:

    output_path: str = get_dir_dot_dot_path( target_dir = output_dir, root_dir = MAIN_DIR )
    create_dir( target_dir=output_path )
    return output_path