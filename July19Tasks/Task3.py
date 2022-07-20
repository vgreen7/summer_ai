#Task 3: Write a program that lets the user type a word and prints how many letters are in that word.

word_input = input("What is your word? ")

letter_count = 0

for i in word_input:
    letter_count += 1

print(letter_count)