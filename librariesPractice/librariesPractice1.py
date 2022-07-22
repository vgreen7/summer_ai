import math
import random

result_1 = math.pow(2,4)
print("Result 1 is", result_1)

result_2 = math.sqrt(16)
print("Result 2 is", result_2)

result_3 = random.randint(0,100)
print("Result 3 is", result_3)

names = ["Will", "Billy", "Max", "El", "Mike", "Hopper", "Dustin", "Lucas", "Joyce"]
print("Original names: ", names)

random.shuffle(names)
print("Names after shuffling: ", names)

result_4 = random.choice(names)
print("Chosen name is: ", result_4)