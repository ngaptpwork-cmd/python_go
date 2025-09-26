def make_album(artist, title, number=""):
    if number:
        album = {
            "artist_name": artist,
            "album_title": title,
            "number": number,
        }
    else:
        album = {
            "artist_name": artist,
            "album_title": title,
        }
    return album


while True:
    print("Please enter 'q' at anytime to quit")
    title = input("What is your favorite album?")
    if title == "q":
        break
    artist_name = input("And who is the singer of this album? ")
    if artist_name == "q":
        break
    favorite_album = make_album(title, artist_name)
    print(favorite_album)
