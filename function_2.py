def make_album(artist,title,songs = None):
    if songs:
        album = {"artist": artist, "title": title, "Songs" : songs,}
    else:
        album = {"artist": artist, "title": title,}
    return album


    
while True:
    print('\npress enter q anytime to exit')
    artist = input("\nEnter artist name:")
    if artist.lower() == "q":
        break
    title = input("\nEnter title name :")
    if title.lower() == "q":
        break
    Songs = input ("\nHow many songs(press enter if none) : ")
    if Songs.lower() == "q":
        break
    if Songs:
        album = make_album(artist,title, Songs)
        print(album)
    else:
        album = make_album(artist,title)
        print(album)
