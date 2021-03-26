import copy
from playlist import Playlist

def order_playlists(playlists):
    """
    Ordena una lista de Playlist en función al número de seguidores
    """
    ordered_playlists = copy.copy(playlists)
    for j in range(0, len(ordered_playlists)-1):
        iteration = 0
        for i in range(0, len(ordered_playlists)-1):
            if len(ordered_playlists[i].get_user_followers()) < len(ordered_playlists[i+1].get_user_followers()):
                supp = ordered_playlists[i]
                ordered_playlists[i] = ordered_playlists[i+1]
                ordered_playlists[i+1] = supp 
                iteration = 1
        if iteration == 0:
            break
    return ordered_playlists
