#Task 2: Write a program that converts from hours to minutes or minutes to hours depending on the user's choice.

time_decision = input("Minutes or Hours? ")

if (time_decision == "Minutes"):
    minutes_input = input("How many minutes? ")
    minutes = int(minutes_input)
    hours = minutes / 60
    print(hours)
elif (time_decision == "Hours"):
    hours_input = input("How many hours? ")
    hours = int(hours_input)
    minutes = hours * 60
    print(minutes)