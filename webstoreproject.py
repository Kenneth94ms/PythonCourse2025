# Your code below: 
#Maria Web Store

#1D list/arrays
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]

preferred_size.append("Medium")
print(preferred_size)

#2D lists/array
customer_data = [["Ainsley", "Small", True],["Ben", "Large", False],["Chani", "Medium", True],["Depak", "Medium", False]]
print(customer_data)

customer_data[2][2] = False

#Used for remove value on list based on idex plus indicate directly item to remove
customer_data[1].remove(False)
print(customer_data)

#concatenate 2 list or list plus new sublists
customer_data_final = customer_data + [["Amit", "Large", True],["Karim", "X-Large", False]]
print(customer_data_final)