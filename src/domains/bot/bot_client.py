from typing import Any
from discord import Client, Intents

from app import App
from app_types.config import DiscordConf


class BotClient ( Client ):

    __disc_conf: DiscordConf = {}

    def __init__(self, **options: Any) -> None:
        
        intents: Intents = Intents.default()

        super().__init__(intents=intents, **options)

        self.__disc_conf = App.conf()['discord']
        self.__token = self.__disc_conf['token']
        self.__guild = self.__disc_conf['guild']
        print('TOKEN', self.__token)

    
    def run(self) -> None:
        return super().run( "MTAxMjA4OTM3MzQ1OTc1MTA0Nw.GE0GwF.lnJnAbhEXv8oN7L4_lk5bVf2QBkF7rnlDzp5z8", reconnect=True )
    # def run(self, *args: Any, **kwargs: Any) -> None:
    #     super().run(self.__token)