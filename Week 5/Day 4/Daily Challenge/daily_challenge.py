class Text:
    def __init__(self,text):
        self.text = text
        self.word_frequency = self.frequency()
    def frequency(self):
        text_lines = self.text.split(" ")
        frequency = {}

        for word in text_lines:
            word_strp = word.strip(',\n.?;!').lower()
            if word_strp not in frequency:
                frequency[word_strp] = 1
            else:
                frequency[word_strp] += 1
        return frequency
    def most_frequent_word(self):
        most_frequent = 0
        most_frequent_word = ""
        for word, frequency in self.word_frequency.items():
            if frequency > most_frequent:
                most_frequent_word = word
                most_frequent = frequency
        return (f"The most frequent word is '{most_frequent_word}' and it was repeated {most_frequent} times")
    def unique_words(self) -> list:
        return sorted(list(text_obj.word_frequency))

file_location = "Daily Challenge\stranger.txt"
text_stranger = ""
with open(file_location,"r")as file:
    text_stranger = file.read()

text_obj = Text(text_stranger)
print(text_obj.frequency())
print(text_obj.most_frequent_word())
print(text_obj.unique_words())

