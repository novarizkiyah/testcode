guest_list = ['nova', 'aya', 'aryya']
print(guest_list)
del guest_list[0]
print(guest_list)
guest_list.append('rizki')
print(guest_list)
guest_list.insert(0, 'mulyono')
guest_list.insert(3,'fufufafa')
guest_list.append('rk')
print(guest_list)

print(f"Sorry helemaal, I just have 2 seats for dinner")
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

print(guest_list)
print(f"Do you want to dinner with me, dear {guest_list[0].title()}")
print(f"Do you want to dinner with me, dear {guest_list[1].title()}")

del guest_list[0]
del guest_list[0]
print(guest_list)