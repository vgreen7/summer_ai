import math as mathematics
import random as arbitrary

result_1 = mathematics.pow(2,4)
print("Result 1 is", result_1)

result_2 = mathematics.sqrt(16)
print("Result 2 is", result_2)

result_3 = arbitrary.randint(0,100)
print("Result 3 is", result_3)

names = ["Will", "Billy", "Max", "El", "Mike", "Hopper", "Dustin", "Lucas", "Joyce"]
print("Original names: ", names)

arbitrary.shuffle(names)
print("Names after shuffling: ", names)

result_4 = arbitrary.choice(names)
print("Chosen name is: ", result_4)