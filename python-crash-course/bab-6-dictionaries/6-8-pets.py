#Make several dictionaries, where the name of each dictionary is the name of a pet. 
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do print everything you know about each pet.

#Note: When I decided to post solutions and wrote complete programs to solve each exercise, 
# I realized this problem was not as well phrased as it should have been. 
# It doesn’t really make sense to name each dictionary for the pet it describes; 
# that information should really be included in the dictionary, 
# rather than being used as the name of the dictionary. 
# This solution reflects that approach.


pets_1 = {
    'name' : 'doggy',
    'animal' : 'dog',
    'owner' : 'bastian',
}

pets_2 = {
    'name' : 'kitty',
    'animal' : 'cat',
    'owner' : 'nova',

}

pets_3 = {
    'name' : 'sniky',
    'animal' : 'snake',
    'owner' : 'rahmat',
}
    
pets = [pets_1, pets_2, pets_3]

for pet in pets:
    print(
        f"My pate name is {pet['name'].title()},",
        f"it is a {pet['animal']},",
        f"then the owner name's {pet['owner'].title()}"         
    )