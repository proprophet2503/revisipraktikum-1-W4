Items_Storage = {}

N_item = int(input("Enter the number of items available in the store: "))

for i in range(N_item):
	item = input(f"Item No.{i+1}: ")
	quantity = int(input("Enter the quantity of the item: "))
	Items_Storage[item] = quantity

print("Dictionary after adding user input: ", Items_Storage)

charlies_cart = {}
storage_after = {}


N_c_item = int(input("Enter the number of items in Charlie's Cart: "))

for i in range(N_c_item):
	c_item = input(f"Item No.{i+1} in Charlie's Cart: ")
	c_quantity = int(input("Enter the quantity of the item in Charlie's Cart: "))
	storage_after_quantity = 0
	charlies_cart[c_item] = c_quantity
	storage_after[c_item] = storage_after_quantity 
	

print("Dictionary after adding user input:", charlies_cart)

'''
how to iterate through a dictionary in python 
so the keys can be cheked if they are the same


'''

for key in Items_Storage:
	for key in charlies_cart:
			storage_after[key] = Items_Storage[key]  - charlies_cart[key]
			

print("Storage after Charlie's purchase: ", storage_after)
			
	

