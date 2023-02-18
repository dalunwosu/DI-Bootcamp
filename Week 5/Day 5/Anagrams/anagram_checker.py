
class AnagramChecker:
    def __init__(self,list) :
        with open(list,"r") as f:
            text = f.readlines()
            for i in range(len(text)):
                text[i] = text[i].strip("\n").lower()
        self.list =  text

    def is_valid_word(self, word):
        return word.lower() in self.list()
    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    def get_anagrams(self,word):
        anagrams = []
        for item in self.list:
            if self.is_anagram(word,item):
                anagrams.append(item)
        return anagrams

