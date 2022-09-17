import logging
from urllib.error import HTTPError
import requests

from typing import Any, Dict


def make_get( url: str, headers: Dict[str, Any] = None, body: Any = None ):
    
        resp = requests.get( url, headers = headers )
        resp.raise_for_status()

        if resp.status_code != 200:
            raise HTTPError( url=url, code=resp.status_code )

        json_data = resp.json()

        logging.debug( f'request.get {url} {resp.status_code}')
        return json_data

   