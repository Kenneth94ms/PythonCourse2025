weight = 41.5
price = 0
textprice = "Price: $"
groundtext = "Ground Shipping - "
premiumtext = "Ground Shipping Premium - "
dronetext = "Drone Shipping - "

#Ground shipping calculation + message to customer
if weight < 2:
  price = weight*1.50 + 20.00
  #a float to concatenate to string need to be converted to str
  result = groundtext + textprice + str(price)
  print(result)
elif weight >= 2 and weight < 6:
  price = weight*3.00 + 20.00
  result = groundtext + textprice + str(price)
  print(result)
elif weight >= 6 and weight < 10:
  price = weight*4.00 + 20.00
  result = groundtext + textprice + str(price)
  print(result)
elif weight >= 10:
  price = weight*4.75 + 20.00
  result = groundtext + textprice + str(price)
  print(result)
else:
  price == 0
  print("No weight detected")

#Ground shipping premium + message to customer
price = 125.00
result = premiumtext + textprice + str(price)
print(result)

#Drone shipping calculation + message to customer
if weight < 2:
  price = weight*4.50 + 0.00
  #a float to concatenate to string need to be converted to str
  result = dronetext + textprice + str(price)
  print(result)
elif weight >= 2 and weight < 6:
  price = weight*9.00 + 0.00
  result = dronetext + textprice + str(price)
  print(result)
elif weight >= 6 and weight < 10:
  price = weight*12.00 + 0.00
  result = dronetext + textprice + str(price)
  print(result)
elif weight >= 10:
  price = weight*14.25 + 0.00
  result = dronetext + textprice + str(price)
  print(result)
else:
  price == 0
  print("No weight detected")