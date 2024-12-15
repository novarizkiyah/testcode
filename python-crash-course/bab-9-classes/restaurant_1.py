from restaurant import Restaurant, IceCreamStand

restaurant = Restaurant("Praboemoelih", "Indonesian cuisine")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
#Print the number of customers the restaurant has served,
print(f"Restaurant has served : {restaurant.number_served}")
#change this value and print it again.
restaurant.number_served = 15
print(f"Restaurant has served : {restaurant.number_served} at this moment")
# Calling the method set_number_served()
restaurant.set_method_served(30)
print(f"Restaurant has served : {restaurant.number_served} at this moment")
# Calling increment_number_served()
restaurant.increment_number_served(1000)
print(f"Restaurant has served : {restaurant.number_served} at this moment")

restaurant.describe_restaurant()
restaurant.open_restaurant()

icecream = IceCreamStand("Es Krim")
icecream.flavors = ['Strawberry', 'Chocolate', 'Vanilla']
icecream.show_flavors()