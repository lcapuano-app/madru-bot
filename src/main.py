#!/usr/bin/python3
from setup import setup_init
from domains.quote_img.img_gen import QuoteImageGen


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
    setup_init()
    fake_req()
    #print(qq)


if __name__ == '__main__':
    main()
    
