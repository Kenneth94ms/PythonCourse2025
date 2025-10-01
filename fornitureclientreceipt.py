#Variable for store items plus descriptions for receipt
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00
stylish_sette_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_sette_price = 180.50
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15
sales_tax = .088

#variables for customer one
customer_one_total = 0
customer_one_itemization = ""
customer_one_tax = 0

customer_one_total += lovely_loveseat_price
#print("Price for client one:",customer_one_total)
customer_one_itemization += lovely_loveseat_description
#print("Items for client one:",customer_one_itemization)

customer_one_total += luxurious_lamp_price
#print("Price for client one:",customer_one_total)
customer_one_itemization += luxurious_lamp_description
#print("Items for client one:",customer_one_itemization)

customer_one_tax += customer_one_total*sales_tax
#print("Tax for the purchase 0.8%:",customer_one_tax)

customer_one_total += customer_one_tax
#print("Price for client one + TAX:",customer_one_total)

#Prints for show the receipt to client
print("Customer One Items:")
print("Items for client one:",customer_one_itemization)
print("Customer One Total:")
print("Price for client one + TAX:","{:.2f}".format(customer_one_total))