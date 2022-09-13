import logging
from typing import Any


def try_parse_int( arg: Any ) -> int:
    try: 
        return int( arg )
    except ValueError as err: 
        logging.debug( err )
        return 0