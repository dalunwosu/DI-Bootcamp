import random

# Exercise 1
file_location = "Mandatory Exercise\words.txt"


def get_words_from_file(file):
    with open(file, "r") as f:
        global order
        order = f.readlines()
        order = [word.replace("\n", "")for word in order]
        return order
        # The best place to store the data is in a list


get_words_from_file(file_location)


def get_random_sentence(length):
    sentence = ""
    for word in range(length):
        word = random.choice(order)
        sentence += " " + word
    sentence = sentence.lower()
    print(sentence)


def main():
    print(""""This program gets a list of words from a different file and prints a sentence, 
 the length of which is determined by the user. The words are gotten at random """)
    num = int(input("Give a number from 2 to 20: "))
    if 2 <= num <= 20:
        get_random_sentence(num)
    else:
        raise ValueError("Wrong Number")


main()
