from games.models import Game as GameModel, GameHistory as GameHistoryModel, GameContract as GameContractModel

def __with_sponsored_game(query_set):
    return __game_list_set().filter(is_new=2).union(query_set)

def __game_list_set():
    return GameModel.objects.only(
                'id', 'name', 'detail_link', 'profile_pic', 'short_desc', 'genres', 'block_chains', 'devices',\
                'status', 'nft', 'f2p', 'p2e', 'p2e_score', 'social_24h', 'social_7d', 'is_new' )