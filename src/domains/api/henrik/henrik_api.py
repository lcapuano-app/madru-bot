import logging
import urllib.parse

from typing import TYPE_CHECKING, Tuple

from core import App
from utils.http import make_get, get_random_user_agent
from models.api.henrik import HenrikRespDict, HenrikRankDict


class HenrikApi:

    
    def get_rank( self, player: Tuple[str, str] ) -> HenrikRankDict:
        
        conf = App().config
        name, tag = player
        name = urllib.parse.quote(name)
        
        url: str = conf.api.henrik.rank.format( name=name, tag=tag )
        user_agent = get_random_user_agent( conf )
        headers = { 'User-Agent': user_agent }

        """ try:
            res: HenrikRespDict = make_get( url, headers )
            return res['data']
            
        except Exception as err:
            logging.error( err, exc_info=True )
            return None """