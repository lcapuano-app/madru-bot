import os

from definitions import MAIN_DIR
from fn_result import Result, Ok,Err


def create_dir( target_dir: str = None, raise_if_exists: bool = False ) -> Result[None, ValueError | OSError]:

    if target_dir is None:
        return Err(ValueError('You must provide a target dir'))

    if os.path.exists( target_dir ):
        if raise_if_exists:
            return Err(OSError(f'Target dir "{target_dir}" already exists'))
        else:
            return Ok(None)
    
    else:
        os.makedirs( target_dir )
        return Ok(None)


def get_dir_dot_dot_path( target_dir: str = None, root_dir: str = MAIN_DIR ) -> Result[str, ValueError]:
    """ Raises Value error if target or root dirs are missing """
    if target_dir is None:
        return Err(ValueError('You must provide a target dir'))
    
    elif root_dir is None:
        return Err(ValueError('You must provide a root dir'))

    else:
        path = root_dir
        splited_path = target_dir.split( os.path.sep )
        up_levels = splited_path.count('..')

        counter = 0
        while up_levels > counter:
            path = os.path.dirname( path )
            up_levels = splited_path.count('..')
            counter += 1

        splited_path = list( filter( lambda splt: (splt != '..'), splited_path ) )
        path = os.path.join( path, *splited_path)

        return Ok(path)
