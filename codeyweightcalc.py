print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
  print("Planet is Venus")
  codeyweight = weight * 0.91
  print("Codey Weith is:", codeyweight)
elif planet == 2:
  print("Planet is Mars")
  codeyweight = weight * 0.38
  print("Codey Weith is:", codeyweight)
elif planet == 3:
  print("Planet is Jupiter")
  codeyweight = weight * 2.34
  print("Codey Weith is:", codeyweight)
elif planet == 4:
  print("Planet is Saturn")
  codeyweight = weight * 1.06
  print("Codey Weith is:", codeyweight)
elif planet == 5:
  print("Planet is Uranus")
  codeyweight = weight * 0.92
  print("Codey Weith is:", codeyweight)
else:
  print("Planet is Neptune")
  codeyweight = weight * 1.19
  print("Codey Weith is:", codeyweight)
