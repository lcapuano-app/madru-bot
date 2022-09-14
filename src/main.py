#!/usr/bin/python3

from app import App
from setup import config, logger


def fake_req():
    from quote.quote_gen import gen_quote_image
    quote_req = {
        "quote_id" : "63139372217ba7e20813b9b3",
        "author"   : "Chiquinha",
        "overlay"  : "chiquinha",
        "msg"      : "Minhas tias não me deixavam fazer nada, eu queria brincar de fogueirinha com os móveis novos da minha tia, não. Eu queria fazer uma tenda de campanha no jardim, com a cortina da sala, não. Eu queria laçar a televisão com uma corda, não. Acredita que não me deixaram fazer um dominó com as teclas do piano? E com o trabalho que eu tive pra tirar as teclas do piano…"
    }
    gen_quote_image( quote_req )

def main() -> None:
    fake_req()
    
    


if __name__ == '__main__':
    
    config.load_config()
    logger.load_logger()
    s1 = App()
    s2 = App()
    assert s1 is s2
    import pprint
    pprint.pprint( s1.config.quote.decor.bottom.color )
    #main()

    

    
    
