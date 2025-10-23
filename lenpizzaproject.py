# Your code below:
#variables
toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2,6,1,3,2,7,2]

#methods
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print(num_pizzas)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#2D list of combine prices + ingredients manually, you can usa concatenate prices + prizzas but need extra work
pizza_and_prices = [[2,"pepperoni"],[6,"pineapple"],[1,"cheese"],[3,"sausage"],[2,"olives"],[7,"anchovies"],[2,"mushrooms"]]
print(pizza_and_prices)

#sorted pizzas in ascending value price
pizza_and_prices_sorted = sorted(pizza_and_prices)
print(pizza_and_prices_sorted)

#method for extrac the first list/element of a 2D list based on index value
cheapest_pizza = pizza_and_prices_sorted[0:1]
print(cheapest_pizza)

#method for extract the last list/element of a 2D lsit based on last index value negative
priciest_pizza = pizza_and_prices_sorted[-1:]
print(priciest_pizza)

#method pop() empty remove the last element of a list
pizza_and_prices_sorted.pop()
print(pizza_and_prices_sorted)

#method for insert a new element/list inside the list based on index
pizza_and_prices_sorted.insert(4,[2.5,"peppers"])
print(pizza_and_prices_sorted)

#method for extract and saved element of a list based on fisrt index and last excluding last
three_cheapest = pizza_and_prices_sorted[0:3]