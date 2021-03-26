from exceptions import Errorplaylist
from song import Song

class Playlist():
    number_playlists = 0
    def __init__(self, user_creator, name, ID = None, users_followers = None, songs = None):
        
        from user import User
        
        if ID == None:
            Playlist.number_playlists += 1
            self.ID = Playlist.number_playlists
        else:
            if isinstance(ID, int):
                self.ID = ID
            else:
                raise Errorplaylist("La playlist creada ha de tener un ID en formato entero  (int)")

        if isinstance(user_creator, User):
            self.user_creator = user_creator
        else:
            raise(Errorplaylist("La playlist creada ha de tener un usuario propietario (User)"))

        self.set_users_followers(users_followers)
        self.set_songs(songs)
        self.set_name(name)
            
    def set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise Errorplaylist("La playlist creada no tiene nombre o el formato esta incorrecto (str)")

    def get_name(self):
        return self.name

    def get_user_creator(self):
        return self.user_creator

    def get_user_followers(self):
        return self.users_followers
    
    def get_songs(self):
        return self.songs
    
    def get_ID(self):
        return self.ID

    def set_users_followers(self, users_followers):
        
        if users_followers == None:
            self.users_followers = []
        elif isinstance(users_followers, list):
            for user in users_followers:
                if not isinstance(user, User):
                    raise Errorplaylist("Las playlist seguidas dentro de la lista han de ser en formato Playlist (Playlist)")
            self.users_followers = users_followers
        else:
            raise Errorplaylist("Las playlist seguidas deben estan introducidas por medio de una lista (list)")
        
    def set_songs(self, songs):

        if songs == None:
            self.songs = []
        elif isinstance(songs, list):
            for song in songs:
                if not isinstance(song, Song):
                    raise Errorplaylist("La playlist creada debe de tener canciones en formato de song dentro de la lista (Song)")
            self.songs = songs
        else:
            raise Errorplaylist("La playlist creada debe de tener canciones en formato de lista (list)")

    def add_follower(self, user):
        from user import User
        
        if isinstance(user, User):
            self.get_user_followers().append(user)
        else:
            raise Errorplaylist ("La playlist creada solo puede ser seguida por usuarios o artistas (User)")
        
    def delete_follower(self, user):
        from user import User
        
        if isinstance(user, User):
            self.get_user_followers().remove(user)
        else:
            raise Errorplaylist ("La playlist creada solo puede ser seguida por usuarios o artistas (User)")        
    
    def add_song_to_playlist(self, song):

        if isinstance(song, Song):
            self.get_songs().append(song)
        else:
            raise Errorplaylist ("Asegurate de añadir canciones de tipo Song (Song)")

    def delete_song_to_playlist(self, song):
        
        
        if isinstance(song, Song):
            self.get_songs().remove(song)
        else:
            raise Errorplaylist ("Asegurate de añadir canciones de tipo Song (Song)")

    def __str__(self):
        #return ("PLAYLIST     Nombre: " + str(self.get_name()) + ", ID: " + str(self.get_ID()) + ", Propietario: " + self.get_user_creator.get_name() + ", Seguidores: " + str(len(self.get_user_followers())) + ", Canciones: " + self.get_songs_name() )
        return ("PLAYLIST     Nombre: " + str(self.get_name()) + ", ID: " + str(self.get_ID()) + ", Propietario: " + str(self.get_user_creator().get_name()) + ", Seguidores: " + str(len(self.get_user_followers())) + ", Canciones: " + str(self.get_songs()))

    def __repr__(self):
        return ("Nombre: " + str(self.get_name()) + ", Número canciones: " + str(len(self.get_songs())))      

