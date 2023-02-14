import random
import string
from datetime import datetime
from faker import Faker

#Exercise 2
def choose(num):
    computer_number = random.randint(0, 100)
    if num == computer_number:
        print("Success! You put the correct number")
    else:
        print("Wrong number")
choose(75)

#Exercise 3 
print("".join(random.choices(string.ascii_letters,k=5)))

#Exercise 4
def today():
    print(datetime.now())
today()

#Exercise 5
def january():
   now = datetime.now()
   jan = datetime(2024,1,1)
   print(f"The first of January is {jan - now} hours away")
january()

#Exercise 6
def minutes(date_of_birth):
    birth = datetime.strptime(date_of_birth, "%d/%m/%Y")
    lived = datetime.now() - birth
    minutes_lived = int(lived.total_seconds()//60) 
    print(f"You have lived {minutes_lived} minutes so far")
minutes("14/11/2005")

#Exercise 7
def holiday():
    today = datetime.now()
    print(f"Today's date is {datetime.today()}")
    easter = datetime(2023,4,9)
    time = easter - today
    print(f"The time until the next holiday is {time} hours")
holiday()

#Exercise 8
def space_age(age_in_seconds):
    earth_year_in_seconds = 31557600
    earth_age = round(age_in_seconds/earth_year_in_seconds,2)
    planets = {
        "Earth": 1,
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132
    }
    age_on_planets = {planet: earth_age/ orbital_period for planet, orbital_period in planets.items()}
    print(age_on_planets)
space_age(1000000000)

#Exercise 9
fake = Faker()
users = []

def fake_stuff():
    user = {
        "name" : fake.name(),
        "address": fake.address(),
        "lanugage_code": fake.language_code()
    }
    users.append(user)
for i in range(5):
    fake_stuff()
print(users)