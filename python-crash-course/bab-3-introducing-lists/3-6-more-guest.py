guest_list = ['nova', 'aya', 'aryya']
print(guest_list)
del guest_list[0]
print(guest_list)
guest_list.append('rizki')
print(guest_list)
guest_list.insert(0, 'mulyono')
guest_list.insert(3,'fufufafa')
guest_list.append('rk')
print(f"Do you want to dinner with me, dear {guest_list[0].title()}")
print(f"Do you want to dinner with me, dear {guest_list[1].title()}")
print(f"Do you want to dinner with me, dear {guest_list[2].title()}")
print(f"Do you want to dinner with me, dear {guest_list[3].title()}")
print(f"Do you want to dinner with me, dear {guest_list[4].title()}")
print(f"Do you want to dinner with me, dear {guest_list[5].title()}")