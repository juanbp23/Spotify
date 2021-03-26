from album import Album
from song import Song
from user import User
from artist import Artist
from playlist import Playlist
from exceptions import *
from utils import *


def main():
    
    option = 0
    current_user = None
    while True:

        if current_user == None:
            while True:

                if current_user != None:
                    break
                
                print("")
                print("1. Crear cuenta")
                print("2. Iniciar sesión")
                print("3. Salir")
                print("")

                try:
                    option = int(input("Eliga una opción: "))
                
                except Exception:
                    print("Asegurese de insertar tipo de dato entero (int)")
                    break

                if option == 1:

                    option = 0
                    while True:

                        print("")
                        print("Escoga entre los tipos de cuentas disponibles")
                        print("1. Artista")
                        print("2. Usuario")
                        print("")
                        
                        try:
                            option = int(input("Eliga una opción: "))
                        
                        except Exception:
                            print("Asegurese de insertar tipo de dato entero (int)")
                            continue
                        
                        if option == 1:
                            
                            try:
                                artist_name = input("Introduzca su nombre de artista: ")
                                current_user = Artist(name = artist_name)
                                artists.append(current_user)
                                print("Enhorabuena " + current_user.get_name() + "!, has sido registrado")
                                break
                            except Errorartist as e:
                                print(e)

                            
                        elif option == 2:

                            try: 
                                user_name = input("Introduzca su nombre de usuario: ")
                                current_user = User(name =user_name)
                                users.append(current_user)
                                print("Enhorabuena " + current_user.get_name() + "!, has sido registrado")
                                break
                            
                            except Erroruser as e:
                                print(e)

                        else:
                            print("Asegurese de insertar valores entre el rango 1-2")
                
                elif option == 2:
                    
                    option = 0
                    while True:

                        print("")
                        print("Seleccione su tipo de cuenta")
                        print("1. Artista")
                        print("2. Usuario")
                        print("")
                        
                        try:
                            option = int(input("Eliga una opción: "))
                        
                        except Exception:
                            print("Asegurese de insertar tipo de dato entero (int)")
                            continue
                        
                        if option == 1:
                            
                            for artist in artists:
                                print(artist)
                            
                            log_in = (input("Seleccione el nombre o el id de su cuenta: "))
                            for artist in artists:
                                if str(artist.get_ID()) == log_in or artist.get_name() == log_in:
                                    current_user = artist
                                    print("Inicio de sesión de la cuenta " + current_user.get_name() + " exitoso")
                                    continue

                            if current_user != None:
                                break
                            
                            print("EL nombre o ID introducidos no son correctos, asegurese de iniciar sesión correctamente")
                            continue

                        if option == 2:

                            for user in users:
                                print(user)
                            
                            log_in = (input("Seleccione el nombre o el id de su cuenta: "))
                            for user in users:
                                if str(user.get_ID()) == log_in or user.get_name() == log_in:
                                    current_user = user
                                    print("Inicio de sesión de la cuenta " + current_user.get_name() + " exitoso")
                                    continue

                            if current_user != None:
                                break
                            print("EL nombre o ID introducidos no son correctos, asegurese de iniciar sesión correctamente")
                            continue
                        
                        
                        else:
                            print("Asegurese de insertar valores entre el rango 1-2")
                
                elif option == 3:
                    exit()
                else:
                    print("Asegurese de insertar valores en el rango 1-3")

        if isinstance(current_user, Artist):

            while True:   

                print("")
                print("1. Mostrar playlist/s seguidas")
                print("2. Mostrar playlist/s creadas")      
                print("3. Ver canción")
                print("4. Ver álbum")
                print("5. Ver artista")
                print("6. Seguir playlist")
                print("7. Dejar de seguir playlist")
                print("8. Crear playlist")
                print("9. Eliminar playlist")
                print("10. Añadir canción a la playlist")
                print("11. Borrar canción de una playlist")
                print("12. Mostrar canciones ")
                print("13. Mostrar álbumes ")
                print("14. Subir álbum ")
                print("15. Borrar álbum")
                print("16. Añadir canción a un álbum")
                print("17. Eliminar canción de un álbum")
                print("18. Salir usuario")

                try:
                    option = int(input("Eliga una opción: "))
                
                except Exception:
                    print("Asegurese de insertar tipo de dato entero (int)")

                if option == 1:
                    for playlist in current_user.get_playlist_followed():
                        print(playlist)
                    continue

                if option == 2:
                    for playlist in current_user.get_playlist_created():
                        print(playlist)
                    continue

                if option == 3:
                    songs_find = []
                    
                    song_ = str(input("Inserte el ID o nombre de la canción:"))

                    for song in songs:
                        if str(song.get_ID()) == song_ or song.get_name() == song_:
                            songs_find.append(song)

                    if len(songs_find) == 0:
                        print("Lo sentimos, pero ninguna canción coincide con los criterios establecidos")

                    else:
                        for song in songs_find:
                            print(song)
                    
                    continue
                
                if option == 4:
                    albums_find = []

                    album_ = str((input("Seleccione el nombre del álbum: ")))

                    for album in albums:
                        if str(album.get_name()) == album_:
                            albums_find.append(song)

                    if len(albums_find) == 0:
                        print("Lo sentimos, pero ningun álbum coincide con los criterios establecidos")

                    else:
                        for album in albums_find:
                            print(album)
                    
                    continue

                if option == 5:
                    artists_find = []

                    artist_ = str((input("Seleccione el nombre del artista: ")))

                    for artist in artists:
                        if str(artist.get_name()) == artist_:
                            artists_find.append(song)

                    if len(artists_find) == 0:
                        print("Lo sentimos, pero ningun álbum coincide con los criterios establecidos")

                    else:
                        for artist in artists_find:
                            print(artist)
                    
                    continue

                if option == 6:
                    
                    maximum = 0
                    for playlist in order_playlists(playlists):
                        maximum += 1
                        print(playlist)
                        if maximum == 100:
                            break

                    playlist_to_follow = str( input ("Selecione el id de la playlist que desea seguir: "))
                    find = False

                    try:
                            
                        for playlist in playlists:
                            if str(playlist.get_ID()) == playlist_to_follow:
                                current_user.follow_playlist(playlist)
                                find = True
                                print("Se ha añadido a su lista de playlist seguidas: " + playlist.get_name())
                            
                    except Erroruser or Errorartist as e:
                        print(e)  
                        continue

                    if find == False:
                        print("Lo sentimos, pero no tenemos registrada ninguna playlist con dicho id ")
                    continue

                if option == 7:

                    for playlist in current_user.get_playlist_followed():
                        print(playlist)

                    playlist_to_unfollow = str( input ("Selecione el id de la playlist que desea dejar de seguir: "))
                    delete = False
                    
                    for playlist in current_user.get_playlist_followed():
                        if playlist_to_unfollow == str(playlist.get_ID()):
                            current_user.unfollow_playlist(playlist)
                            delete = True
                            print("Se ha eliminado a su lista de playlist seguidas: " + playlist.get_name())
             
                    if delete == False:
                        print("Lo sentimos, pero no tenemos registrada ninguna playlist con dicho id ")
                    continue


                if option == 8:

                    try:
                        playlist_name = str(input("Que nombre le quiere dar a su playlist: "))
                        playlist = Playlist(user_creator=current_user, name = playlist_name)
                        current_user.create_playlist(playlist)
                        print("La playlist " + playlist.get_name() + " ha sido creada correctamente")
                        continue

                    except Errorplaylist as e:
                        print("No ha sido posible crear la playlist")
                        print(e)
        
                        continue

                if option == 9:


                    for playlist in current_user.get_playlist_created():
                        print(playlist)

                    delete = False
                    playlist_delete = input ("Selecione el id de la playlist que desea eliminar: ")

                    for playlist in current_user.get_playlist_created():
                        if playlist_delete == str(playlist.get_ID()):
                            current_user.delete_playlist(playlist)
                            delete = True
                            print("La playlist " + playlist.get_name() + " ha sido eliminada correctamente")
                            continue
                    
                    if not delete:
                        print("No ha sido posible encontrar la playlist con el id insertado")
                        continue



                if option == 10:

                    for playlist in current_user.get_playlist_created():
                        print(playlist)

                    find = False
                    playlist_id = input ("Selecione el id de la playlist a la que desea añadir la canción: ")

                    for playlist in current_user.get_playlist_created():
                        if playlist_id == str(playlist.get_ID()):
                            find = True
                            playlist_ = playlist
                            print("La playlist " + playlist.get_name() + " ha sido encontrada")
                            continue
                    
                    if find:
                        find = False
                        song_id = str(input("Inserte el ID de la canción que desea insertar: "))

                        for song in songs:
                            if str(song.get_ID()) == song_id:
                                find = True
                                playlist_.add_song_to_playlist(song)
                                print("Se ha añadido correctamente la canción " + song.get_name() + " a la playlist " + playlist_.get_name())
                                

                        if not find:
                            print("Lo sentimos, pero ninguna canción coincide con los criterios establecidos")
                            
                        
                        continue

                    else:
                        print("No ha sido posible encontrar la playlist con el id insertado")
                        continue

                if option == 11:

                    for playlist in current_user.get_playlist_created():
                        print(playlist)

                    find = False
                    playlist_id = input ("Selecione el id de la playlist a la que desea eliminar una canción: ")

                    for playlist in current_user.get_playlist_created():
                        if playlist_id == str(playlist.get_ID()):
                            find = True
                            playlist_ = playlist
                            print("La playlist " + playlist.get_name() + " ha sido encontrada")
                            continue
                    
                    if find:
                        find = False

                        for song in playlist_.get_songs():
                            print(song)

                        song_id = str(input("Inserte el ID de la canción que desea eliminar: "))

                        for song in playlist_.get_songs():
                            if str(song.get_ID()) == song_id:
                                find = True
                                playlist_.delete_song_to_playlist(song)
                                print("Se ha eliminado correctamente la canción " + song.get_name() + " a la playlist " + playlist_.get_name())
                                

                        if not find:
                            print("Lo sentimos, pero ninguna canción coincide con los criterios establecidos")
                            
                        
                        continue

                    else:
                        print("No ha sido posible encontrar la playlist con el id insertado")
                        continue
                
                if option == 12:

                    print("Canciones propias: ")
                    for album in current_user.get_albums():
                        for song in album.get_songs():
                            print(song)

                    print("Colaboraciones: ")
                    for song in current_user.get_collaborations():
                        print(song)
                    
                    continue

                if option == 13:
                    print("Álbums: ")
                    for album in current_user.get_albums():
                        print(album)
                    
                    continue
                
                if option == 14:

                    try:
                        album_name = str(input("Que nombre le quiere dar a su álbum: "))
                        album = Album(artist= current_user, name = album_name)
                        current_user.add_album(album)
                        print("El álbum " + album.get_name() + " ha sido creada correctamente")
                        continue

                    except Errorplaylist as e:
                        print("No ha sido posible crear el álbum")
                        print(e)
        
                        continue

                if option == 15:
                    
                    if len(current_user.get_albums()) == 0:
                        print("Primero has de crear un álbum para poder borrarlo ")
                        continue

                    print("Álbums: ")
                    for album in current_user.get_albums():
                        print(album)

                    find = False
                    album_id = str(input("Seleccione el id del álbum sque quieres borrar: "))
                    
                    for album in current_user.get_albums():
                        if str(album.get_ID()) == album_id:
                            album_ = album
                            find = True
                        
                    if find:

                        current_user.delete_album(album_)
                        print("El álbum " + album_.get_name() + " ha sido borrado")
                        continue

                    else:
                        print("No ha sido posible encontrar ningun álbum con la id insertada")
                        continue


                if option == 16:

                    if len(current_user.get_albums()) == 0:
                        print("Primero has de crear un álbum para poder añadirle canciones")
                        continue

                    print("Álbums: ")
                    for album in current_user.get_albums():
                        print(album)

                    find = False
                    album_id = str(input("Seleccione el id del álbum sobre el que quieres añadir su canción: "))
                    
                    for album in current_user.get_albums():
                        if str(album.get_ID()) == album_id:
                            album_ = album
                            find = True
                        
                    if find:
                        artists_ = []
                        artists_.append(current_user)
                        print("Quiere añadir algun algun artista como colaborador?")
                        
                        while True:
                            
                            collaboration = str(input(" (si / no):  "))

                            if collaboration == "si":
                                artist_id = str(input("Seleccione el id del artista: "))
                                find = False

                                for artist in artists:
                                    
                                    if str(artist.get_ID()) == artist_id:
                                        artists_.append(artist)
                                        find = True

                                if not find:
                                    print("No hemos encontrado un artista con el id insertado")

                            elif collaboration == "no":
                                break

                            else:
                                print("rellene el campo como se especifica")

                        try:
                            song_name = str(input("Que nombre le quiere dar a su canción: "))
                            song = Song(album = album_, artists = artists_, name = song_name )
                            album_.add_song(song)
                            
                            for i in range(1, len(artists_)):
                                artists_[i].add_collaboration(song)

                            print("La canción " + song.get_name() + " ha sido añadida al álbum " + album_.get_name() + " correctamente")
                            continue

                        except Errorplaylist as e:
                            print("No ha sido posible crear el álbum")
                            print(e)
                            continue


                    else:
                        print("No ha sido posible encontrar ningun álbum con la id insertada")
                        continue
                
                if option == 17:

                    if len(current_user.get_albums()) == 0:
                        print("Primero has de crear un álbum para poder borrarle canciones")
                        continue

                    print("Álbums: ")
                    for album in current_user.get_albums():
                        print(album)

                    find = False
                    album_id = str(input("Seleccione el id del álbum sobre el que quieres borrar una canción: "))
                    
                    for album in current_user.get_albums():
                        if str(album.get_ID()) == album_id:
                            album_ = album
                            find = True
                        
                    if find:
                        
                        find = False
                        for song in album_.get_songs():
                            print(song)

                        song_id = str(input("Inserte el ID de la canción que desea eliminar: "))

                        for song in album_.get_songs():

                            if str(song.get_ID()) == song_id:
                                find = True
                                album_.delete_song(song)

                                for i in range(1,len(song.get_artists())):
                                    song.get_artists()[i].delete_collaboration(song)

                                print("Se ha eliminado correctamente la canción " + str(song.get_name()) + " del álbum " + str(album_.get_name()) )
                                
                        if not find:
                            print("Lo sentimos, pero ninguna canción coincide con los criterios establecidos")
                                 
                        continue

                    else:
                        print("No ha sido posible encontrar ningun álbum con la id insertada")
                        continue

                if option == 18:
                    current_user = None
                    break
                
                else:
                    print("Asegurese de insertar valores entre el rango 1-8")
                    

        if isinstance(current_user, User):

            while True:   

                print("")
                print("1. Mostrar playlist/s seguidas")
                print("2. Mostrar playlist/s creadas")      
                print("3. Ver canción")
                print("4. Ver álbum")
                print("5. Ver artista")
                print("6. Seguir playlist")
                print("7. Dejar de seguir playlist")
                print("8. Crear playlist")
                print("9. Eliminar playlist")
                print("10. Añadir canción a la playlist")
                print("11. Borrar canción de una playlist")
                print("12. Salir de usuario")

                try:
                    option = int(input("Eliga una opción: "))
                
                except Exception:
                    print("Asegurese de insertar tipo de dato entero (int)")

                if option == 1:
                    for playlist in current_user.get_playlist_followed():
                        print(playlist)
                    continue

                if option == 2:
                    for playlist in current_user.get_playlist_created():
                        print(playlist)
                    continue

                if option == 3:
                    songs_find = []
                    
                    song_ = str(input("Inserte el ID o nombre de la canción:"))

                    for song in songs:
                        if str(song.get_ID()) == song_ or song.get_name() == song_:
                            songs_find.append(song)

                    if len(songs_find) == 0:
                        print("Lo sentimos, pero ninguna canción coincide con los criterios establecidos")

                    else:
                        for song in songs_find:
                            print(song)
                    
                    continue
                
                if option == 4:
                    albums_find = []

                    album_ = str((input("Seleccione el nombre del álbum: ")))

                    for album in albums:
                        if str(album.get_name()) == album_:
                            albums_find.append(song)

                    if len(albums_find) == 0:
                        print("Lo sentimos, pero ningun álbum coincide con los criterios establecidos")

                    else:
                        for album in albums_find:
                            print(album)
                    
                    continue

                if option == 5:
                    artists_find = []

                    artist_ = str((input("Seleccione el nombre del artista: ")))

                    for artist in artists:
                        if str(artist.get_name()) == artist_:
                            artists_find.append(song)

                    if len(artists_find) == 0:
                        print("Lo sentimos, pero ningun álbum coincide con los criterios establecidos")

                    else:
                        for artist in artists_find:
                            print(artist)
                    
                    continue

                if option == 6:
                    
                    maximum = 0
                    for playlist in order_playlists(playlists):
                        maximum += 1
                        print(playlist)
                        if maximum == 100:
                            break

                    playlist_to_follow = str( input ("Selecione el id de la playlist que desea seguir: "))
                    find = False

                    try:
                            
                        for playlist in playlists:
                            if str(playlist.get_ID()) == playlist_to_follow:
                                current_user.follow_playlist(playlist)
                                find = True
                                print("Se ha añadido a su lista de playlist seguidas: " + playlist.get_name())
                            
                    except Erroruser or Errorartist as e:
                        print(e)  
                        continue

                    if find == False:
                        print("Lo sentimos, pero no tenemos registrada ninguna playlist con dicho id ")
                    continue

                if option == 7:

                    for playlist in current_user.get_playlist_followed():
                        print(playlist)

                    playlist_to_unfollow = str( input ("Selecione el id de la playlist que desea dejar de seguir: "))
                    delete = False
                    
                    for playlist in current_user.get_playlist_followed():
                        if playlist_to_unfollow == str(playlist.get_ID()):
                            current_user.unfollow_playlist(playlist)
                            delete = True
                            print("Se ha eliminado a su lista de playlist seguidas: " + playlist.get_name())
             
                    if delete == False:
                        print("Lo sentimos, pero no tenemos registrada ninguna playlist con dicho id ")
                    continue

                if option == 8:

                    try:
                        playlist_name = input("Que nombre le quiere dar a su playlist: ")
                        playlist = Playlist(user_creator=current_user, name = playlist_name)
                        current_user.create_playlist(playlist)
                        print("La playlist " + playlist.get_name() + " ha sido creada correctamente")
                        continue

                    except Errorplaylist as e:
                        print("No ha sido posible crear la playlist")
                        print(e)
        
                        continue

                if option == 9:


                    for playlist in current_user.get_playlist_created():
                        print(playlist)

                    delete = False
                    playlist_delete = input ("Selecione el id de la playlist que desea eliminar: ")

                    for playlist in current_user.get_playlist_created():
                        if playlist_delete == str(playlist.get_ID()):
                            current_user.delete_playlist(playlist)
                            delete = True
                            print("La playlist " + playlist.get_name() + " ha sido eliminada correctamente")
                            continue
                    
                    if not delete:
                        print("No ha sido posible encontrar la playlist con el id insertado")
                        continue

                if option == 10:

                    for playlist in current_user.get_playlist_created():
                        print(playlist)

                    find = False
                    playlist_id = input ("Selecione el id de la playlist a la que desea añadir la canción: ")

                    for playlist in current_user.get_playlist_created():
                        if playlist_id == str(playlist.get_ID()):
                            find = True
                            playlist_ = playlist
                            print("La playlist " + playlist.get_name() + " ha sido encontrada")
                            continue
                    
                    if find:
                        find = False
                        song_id = str(input("Inserte el ID de la canción que desea insertar: "))

                        for song in songs:
                            if str(song.get_ID()) == song_id:
                                find = True
                                playlist_.add_song_to_playlist(song)
                                print("Se ha añadido correctamente la canción " + song.get_name() + " a la playlist " + playlist_.get_name())
                                

                        if not find:
                            print("Lo sentimos, pero ninguna canción coincide con los criterios establecidos")
                            
                        
                        continue

                    else:
                        print("No ha sido posible encontrar la playlist con el id insertado")
                        continue

                if option == 11:

                    for playlist in current_user.get_playlist_created():
                        print(playlist)

                    find = False
                    playlist_id = input ("Selecione el id de la playlist a la que desea eliminar una canción: ")

                    for playlist in current_user.get_playlist_created():
                        if playlist_id == str(playlist.get_ID()):
                            find = True
                            playlist_ = playlist
                            print("La playlist " + playlist.get_name() + " ha sido encontrada")
                            continue
                    
                    if find:
                        find = False

                        for song in playlist_.get_songs():
                            print(song)

                        song_id = str(input("Inserte el ID de la canción que desea eliminar: "))

                        for song in playlist_.get_songs():
                            if str(song.get_ID()) == song_id:
                                find = True
                                playlist_.delete_song_to_playlist(song)
                                print("Se ha eliminado correctamente la canción " + song.get_name() + " a la playlist " + playlist_.get_name())
                                

                        if not find:
                            print("Lo sentimos, pero ninguna canción coincide con los criterios establecidos")
                            
                        
                        continue

                    else:
                        print("No ha sido posible encontrar la playlist con el id insertado")
                        continue

                if option == 12:
                    current_user = None
                    break
                
                else:
                    print("Asegurese de insertar valores entre el rango 1-8")
                    





main()