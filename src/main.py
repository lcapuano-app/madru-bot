#!/usr/bin/python3
import os

from colorama import init as init_colorama
from os.path import join, dirname
from dotenv import load_dotenv

from definitions import ROOT_DIR
from app_config import AppConfig
from app_logger import AppLogger
from quote_img_gen.img_gen import QuoteImageGen


""" Tries to access all props that we need No error handlres here!
    Let it crash!! We can continue without it """
def __init_dot_env() -> None:

    dotenv_path = join( ROOT_DIR, '.env' )
    load_dotenv( dotenv_path )
    os.environ['ENV']

def __get_app_config() -> AppConfig:
    app_config = AppConfig()
    print(app_config.config)

def __set_app_logger( app_config: AppConfig ):
    app_config.cfg_log
    AppLogger.load_config(
        log_level = app_config.cfg_log['level'],
        filename = app_config.cfg_log['filename'],
        out_dir = app_config.cfg_log['out_dir']
    )

def fake_req():
    quote_req = {
        "quote_id" : "63139372217ba7e20813b9b3",
        "author"   : "Chiquinha",
        "overlay"  : "chiquinha",
        "msg"      : "Minhas tias não me deixavam fazer nada, eu queria brincar de fogueirinha com os móveis novos da minha tia, não. Eu queria fazer uma tenda de campanha no jardim, com a cortina da sala, não. Eu queria laçar a televisão com uma corda, não. Acredita que não me deixaram fazer um dominó com as teclas do piano? E com o trabalho que eu tive pra tirar as teclas do piano…"
    }

    img_gen = QuoteImageGen( quote_req )
    img = img_gen.gen()
    #img.show()

def main() -> None:
    __init_dot_env()
    init_colorama()
    app_config = AppConfig()
    __set_app_logger( app_config )
    fake_req()
    #print(qq)


if __name__ == '__main__':
    main()
