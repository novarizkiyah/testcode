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

#Add new line that print only two people for dinner 
print(f"Sorry helemaal, I just have 2 seats for dinner")

#Use pop() to remove guest
last_guest = guest_list.pop(5)
print(last_guest)
print(f"Sorry, {last_guest.title()} I can not invite you to my dinner")

last_second_guest = guest_list.pop(4)
print(last_second_guest)
print(f"Sorry, {last_second_guest.title()} I can not invite you to my dinner")

last_third_guest = guest_list.pop(3)
print(last_third_guest)
print(f"Sorry, {last_third_guest.title()} I can not invite you to my dinner")

last_fourth_guest = guest_list.pop(2)
print(last_fourth_guest)
print(f"Sorry, {last_fourth_guest.title()} I can not invite you to my dinner")

#print 2 guest
print(guest_list)
print(f"Do you want to dinner with me, dear {guest_list[0].title()}")
print(f"Do you want to dinner with me, dear {guest_list[1].title()}")

#delete guest 
del guest_list[0]
del guest_list[0]
print(guest_list)