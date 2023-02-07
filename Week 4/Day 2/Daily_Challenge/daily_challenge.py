# Exercise 1 
number = int(input("Give me a number: "))
length = int(input("Give me a length: "))
number_list = [number]
multiplier = 1
while len(number_list) < length:
    multiplier += 1
    multiple = number * multiplier
    number_list.append(multiple)
print(number_list)

# Exercise 2 
from ordered_set import OrderedSet
word = input("Enter a word: ")
word_set = OrderedSet(word)
new_word = "".join(word_set)
print("The new word without duplicate consecutive letters: " + new_word)

#correction
input_string = input("Give me a word: ")
result_string = input_string[0]
for char in input_string[1:] :
    if result_string[-1] != char:
        result_string += char
print("The new word without duplicate consecutive letters: " + result_string)