last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
#define lists subjects and gardes
subjects = ["physics","calculus","poetry","history"]
print(subjects)

grades = ["98","97","85","88"]
print(grades)

#created 2D list for unify subjects plus grades
gradebook = [["physics",98],["calculus",97],["poetry",85],["history",88]]
print(gradebook)

#method append to add a new subject+grade
gradebook.append(["computer science", 100])
print(gradebook)

gradebook.append(["visual arts", 93])
print(gradebook)

#method to access index and modify value
gradebook[5][1] = 98
print(gradebook)

#method to remove value using index from a list and sublist
gradebook[2].remove(85)
print(gradebook)

#method to add a new value on sublist, the value position is foolow the order 0 1 2 3 etc
gradebook[2].append("Pass")
print(gradebook)

#method to concatenate 2 list/arrays
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)