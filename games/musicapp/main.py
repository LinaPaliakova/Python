from ascii_art import logo
from songs import songs

def print_playlist():
    for song in songs:
         for i in range(len(song[1:])):
             print(songs.index(song) + 1,':', i + 1, song[0],"-", song[i+1])

def print_song(p_user_song):
    mylist = [int(i) for i in p_user_song.split(":")]
    group = mylist[0]
    song_to_play = mylist[1]
    print(songs[group - 1][0], songs[group - 1][song_to_play], "playing now")  

print(logo)


while True:
     print_playlist()
     user_song = input("Select a song to play using number: (1 : 1): ")
     print_song(user_song)
     user_input = input("Press C to change to song or any other key to quite the app ")
     if user_input != 'C':
       print("Goodbye!")
       break
