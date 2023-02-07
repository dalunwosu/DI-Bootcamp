# Exercise 1
def create_dictionary(word):
    i = 0
    result = {}
    for char in word:
        if char in result:
            result[char].append(i)
            i += 1
        else:
            result[char] = [i]
            i += 1
    return result

word = input("Enter a word: ")
print(create_dictionary(word))

#Exercise 2
