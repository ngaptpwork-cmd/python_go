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


first_album = make_album("Taylor Swift", "The Story of Us")
print(first_album)

second_album = make_album("7UpperCut", "Trốn tìm")
print(second_album)

third_album = make_album("Doraemon", "Doraemon OST", number="3")
print(third_album)
