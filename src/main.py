#!/usr/bin/python3
import os

from colorama import init as init_colorama
from os.path import join, dirname
from dotenv import load_dotenv

from definitions import ROOT_DIR



""" Tries to access all props that we need No error handlres here!
    Let it crash!! We can continue without it """
def __init_dot_env() -> None:

    dotenv_path = join( ROOT_DIR, '.env' )
    load_dotenv( dotenv_path )
    os.environ['ENV']


if __name__ == '__main__':

    __init_dot_env()
    init_colorama()

