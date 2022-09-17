import random
from typing import List

from definitions import DEFAULT_USER_AGENT

from models.config import AppConfig


def get_random_user_agent( conf: AppConfig ) -> str:

    user_agents: List[str] = conf.api.user_agents


    if not user_agents:
        return DEFAULT_USER_AGENT

    else:
        return random.choice(user_agents)