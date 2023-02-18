from anagram_checker import AnagramChecker
def get_valid_input():
    while True:
        user_input = input("Enter a word or type 'exit' to quit: ").strip()
        if user_input == 'exit':
            return None
        elif " " in user_input:
            print("Error: Only a single word is allowed.")
        elif not user_input.isalpha():
            print("Error: Only alphabetic characters are allowed.")
        else:
            return user_input.lower()

def display_anagrams(word, anagrams):
    print(f"\nYOUR WORD: {word}")
    if len(anagrams) == 0:
        print("No anagrams found.")
    else:
        print(f"This is a valid English word.")
        print(f"Anagrams for your word: {', '.join(anagrams)}.")

def main():
    dictionary = 'Anagrams\dictionary.txt'
    checker = AnagramChecker(dictionary)

    while True:
        user_input = get_valid_input()
        if user_input is None:
            break

        anagrams = checker.get_anagrams(user_input)
        display_anagrams(user_input, anagrams)

main()
