import random
# Exercise 1
# Way 1


def display_message():
    reason = "I am learning Python in this course"
    return reason


show = display_message()
print(show)
# Way 2


def display_message():
    print("I am learning Python in this course")


display_message()

# Exercise 2


def favorite_book(title):
    book = f"One of My favorite books is {title}"
    return book


story = favorite_book("Harry Potter")
print(story)
# Way 2


def favorite_book(title):
    print(f"One of My favorite books is {title}")


favorite_book("The godfather")

# Exercise 3
# Way 1


def describe_city(city, country="Nigeria"):
    geography = f"{city} is in {country}"
    return geography


location = describe_city("Abuja")
print(location)
# Way 2


def describe_city(city, country="Nigeria"):
    print(f"{city} is in {country}")


describe_city("Lagos")

# Exercise 4


def random_number(number):
    computer_number = random.randint(0, 100)
    if number == computer_number:
        print("Success! You put the correct number")
    elif number != computer_number:
        print("You failed. The two numbers are not the same")
        print(
            f"Your number is {number}, the computer's number is {computer_number}")


random_number(81)

# Exercise 5


def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text is {text}")


make_shirt("small", "Wubulubbadubdub")


def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")


make_shirt()
make_shirt("medium")
make_shirt("XL", "I'm Pickle Riiiiiiiick!!")

# Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians():
    for name in magician_names:
        print(name)


show_magicians()


def make_great():
    for i, name in enumerate(magician_names):
        magician_names[i] = f"The Great {name} "


make_great()
show_magicians()

# Exercise 7


def get_random_temp():
    temp = random.randint(-10, 40)
    return temp


heat = get_random_temp()
# print(heat)


def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
# main()


def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat")
    elif 16 <= temp <= 23:
        print("The weather is fine go have fun!")
    elif 24 <= temp <= 32:
        print("The weather is perfect! Go outside and have sonme fun")
    elif 32 <= temp <= 40:
        print("The weather is quite hot, don't don't forget to stay hydrated")


main()


def get_random_temp(season):
    if season == "winter":
        return random.randint(-10, 16)
    elif season == "autumn" or season == "fall":
        return random.randint(16, 23)
    elif season == "spring":
        return random.randint(24, 32)
    elif season == "summer":
        return random.randint(32, 40)


def main():
    season = input("Give me a season of the year: ").lower()
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat")
    elif 16 <= temp <= 23:
        print("The weather is fine go have fun!")
    elif 24 <= temp <= 32:
        print("The weather is perfect! Go outside and have some fun")
    elif 32 <= temp <= 40:
        print("The weather is quite hot, don't don't forget to stay hydrated")


main()
