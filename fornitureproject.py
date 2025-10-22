inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#method for obtain lenght of a list
inventory_len = len(inventory)
print(inventory_len)

#saving first element of a list using the index
first = inventory[0]
print(first)

#saving last element of a list using the index negative
last = inventory[-1]
print(last)

#method for obtain elements of a list using the index frist until last
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

first_3 = inventory[0:3]
print(first_3)

#method for count repetead elements on a list
twin_beds = inventory.count("twin bed")
print(twin_beds)

#method for removing an element from a list using the index value
removed_item = inventory.pop(4)
print(removed_item)

#method for add a new value inside the list, with index value and the value itself
inventory.insert(10, "19th Century Bed Frame")
print(inventory)

#method for sort the list but avoid modify the list, until you asign to og value
inventory = sorted(inventory)
print(inventory)