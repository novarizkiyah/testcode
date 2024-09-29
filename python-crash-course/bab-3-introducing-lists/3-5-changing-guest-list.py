#Mulai dengan item, lalu panggil
guest_list = ['nova', 'aya', 'aryya']
print(guest_list)

print(f"Do you want to dinner with me, dear {guest_list[0].title()}")
print(f"Do you want to dinner with me, dear {guest_list[1].title()}")
print(f"Do you want to dinner with me, dear {guest_list[2].title()}")

#Mengganti item di dalam list
guest_list[0] = 'rizki'
print(guest_list)

#Memanggil lagi
print(f"Do you want to dinner with me, dear {guest_list[0].title()}")
print(f"Do you want to dinner with me, dear {guest_list[1].title()}")
print(f"Do you want to dinner with me, dear {guest_list[2].title()}")


