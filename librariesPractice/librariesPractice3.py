from math import pow, sqrt
from random import randint, shuffle, choice

result_1 = pow(2,4)
print("Result 1 is", result_1)

result_2 = sqrt(16)
print("Result 2 is", result_2)

result_3 = randint(0,100)
print("Result 3 is", result_3)

names = ["Will", "Billy", "Max", "El", "Mike", "Hopper", "Dustin", "Lucas", "Joyce"]
print("Original names: ", names)

shuffle(names)
print("Names after shuffling: ", names)

result_4 = choice(names)
print("Chosen name is: ", result_4)