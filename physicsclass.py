# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
# code to calculate farenheit to celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32)*5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# code to calculate celsius to farenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_farenheit = c_to_f(0)
print(c0_in_farenheit)

#code to calculate force of an object with mass per acceleration
def get_force(mass, acceleration):
  force = mass*acceleration
  return force

train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

#code to calculate energy of an object
def get_energy(mass, c = 3*10**8):
  calcenergy = mass*c**2
  return calcenergy

bomb_energy = get_energy(bomb_mass)
print(bomb_energy)
print("A 1Kg bomb supplies " + str(bomb_energy) + " Joules.")

#code to calculate work of an object
def get_work(mass, acceleration, distance):
  work = get_force(mass, acceleration)*distance
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)
print("The GE train does " + str(train_work) + " Joules of work.")