hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#variables for calculate
total_price = 0
average_price = 0
total_revenue = 0
final_total_revenue = 0
average_daily_revenue = 0

#sum all prices on total_price
for price in prices:
  total_price += price
print(total_price)

#avg of all prices
average_price = total_price/len(prices)
print("Average Haircut Price: "+ str(average_price))

#comprehesion list for create new prices minus 5 dollars
new_prices = [price - 5 for price in prices]
print("New prices: " + str(new_prices))

#new loop for count the hairstyle or recorrer the entire hairstyles lenght
for i in range(len(hairstyles)):
  print(i)
  #code for calc total revenue of every hairstyle
  total_revenue = prices[i]*last_week[i]
  print("Total Revenue: " + str(total_revenue))
  #code for sum all revenues
  final_total_revenue += total_revenue
  print("Final revenue(sum): " + str(final_total_revenue))
#code for calculate the avg daily revenue total / total hairstyles
average_daily_revenue = final_total_revenue/7
print("Average daily revenue: " + str(average_daily_revenue))

#method or code for extract prices lower 30 from list new_prices
underprices = [price for price in new_prices if price < 30]
print("Prices lower 30: " + str(underprices))

for i in range(len(new_prices)):
  if i < 30:
    print(i)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)

#cuts_under_30 = [x[i] for x, i in zip(hairstyles, new_prices) if new_prices < 30]
#print(cuts_under_30)
#cuts_under_30 = [prices for prices in new_prices if 6 < 30]
#cuts_under_30 = [hairstyle for hairstyles in range(len(new_prices)) if new_prices[i] < 30]
#print(cuts_under_30)