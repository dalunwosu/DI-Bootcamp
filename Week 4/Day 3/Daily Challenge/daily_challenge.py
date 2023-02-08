# Exercise 1
word = input("Give me a word: ")
i = 0
result = {}
for char in word:
    if char in result:
        result[char].append(i)
        i += 1
    else:
        result[char] = [i]
        i += 1
print(result)

# Second way 
word_s = input("Give me a word: ")
result_i = {}
for i, char in enumerate(word_s):
    if char in result_i:
        result_i[char].append(i)

    else:
        result_i[char] = [i]

print(result_i)
#Exercise 2
