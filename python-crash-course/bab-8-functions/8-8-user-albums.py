#Start with your program from Exercise 8-7. 
# Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and 
# print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.

def make_album(artis, album):
    '''Return artis name, album'''
    info = {'name':artis, 'name album': album}
    return info

while True:
    print("Plase tell your favorite artist:")
    print("enter quit to quit")

    artis_name = input("Name :")
    if artis_name == 'quit':
        break
    album_name = input("Album :")
    if artis_name == 'quit':
        break



    print(make_album(artis_name, album_name))



