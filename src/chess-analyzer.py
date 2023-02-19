from chessdotcom import get_player_profile, get_player_game_archives, get_player_games_by_month, get_player_stats,get_player_tournaments
from datetime import datetime
import pprint

printer = pprint.PrettyPrinter()

def timestamp_to_date(timestamp):
    """
    Convert a timestamp to a date:
    ex: timestamp_to_date(1606413589) => '26-11-2020'
    """
    return datetime.fromtimestamp(timestamp).strftime('%d-%m-%y%y')


def profile_info(player):
    """
    turn a table with the profile information of the player name in entry
    ---
    [name, country, league, status, creation_date, followers, link] 
    """
    request = get_player_profile("BaguettedeFromage").json["player"]
    P = [request['name'],request['country'][34:],request['league'],request["status"],timestamp_to_date(request['joined']),request["followers"],request["url"]] 
    return P

def tournament_info(player):
    """
    Return a table with the tournaments information of the player name in entry
    ---
    [played_tournaments,winner, eliminated, withdrew, removed]
    """
    request = get_player_tournaments(player).json["tournaments"]["finished"]
    tournaments = [len(request),0 ,0 ,0,0] 
    eliminated = 0
    withdrew = 0
    removed = 0
    for tournament in request:
        if tournament["status"] == 'winner':
            tournaments[1] += 1
        elif tournament["status"] == 'eliminated':
            tournaments[2] += 1
        elif tournament["status"] == 'withdrew':
            tournaments[3] += 1
        elif tournament["status"] == 'removed':
            tournaments[4] += 1
    return tournaments

def player_rank(player):
    """
    Return 2 table with the ranks information of the player name in entry
    ---
    best = [chess_blitz, chess_bullet, chess_daily, chess_rapid, puzzle_rush, tactics]
    current = [chess_blitz, chess_bullet, chess_daily, chess_rapid, puzzle_rush, tactics]
    """
    pass

if __name__ == "__main__":
    #response = get_player_profile(input("Player name: "))
    response = get_player_profile("BaguettedeFromage").json["player"]
    #print(response)
    printer.pprint(response)
    #print(profile_info("BaguettedeFromage"))
    #print(tournament_info("BaguettedeFromage"))



"""
get_player_stats
---
{'stats': {'chess_blitz': {'best': {'date': 1672946853,
                                    'game': 'https://www.chess.com/game/live/65721220887',
                                    'rating': 865},
                           'last': {'date': 1676546595,
                                    'rating': 817,
                                    'rd': 74},
                           'record': {'draw': 7, 'loss': 51, 'win': 71}},
           'chess_bullet': {'best': {'date': 1616682328,
                                     'game': 'https://www.chess.com/game/live/10321713177',
                                     'rating': 742},
                            'last': {'date': 1676747490,
                                     'rating': 657,
                                     'rd': 87},
                            'record': {'draw': 0, 'loss': 36, 'win': 36}},
           'chess_daily': {'best': {'date': 1613499745,
                                    'game': 'https://www.chess.com/game/daily/312098816',
                                    'rating': 939},
                           'last': {'date': 1675118329,
                                    'rating': 593,
                                    'rd': 156},
                           'record': {'draw': 0,
                                      'loss': 35,
                                      'time_per_move': 10485,
                                      'timeout_percent': 0,
                                      'win': 9}},
           'chess_rapid': {'best': {'date': 1671985236,
                                    'game': 'https://www.chess.com/game/live/65703738939',
                                    'rating': 1072},
                           'last': {'date': 1676748572,
                                    'rating': 990,
                                    'rd': 51},
                           'record': {'draw': 19, 'loss': 159, 'win': 202}},
           'puzzle_rush': {'best': {'score': 15, 'total_attempts': 18}},
           'tactics': {'highest': {'date': 1676723429, 'rating': 1670},
                       'lowest': {'date': 1608311624, 'rating': 412}}}}
"""




"""
get_player_game_archives(name)
---
{'archives': ['https://api.chess.com/pub/player/baguettedefromage/games/2020/11',
              'https://api.chess.com/pub/player/baguettedefromage/games/2020/12',
              'https://api.chess.com/pub/player/baguettedefromage/games/2021/01',
              'https://api.chess.com/pub/player/baguettedefromage/games/2021/02',
              'https://api.chess.com/pub/player/baguettedefromage/games/2021/03',
              'https://api.chess.com/pub/player/baguettedefromage/games/2021/04',
              'https://api.chess.com/pub/player/baguettedefromage/games/2021/05',
              'https://api.chess.com/pub/player/baguettedefromage/games/2021/06',
              'https://api.chess.com/pub/player/baguettedefromage/games/2021/07',
              'https://api.chess.com/pub/player/baguettedefromage/games/2021/09',
              'https://api.chess.com/pub/player/baguettedefromage/games/2021/10',
              'https://api.chess.com/pub/player/baguettedefromage/games/2021/12',
              'https://api.chess.com/pub/player/baguettedefromage/games/2022/08',
              'https://api.chess.com/pub/player/baguettedefromage/games/2022/12',
              'https://api.chess.com/pub/player/baguettedefromage/games/2023/01',
              'https://api.chess.com/pub/player/baguettedefromage/games/2023/02']}
"""


"""
get_player_games_by_month(name,year,mounth)
---
"""
