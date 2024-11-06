#Start with your program from Exercise 8-7. 
# Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and 
# print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.

def make_album(artist, album):
    artist = artist.title()
    album = album.title()
    print("This is your data : ")
    info = {'Artist Name' : artist, 'Album Name' : album}
    return info

while True:
    artist_name = input("What is your Artist's name : 'Type quit to exit' ")
    if artist_name.lower() == 'quit':
        print("Thank you!")
        break
    album_name = input("What is your artis's album name : 'Type quit to exit' ")
    if album_name.lower() == 'quit':
        print("Bye!")
        break

    print(make_album(artist_name, album_name))



