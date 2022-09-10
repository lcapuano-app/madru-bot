import os

def create_dir( target_dir: str = None, raise_if_exists: bool = False ):

    if target_dir is None:
        raise ValueError('You must provide a target dir')

    if os.path.exists( target_dir ):
        if raise_if_exists:
            raise Exception(f'Target dir "{target_dir}" already exists')
        else:
            return None
    
    else:
        os.makedirs( target_dir )


def get_dir_dot_dot_path( target_dir: str = None, root_dir: str = None ) -> str:
    """ Raises Value error if target or root dirs are missing """
    if target_dir is None:
        raise ValueError('You must provide a target dir') 
    
    elif root_dir is None:
        raise ValueError('You must provide a root dir')

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

        return path