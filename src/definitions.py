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

# Default quote Failover
__DEFAULT_QUOTE_FILE_NAME = 'quote.default.json'
DEFAULT_QUOTE_FILE = os.path.join( CONFIG_DIR, __DEFAULT_QUOTE_FILE_NAME )
