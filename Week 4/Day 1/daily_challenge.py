sentence = input("Give me a string 10 Characters Long: ") 
if len(sentence) < 10 :
    print("string not long enough")
elif len(sentence) > 10 :
    print("string too long")
else: 
    print(sentence[0] , sentence[9])

index = range(len(sentence))
for x in index :
    print(sentence[:x + 1])

import random
shuffle = ''.join(random.sample(sentence, len(sentence)))
print(shuffle)
