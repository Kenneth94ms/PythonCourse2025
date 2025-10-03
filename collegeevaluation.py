statement_one = not(4+5<=9)

statement_two = not(8*2) != 20-4

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

#code for check not credits and gpa
if not credits >= 120 and not gpa >= 2.0:
  print("You do not meet either requirement to graduate!")

#code for check credits and gpa
if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")


#code for asign score based on elif use similar to case from java
grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")