#Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, 
# and it should return a dictionary containing these two pieces of information. 
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album information correctly.

#Add an optional parameter to make_album() that allows you to store the nubmer of tracks on an album. 
# If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. 
# Make at least one new function call that includes the number of tracks on an album.

def make_album(artist, title, tracks=None):
    album_info = {
        'artist': artist,
        'title': title
    }
    if tracks is not None:
        album_info['tracks'] = tracks
    return album_info

# Creating album dictionaries with and without the number of tracks
album1 = make_album("Taylor Swift", "Folklore", 16)
album2 = make_album("The Weeknd", "After Hours")
album3 = make_album("Adele", "30", 12)

# Printing the album information
print(album1)
print(album2)
print(album3)

