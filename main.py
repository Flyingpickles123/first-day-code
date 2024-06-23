
from typing import TypedDict


class Player(TypedDict):
    username: str
    name: str


type Players = dict[int, Player]


class Stats(TypedDict):
    farm: int
    kills: int
    deaths: int


class Game(TypedDict):
    players: list[int]
    stats: dict[int, Stats]


type Games = list[Game]


FARM = 10
KILL = 30
DEATH = -40


def player_gold_count(players: Players, games: Games) -> tuple[dict[int, int], str]:
    """
    Return a map of player IDs with their total gold count,
    and the username of the player with the highest gold.
    """
    highest = (0,0)
    golds={}

    for game in games:
        for id,stats in game["stats"].items():
            gold = stats["farm"] * FARM + stats["kills"] * KILL + stats["deaths"] * DEATH
            golds[id] = gold 
            if gold > highest [1]:
                highest = (id, gold)

    return golds, players[highest[0]]["username"]

def main():
    players: Players = {
        1234109: {"username": "FlyingPickles123", "name": "Felix"},
        1294867: {"username": "Zer0", "name": "Drew"},
        2109873: {"username": "Jinrhi", "name": "Richard"},
        7401704: {"username": "Magrex", "name": "Adam"},
    }

    games: Games = [
        {
            "players": [1234109, 1294867],
            "stats": {
                1234109: {"farm": 247, "kills": 17, "deaths": 10},
                1294867: {"farm": 189, "kills": 23, "deaths": 16},
            },
        },
        {
            "players": [2109873, 7401704],
            "stats": {
                2109873: {"farm": 25, "kills": 42, "deaths": 18},
                7401704: {"farm": 160, "kills": 31, "deaths": 27},
            },
        },
    ]
             

    result = player_gold_count(players, games)
    print(result)

main()