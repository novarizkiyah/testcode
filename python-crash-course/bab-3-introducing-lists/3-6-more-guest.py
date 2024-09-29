# Call everyone that i have bigger table
guest_list = ['nova', 'aya', 'aryya']
print(guest_list)
print(f"Hello {guest_list[0].title()}, I have found bigger table")
print(f"Hello {guest_list[1].title()}, I have found bigger table")
print(f"Hello {guest_list[2].title()}, I have found bigger table")

#Use insert() to add people in the beginning
guest_list.insert(0, 'mulyono')

#Use insert() to add people in the middle
guest_list.insert(3,'fufufafa')

#Use append to add people in the end of your list
guest_list.append('rk')

#Print new invitation to everyone
print(f"Do you want to dinner with me, dear {guest_list[0].title()}")
print(f"Do you want to dinner with me, dear {guest_list[1].title()}")
print(f"Do you want to dinner with me, dear {guest_list[2].title()}")
print(f"Do you want to dinner with me, dear {guest_list[3].title()}")
print(f"Do you want to dinner with me, dear {guest_list[4].title()}")
print(f"Do you want to dinner with me, dear {guest_list[5].title()}")