#Imagine an alien was just shot down in a game
#Create a variable name alien_color abd assign it a value of "green", "yellow", "red"
alien_color = ['green', 'yellow', 'red']

#Write an if statement to test whether the alien's color is green.
#If it is, print a message that the player just earn 5 points.

if 'green' in alien_color:
    print("you earn 5 points")

#Write one version of this program that passes the if test and another that fails
#(The version that fails will have no output)
if 'green' in alien_color:
    print("you earn 5 points")
if 'black' in alien_color:
    print("you earn 6 points")