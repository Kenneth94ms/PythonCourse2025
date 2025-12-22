# Write your function here
def append_size(my_list):
  x = len(my_list)
  print(x)
  my_list.append(x)
  return my_list

# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))



# Write your function here
def append_sum(my_list):
  for x in range(3):
    x = my_list[-1] + my_list[-2]
    my_list.append(x)
  return my_list

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))



# Write your function here
def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  else:
    return my_list2[-1]


# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))



# Write your function here
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False

# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))




# Write your function here
def combine_sort(my_list1, my_list2):
  y = my_list1 + my_list2
  x = sorted(y)
  return x

# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))