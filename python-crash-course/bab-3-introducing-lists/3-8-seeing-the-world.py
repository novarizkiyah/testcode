# Seeing the World : Think of at least 5 places in the world you'd like to visit

# 1. store the location in a list. Make sure the list is not alphabetical order.
my_go_to_places = ['madinah', 'paris', 'gowa', 'washington', 'jogjakarta']

#2. print your list in its original order. Don't worry about printing the list neatly; just print it as a raw Python list.
print("Print lokasi awal: ")
print(my_go_to_places)

#3. use sorted() to print your list in alphabetical order without modifying the actual list
print("Print lokasi setelah diurutkan secara alfabet pakai fungsi sorted() : ")
print(sorted(my_go_to_places))

#4. show that your list is still in its original order by printing it.
print("Karena pake fungsi sorted() maka itu temporari saja : ")
print(my_go_to_places)

#5. use sorted() to print your list in reverse-alphabetical order without changing the order of the original list
print("Nah, bisa juga fungsi sorted() reverse alfabetic tetap temporari contohnya: ")
print(sorted(my_go_to_places, reverse=True))

#6. show that your list is still in its original order by printing it again
print("Nah kan, setelah diprint tetap balik ke lokasi awal: " )
print(my_go_to_places)

#7. Use reverse() to change the order of your list. Print the list to show that its order has changed
print("Kali ini pakai reverse() method agar cuma balik dari list bukan secara alfabet tapi ini permanent: ")
my_go_to_places.reverse()
print(my_go_to_places)

#8. Use reverse() to change the order of your list. Print the list to show it's back to its original order.
print("Meski permanent, bisa balikin ke lokasi awal dengan reverse() method lagi: ")
my_go_to_places.reverse()
print(my_go_to_places)

#9. Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed.
print("kalau mau secara alfabet permanent pakai sort() method: ")
my_go_to_places.sort()
print(my_go_to_places)

#10. Use sort() to change your list so it's stored in reverse-alphabetical order. Ptint the list to show that its order has changed.
print("kalau mau balikin reverse alfabetik dan permanen tinggal tambahin reverse=True: ")
my_go_to_places.sort(reverse=True)
print(my_go_to_places)