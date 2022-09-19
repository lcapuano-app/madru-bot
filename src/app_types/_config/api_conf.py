from typing import TypedDict


class ApiAssetsConf( TypedDict ):
    url_get  : str
    url_post : str


class ApiHenrikConf( TypedDict ):
    rank : str


class ApiConf( TypedDict ):
    assets      : ApiAssetsConf
    henrik      : ApiHenrikConf
    user_agents : list

