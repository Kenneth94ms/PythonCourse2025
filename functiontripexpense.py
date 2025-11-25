current_budget = 3500.75
shirt_expense = 9

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 
def deduct_expense(budget, expense):
  return budget - expense

#code for call function and asign to a variable
new_budget_after_shirt = deduct_expense(current_budget,shirt_expense)
#print the content of the variable
print(new_budget_after_shirt)

#calling function and passing argument
print_remaining_budget(new_budget_after_shirt)

#multiplke returns
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()
print(most_popular1)
print(most_popular2)
print(most_popular3)