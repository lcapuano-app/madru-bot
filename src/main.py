import pyfiglet

from app_config import config, logger



def fake_req():
    from quote.quote_gen import gen_quote_image
    quote_req = {
        "quote_id" : "63139372217ba7e20813b9b3",
        "author"   : "Chiquinha",
        "overlay"  : "chiquinha",
        "msg"      : "Minhas tias não me deixavam fazer nada, eu queria brincar de fogueirinha com os móveis novos da minha tia, não. Eu queria fazer uma tenda de campanha no jardim, com a cortina da sala, não. Eu queria laçar a televisão com uma corda, não. Acredita que não me deixaram fazer um dominó com as teclas do piano? E com o trabalho que eu tive pra tirar as teclas do piano…"
    }
    gen_quote_image( quote_req )


def __set_config() -> None:
    config.load_config()
    print('  ','-'*100)


def __set_logger() -> None:
    logger.load_logger()
    print('  ','-'*100)


def main() -> None:
    print(pyfiglet.figlet_format( "MadruBot" ))
    __set_config()
    __set_logger()
    
    
    


if __name__ == '__main__':
    main()
    from domains.bot.bot_client import BotClient
    cc = BotClient()
    cc.run()