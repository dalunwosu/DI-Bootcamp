matrix = [["7", "T", "h", "i", "s", "$", "#", "^"], ["i","3", "s", "%", "M", "a", "t", "r"], ["i", "x", "#", "%", "!"]]
letters = []
for thing in matrix:
    for object in thing:
        if object.isalpha():
            letters.append(object)
print(letters)
sentence = "".join(letters)
result = sentence[:4] + " " + sentence[4:6] + " " + sentence[6:]
print(result)



            


