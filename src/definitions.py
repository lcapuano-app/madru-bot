import os.path

# Main dir
MAIN_DIR = os.path.dirname( os.path.abspath( __file__ ) )

# Project root
ROOT_DIR = os.path.dirname( MAIN_DIR )


# Config file dir. We'll select default/prod/test in src/config handler
CONFIG_DIR = os.path.join( ROOT_DIR, 'config' )

# Config file for development
__DEV_FILE_NAME = 'default.jsonc'
CONFIG_DEV = os.path.join( CONFIG_DIR, __DEV_FILE_NAME )

# Config file for production
__PROD_FILE_NAME = 'production.jsonc'
CONFIG_PROD = os.path.join( CONFIG_DIR, __PROD_FILE_NAME )

# Config files failover
CONFIG_FAILOVER_DEV = os.path.join( MAIN_DIR, 'failover', 'failover_' + __DEV_FILE_NAME )
CONFIG_FAILOVER_PROD = os.path.join( MAIN_DIR, 'failover', 'failover_' + __PROD_FILE_NAME )

# Default quote Failover
__DEFAULT_QUOTE_FILE_NAME = 'quote.default.json'
DEFAULT_QUOTE_FILE = os.path.join( CONFIG_DIR, __DEFAULT_QUOTE_FILE_NAME )




# Colors
GOLD_RGB = 'rgb(209,201,5)'
WHITE_RBG = 'rgb(204,204,204)'
DARK_RGB = 'rgb(166,160,0)'

#Quote
IMG_EXT = '.png'
TEXT_COLOR_RGB = 'rgb(209,201,5)'
TEXT_MULTI_WRAP = 50
TEXT_STROKE = DARK_RGB
TEXT_RGB = WHITE_RBG
