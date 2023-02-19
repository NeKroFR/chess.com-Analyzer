from chessdotcom import get_player_profile, get_player_game_archives, get_player_games_by_month, get_player_stats,get_player_tournaments
from datetime import datetime

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
    Return 3 lists with the ranks information of the player name in entry
    ---
    best = [chess_blitz, chess_bullet, chess_daily, chess_rapid]
    current = [chess_blitz, chess_bullet, chess_rapid, chess_daily]
    ratio = [chess_blitz, chess_bullet, chess_rapid, chess_daily]
    """
    request = get_player_stats(player).json["stats"]
    best = []
    current = []
    ratio = []
    # blitz
    blitz = request["chess_blitz"]
    best.append(blitz["best"]["rating"])
    current.append(blitz["last"]["rating"])
    ratio.append(round(blitz["record"]["win"]/blitz["record"]["loss"],2))
    #bullet
    bullet = request["chess_bullet"]
    best.append(bullet["best"]["rating"])
    current.append(bullet["last"]["rating"])
    ratio.append(round(bullet["record"]["win"]/bullet["record"]["loss"],2))
    #rapid
    rapid = request["chess_rapid"]
    best.append(rapid["best"]["rating"])
    current.append(rapid["last"]["rating"])
    ratio.append(round(rapid["record"]["win"]/rapid["record"]["loss"],2))  
    #daily
    daily = request["chess_daily"]
    best.append(daily["best"]["rating"])
    current.append(daily["last"]["rating"])
    ratio.append(round(daily["record"]["win"]/daily["record"]["loss"],2))  
    return best, current, ratio

if __name__ == "__main__":
    #username = input("Player name: ")
    username = "BaguettedeFromage"
    profile = profile_info("BaguettedeFromage")
    tournaments = tournament_info("BaguettedeFromage")
    best_rank, rank, ratio =player_rank("BaguettedeFromage")
    print("Username: ",username)
    print("profile: ",profile)
    print("tournaments: ",tournaments)
    print("best_rank: ",best_rank)
    print("rank: ",rank)        
    print("ratio: ",ratio)

