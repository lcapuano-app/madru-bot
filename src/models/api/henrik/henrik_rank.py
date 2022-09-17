from typing import TypedDict

from models.api.henrik.henrik_images import HenrikImagesDict


class HenrikRankDict ( TypedDict ):
    
    currenttier             : int
    currenttierpatched      : str
    images                  : HenrikImagesDict
    ranking_in_tier         : int
    mmr_change_to_last_game : int
    elo                     : int
    name                    : str
    tag                     : str
    old                     : bool