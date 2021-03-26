from exceptions import Erroruser
from playlist import Playlist

class User ():
    number_id = 0
    def __init__(self, name, ID = None, playlist_followed = None, playlist_created = None):
        # ID llega como parametro
        User.number_id += 1

        if ID != None:
            if isinstance(ID, int):
                self.ID = ID
            else: 
                raise Erroruser ("El usuario creado no tiene el ID en el formato correcto (int)")
        else:
            self.ID = User.number_id

        self.set_name(name)
        self.set_playlist_followed(playlist_followed)
        self.set_playlist_created(playlist_created)



    def set_name(self, name):
        
        if isinstance(name, str):
            self.name = name
        else:
            raise Erroruser("El usuario creado no tiene nombre o el formato esta incorrecto (str)")

    def set_playlist_followed(self, playlist_followed):
        
        if playlist_followed == None:
            self.playlist_followed = []
        elif isinstance(playlist_followed, list):
            for playlist in playlist_followed:
                if not isinstance(playlist, Playlist):
                    raise Erroruser("El usuario creado debe tener las playlist seguidas dentro de la lista han de ser en formato Playlist (Playlist)")
            self.playlist_followed = playlist_followed
        else:
            raise Erroruser("El usuario creado debe tener las playlist seguidas por medio de una lista (list)")
    
    def set_playlist_created(self, playlist_created):

        if playlist_created == None:
            self.playlist_created = []
        elif isinstance(playlist_created, list):
            for playlist in playlist_created:
                if not isinstance(playlist, Playlist):
                    raise Erroruser("El usuario creado debe tener las playlist creadas dentro de la lista han de ser en formato Playlist (Playlist)")
            self.playlist_created = playlist_created
        else:
            raise Erroruser("El usuario creado debe tener las playlist creadas  introducidas por medio de una lista (list)")

    def get_name(self):
        return self.name

    def get_playlist_followed(self):
        return self.playlist_followed

    def get_playlist_created(self):
        return self.playlist_created
    
    def get_ID(self):
        return self.ID

    def create_playlist(self, playlist):

        if isinstance(playlist, Playlist):
            self.get_playlist_created().append(playlist)
        else:
            raise Erroruser ("El usuario debe crear una playlist (Playlist)")
        
    def delete_playlist(self, playlist):
        
        if isinstance(playlist, Playlist):
            self.get_playlist_created().remove(playlist)
        else:
            raise Erroruser ("El usuario debe eliminar una playlist (Playlist)")
        
    def follow_playlist (self, playlist):

        if playlist in self.get_playlist_created():
            raise Erroruser ("El usuario no puede seguir su propia playlist")
        
        if isinstance(playlist, Playlist):

            if self.check_playlist_followed_repeated(playlist):
                self.get_playlist_followed().append(playlist)
                playlist.add_follower(self)
            else:
                raise Erroruser ("No se puede seguir una playlist más de una vez!")
            
        else:
            raise Erroruser ("El usuario debe seguir una playlist (Playlist)")

    def unfollow_playlist (self, playlist):
   
        if isinstance(playlist, Playlist):
            self.get_playlist_followed().remove(playlist)
            playlist.delete_follower(self)
        
        else:
            raise Erroruser ("El usuario debe seguir una playlist (Playlist)")
        
    def check_playlist_followed_repeated(self, playlist):

        if playlist in self.get_playlist_followed():
            return False
        else:
            return True

    def __str__(self):
        return ("USUARIO     Nombre de usuario: " + self.get_name() + ", ID: " + str(self.get_ID()) + ", Playlist seguidas: " + str(self.get_playlist_followed()) + ", Playlist creadas: " + str(self.get_playlist_created()))


