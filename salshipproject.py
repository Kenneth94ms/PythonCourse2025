weight = 41.5
price = 0
textprice = "Price: $"
groundtext = "Ground Shipping - "
premiumtext = "Ground Shipping Premium - "
dronetext = "Drone Shipping - "

#Ground shipping calculation + message to customer
if weight < 2:
  priceg = weight*1.50 + 20.00
  #a float to concatenate to string need to be converted to str
  groundcost = groundtext + textprice + str(priceg)
  print(groundcost)
elif weight >= 2 and weight < 6:
  priceg = weight*3.00 + 20.00
  groundcost = groundtext + textprice + str(priceg)
  print(groundcost)
elif weight >= 6 and weight < 10:
  priceg = weight*4.00 + 20.00
  groundcost = groundtext + textprice + str(priceg)
  print(groundcost)
elif weight >= 10:
  priceg = weight*4.75 + 20.00
  groundcost = groundtext + textprice + str(priceg)
  print(groundcost)
else:
  priceg == 0
  print("No weight detected")

#Ground shipping premium + message to customer
pricep = 125.00
premiumcost = premiumtext + textprice + str(pricep)
print(premiumcost)

#Drone shipping calculation + message to customer
if weight < 2:
  priced = weight*4.50 + 0.00
  #a float to concatenate to string need to be converted to str
  dronecost = dronetext + textprice + str(priced)
  print(dronecost)
elif weight >= 2 and weight < 6:
  priced = weight*9.00 + 0.00
  dronecost = dronetext + textprice + str(priced)
  print(dronecost)
elif weight >= 6 and weight < 10:
  priced = weight*12.00 + 0.00
  dronecost = dronetext + textprice + str(priced)
  print(dronecost)
elif weight >= 10:
  priced = weight*14.25 + 0.00
  dronecost = dronetext + textprice + str(priced)
  print(dronecost)
else:
  priced == 0
  print("No weight detected")

#Code for check what is the cheapest option, always check identation on python, a syntax error can appear
cheapest = min(priceg, pricep, priced)
if cheapest == priceg:
  print("The cheapest option is " + str(groundcost))
elif cheapest == pricep:
    print("The cheapest option is " + str(premiumcost))
else:
      print("The cheapest option is " + str(dronecost))