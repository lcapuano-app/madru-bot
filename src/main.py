from time import sleep
import pyfiglet

from core.setup import config, logger
from domains.api import HenrikApi


def fake_req():
    from quote.quote_gen import gen_quote_image
    quote_req = {
        "quote_id" : "63139372217ba7e20813b9b3",
        "author"   : "Chiquinha",
        "overlay"  : "chiquinha",
        "msg"      : "Minhas tias não me deixavam fazer nada, eu queria brincar de fogueirinha com os móveis novos da minha tia, não. Eu queria fazer uma tenda de campanha no jardim, com a cortina da sala, não. Eu queria laçar a televisão com uma corda, não. Acredita que não me deixaram fazer um dominó com as teclas do piano? E com o trabalho que eu tive pra tirar as teclas do piano…"
    }
    gen_quote_image( quote_req )

def __welcome( msg: str = "MadruBot" ) -> None:
    print(pyfiglet.figlet_format( msg ))


def __setup() -> None:
    config.load_config()
    #logger.load_logger()

def __main() -> None:
    #fake_req()
    name: str='Q95 Madrudruga'
    tag: str='quake'
    player = (name, tag)
    HenrikApi().get_rank( player )
    


if __name__ == '__main__':

    __welcome()
    __setup()
    # __main()

    

    
    
    # from halo import Halo

    # spinner = Halo(text='Loading', spinner='dots')
    # spinner.start() 
    # sleep(5)
    # spinner.stop()
    # print('No Lugar')