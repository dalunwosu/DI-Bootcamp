# Exercise 1
word = input("Give me a word: ")
result = {}
for i, char in enumerate(word):
    if char in result:
        result[char].append(i)
        i += 1
    else:
        result[char] = [i]


print(result)
#Exercise 2
