from googletrans import Translator
translator = Translator()

french_words= ["Bonjour","mon ami", "Au revoir", "Bienvenue", "A bientôt","s'il vous plaît"]
translation = {}
for word in french_words:
    english = translator.translate(word, dest="en")
    translation[word] = english.text

print(translation)
#I don't know why bonjour is not being translated