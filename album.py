from exceptions import Erroralbum
from datetime import date
from song import Song

class Album():
    num_reference = 0
    def __init__(self,  artist, name, ID = None, songs = None, start_date = None):
        
        from artist import Artist

        Album.num_reference =+ 1
        
        if ID == None:
            self.ID = Album.num_reference
        elif isinstance(ID, int):
            self.ID = ID
        else:
            raise Erroralbum("El álbum creado ha de tener el ID en formato entero (int)")

        if isinstance(artist, Artist):
            self.artist = artist
        else: 
            raise Erroralbum("El álbum creado no pertenece a ningún artista (Artist)")

        if isinstance(name, str):
            self.name = name
        else:
            raise Erroralbum("El álbum creado no tiene nombre (str)")
        
        self.set_songs(songs)

        if start_date != None:
            
            if isinstance(start_date, date):
                self.start_date = start_date
            else:
                raise Errorsong("El álbum creado debe de tener la fecha de creación en formato date (date)")
        else:
            self.start_date = date.today()
    
    def get_ID(self):
        return self.ID

    def get_artist(self):
        return self.artist
    
    def get_name(self):
        return self.name

    def get_songs(self):
        return self.songs

    def get_start_date(self):
        return self.start_date

    
    def set_songs(self, songs):
        if songs == None:
            self.songs = []
        elif isinstance(songs, list):
            for song in songs:
                if not isinstance(song, Song):
                    raise Erroralbum("El álbum creado debe tener las canciones dentro de la lista en formato Song (Song)")
            self.songs = songs
        else:
            raise Erroralbum("El álbum creado debe tener las canciones por medio de una lista (list)")

    def add_song(self, song):

        if isinstance(song, Song):
            self.get_songs().append(song)
        else:
            raise Erroralbum("La canción agregada al álbum ha de ser en formato Song (Song)")

    def delete_song(self, song):

        if isinstance(song, Song):
            self.get_songs().remove(song)
        else:
            raise Erroralbum("La canción eliminada al álbum ha de ser en formato Song (Song)")
    
    def __str__(self):
        return ("ÁLBUM     Artista: " + self.get_artist().get_name() + ", Nombre: " + self.get_name() + ", ID: " + str(self.get_ID()) + ", Canciones: " + str(self.get_songs()) + ", Fecha creación: " + str(self.get_start_date()) )
    
    def __repr__(self):
        return( self.get_name())