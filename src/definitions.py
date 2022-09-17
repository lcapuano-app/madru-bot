import os.path
from unittest.mock import DEFAULT

# Main dir
MAIN_DIR = os.path.dirname( os.path.abspath( __file__ ) )

# Project root
ROOT_DIR = os.path.dirname( MAIN_DIR )


# Config file.
CONFIG_DIR = os.path.join( ROOT_DIR, 'config' )
CONFIG_FILE_NAME = 'default.jsonc'
CONFIG_FILE = os.path.join( CONFIG_DIR, CONFIG_FILE_NAME )
CONFIG_FALLBACK = os.path.join( MAIN_DIR, 'fallback/config', CONFIG_FILE_NAME )


# Default quote Failover
__DEFAULT_QUOTE_FILE_NAME = 'quote.default.json'
DEFAULT_QUOTE_FILE = os.path.join( CONFIG_DIR, __DEFAULT_QUOTE_FILE_NAME )

DEFAULT_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'



# Colors
GOLD_RGB = 'rgb(209,201,5)'
WHITE_RBG = 'rgb(204,204,204)'
DARK_RGB = 'rgb(166,160,0)'
TRANSPARENT = 'rgba(0,0,0,0)'

#Quote
AUTHOR_IMG_ALPHA = 100
AUTHOR_RESIZE_LIMIT_RATIO = 1.2
AUTHOR_ROTATE_ANGLE = -10
IMG_EXT = '.png'
MARGIN_RATIO = 0.04
TEXT_COLOR_RGB = 'rgb(209,201,5)'
TEXT_MULTI_WRAP = 50
TEXT_STROKE = DARK_RGB
TEXT_RGB = WHITE_RBG
QUOTE_FONT_SIZE = 18
BOTTOM_FONT_SIZE = 22


