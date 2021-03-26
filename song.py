from datetime import date
from exceptions import Errorsong


class Song():
    number_songs = 0
    
    
    def __init__(self, album, artists, name, ID = None, start_date = None):
        #Como no se puede cambiar ningun dato tras lanzar la canción, realizamos la construcción en el __init__
        from album import Album
        from artist import Artist

        Song.number_songs += 1

        if ID != None:
            if isinstance(ID, int):
                self.ID = ID
            else: 
                raise Erroruser ("La canción creada no tiene el ID en el formato correcto (int)")
        else:
            self.ID = Song.number_songs

        if isinstance(album, Album):
            self.album = album
            self.album_name = album.get_name()
        else: 
            raise Errorsong("La canción creada no pertenece a ningún álbum (Album)")

        if artists == None:
            raise Errorsong("La canción creada no pertenece a ningún artista (Artist)")

        if isinstance(artists, list):
            if len(artists) == 0:
                raise Errorsong("La canción creada tiene que tener mínimo un artista (Artist)")
            self.artists = artists
        else:
            raise Errorsong("La canción creada ha de ser introducida en formato lista (list of Artists)")

        if isinstance(name, str):
            self.name = name
        else:
            raise Errorsong("La canción creada no tiene nombre (str)")

        if start_date != None:

            if isinstance(start_date, date):
                self.start_date = start_date
            else:
                raise Errorsong("La canción creada debe de tener la fecha de creación en formato date (date)")
        else:
            self.start_date = date.today()
    

    def get_ID(self):
        return(self.ID)

    def get_album(self):
        return(self.album)   
    
    def get_album_name(self):
        return self.album_name

    def get_artists(self):
        return(self.artists)
    
    def get_name(self):
        return(self.name)
    
    def get_start_date(self):
        return(self.start_date)

    def __str__(self):
        return ("CANCIÓN     Nombre:  " + self.get_name() + "  , ID: " + str(self.get_ID()) + "  , Artista: " + str(self.get_artists()) + "  , Álbum: " + self.get_album_name())

    def __repr__(self):
        return (self.get_name() + " - " + str(self.get_artists()) + "     ")