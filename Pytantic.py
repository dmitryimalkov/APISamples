"""
Data validation and settings management using python type annotations
In FastAPI you have to validate data used in functions.
For this it is better to use pydantic
This is FootballDB API
1. Create classes and use pydantic for variables validation
2. Create list of endpoints by logical blocks: for coach; for player; for team; for LogIn;...

"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Player(BaseModel):
    num: int
    name = ""
    teams: List[str] = []

player1 = {
    "name": 'Akinfeev Igor',
    "num": 35,
    "teams": ["CSKA", "FK Rostov"]
}

player_object = Player(**player1)
print(player_object)

def print_player_info(player: Player):
    pass
#    print(name, team, position, age, number)

