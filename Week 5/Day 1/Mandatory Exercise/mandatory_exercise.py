# Exercise 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Poppy", 2)
cat2 = Cat("Max", 8)
cat3 = Cat("Pickles", 6)


def check_age(*cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    print(
        f"The oldest cat is {oldest_cat.name}, and he/she is {oldest_cat.age} years old.")


check_age(cat1, cat2, cat3)

# Exercise 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!")


davids_dog = Dog("Rex", 50)
print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup",20)
print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()
if davids_dog.height > sarahs_dog.height:
    print(davids_dog.name)
elif sarahs_dog.height > davids_dog.height:
    print(sarahs_dog.name)

#Exercise 3
class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway= Song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()
chamber_of_reflections = Song(["Spend some time away","Getting ready for the day you're born again","Spend some time alone","Understand that soon you'll run with better men",
"Alone again","Alone again","Alone again","Alone again","Alone","No use looking out","It's within that brings that lonely feeling","Understand that when you leave here, you'll be clear",
"Among the better men","Alone again","Alone again","Alone again","Alone again","Alone","Alone again","Alone again","Alone again","Alone"])
chamber_of_reflections.sing_me_a_song()

#Exercise 4
class Zoo:
    def __init__(self,zoo_name):
        