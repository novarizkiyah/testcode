# Turn your if-else chain in 5-4 into an if-elif-else chain

# 1. if the alien is green, print a message that the player earned 5 points

# 2. if the alien is yellow, print a message that the player earned 10 points

# 3. if the alien is red, print a message that the player earned 15 points

# 4. Write three versions pf this program making sure each message is printed for the appropriate color alien

alien_colors = ["green", "yellow", "red"]

if "green" in alien_colors:
    print("You earn 5 points")
elif "red" in alien_colors:
    print("You earn 10 points")
else:
    print("You earn 15 points")
