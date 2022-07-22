from math import pow as power
from math import sqrt as squareroot
from random import shuffle as shuff
from random import randint as randomnum
from random import choice as choose

result_1 = power(2,4)
print("Result 1 is", result_1)

result_2 = squareroot(16)
print("Result 2 is", result_2)

result_3 = randomnum(0,100)
print("Result 3 is", result_3)

names = ["Will", "Billy", "Max", "El", "Mike", "Hopper", "Dustin", "Lucas", "Joyce"]
print("Original names: ", names)

shuff(names)
print("Names after shuffling: ", names)

result_4 = choose(names)
print("Chosen name is: ", result_4)