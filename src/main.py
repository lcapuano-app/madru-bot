#!/usr/bin/python3
import os
from typing import Tuple

from colorama import init as init_colorama
from os.path import join, dirname
from dotenv import load_dotenv

from logger_init import LoggerInit
from definitions import ROOT_DIR

from config import Cfg

from domains.quote_image import QuoteImage


""" Tries to access all props that we need No error handlres here!
    Let it crash!! We can continue without it """
def __init_dot_env() -> None:

    dotenv_path = join( ROOT_DIR, '.env' )
    load_dotenv( dotenv_path )
    os.environ['ENV']

def __get_logger_config() -> Tuple[str, str, str]:

    cfg = Cfg.get_log_cfg()

    out_dir   = cfg['out_dir']
    log_level = cfg['level']
    filename  = cfg['filename']

    return ( out_dir, log_level, filename )

if __name__ == '__main__':

    __init_dot_env()
    init_colorama()
    out_dir, log_level, filename = __get_logger_config()
    LoggerInit.load_config( log_level = log_level, out_dir = out_dir )

    QuoteImage().get()

