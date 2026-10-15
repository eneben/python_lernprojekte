playlist = ["lied_1", "lied_2", "lied_3"]
print(playlist[0])
print(playlist[-1])
playlist.append("lied_4")
playlist.remove("lied_2")
print(f"Playlist: {playlist}, Anzahl Songs: {len(playlist)}")
prüflied = input("Für welches Lied soll geprüft werden, ob es in der Liste ist? ")
if prüflied in playlist:
    print(prüflied, "ist in der Playlist.")
else:
    print(prüflied, "ist nicht in der Playlist.")