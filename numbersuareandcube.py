# Your code below:

single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []

#for list for square a number
for digit in single_digits:
  print(digit)
  square = digit**2
  squares.append(square)
print(squares)

#for list for cube a number
cubes = [cube**3 for cube in single_digits]
print(cubes)