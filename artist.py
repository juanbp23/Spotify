from datetime import date
from exceptions import Errorartist
from album import Album
from song import Song
from user import User

class Artist(User):
    names = []
    def __init__(self, name, playlist_followed = None, playlist_created = None, albums = None, collaborations = None):
        # ID viene de BBDD
        super().__init__( name, playlist_followed = None, playlist_created = None)
        
        self.set_albums(albums)
        self.set_collaborations(collaborations)
        self.__add_name(name)

    def set_albums(self, albums):

        if albums == None:
            self.albums = []
        elif isinstance(albums, list):
            for album in albums:
                if not isinstance(album, Album):
                    raise Errorartist("El artista creado tiene que tener los discos dentro de la lista en formato Album (Album)")
            self.albums = albums
        else:
            raise Errorartist("El artista creado tiene que tener los discos dentro de la lista  (list)")

    def set_collaborations(self, collaborations):

        if collaborations == None:
            self.collaborations = []
        elif isinstance(collaborations, list):
            for collaboration in collaborations:
                if not isinstance(collaboration, Song):
                    raise Errorartist("El artista creado ha de tener los discos dentro de la lista en formato Album (Album)")
            self.collaborations = collaborations
        else:
            raise Errorartist("El artista creado ha de tener los discos dentro de la lista en formato Album (Album)")
    
    def get_albums(self):
        return self.albums

    def get_collaborations(self):
        return self.collaborations

    def add_album(self, album):
        if isinstance(album, Album):
            self.albums.append(album)
        else:
            raise Errorartist("El álbum añadido ha de ser en formato Album (Album)")

    def __add_name(self, name):
        # es set_name
        for name_ in Artist.names:
            if name_ == name:
                raise Errorartist("El artista creado no puede repetir nombres respecto a los artistas ya creados ")
        Artist.names.append(name)

    def add_collaboration(self, collaboration):
        if isinstance(collaboration, Song):
            self.get_collaborations().append(collaboration)
        else:
            raise Errorartist("La colaboración añadida ha de ser en formato Song")
    
    def delete_collaboration(self, collaboration):

        if isinstance(collaboration, Song):
            self.get_collaborations().remove(collaboration)
        else:
            raise Errorartist("La colaboración eliminada ha de ser en formato Song")
    

    def add_album(self, album):
        if isinstance(album, Album):
            self.get_albums().append(album)
        else:
            raise Errorartist ("EL álbum creado ha de ser añadido en formato álbum (Album)")

    def delete_album(self, album):
        if isinstance(album, Album):
            self.get_albums().remove(album)
            for song in album.get_songs():
                for i in range(1, len(song.get_artists())):
                    song.get_artists()[i].delete_collaboration(song)
        else:
            raise Errorartist ("EL álbum creado ha de ser añadido en formato álbum (Album)")



    def __str__(self):
        return ("ARTISTA     Nombre de usuario: " + self.get_name() + ", ID: " + str(self.get_ID()) + ", Albums: " + str(self.get_albums()) + ", Colaboraciones: " + str(self.get_collaborations()) + ", Playlist seguidas: " + str(self.get_playlist_followed()))

    def __repr__(self):
        return (self.get_name())

