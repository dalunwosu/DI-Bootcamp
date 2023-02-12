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

#Exercise 4
class Zoo:
    def __init__(self,zoo_name):
        self.animals = []
        self.zoo_name = zoo_name
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} is already in the zoo")
        print(self.animals)
    def get_animals(self):
        animal = " ,".join(self.animals)
        print(animal)
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} is not in the zoo")
        print(self.animals)
    def sort_animals(self):
        animal_dict = {}
        for animal in sorted(self.animals):
            first_letter = animal[0]
            if first_letter in animal_dict:
                animal_dict[first_letter].append(animal)
            else  :
                animal_dict[first_letter] = [animal]
        return animal_dict
    def get_groups(self):
        animal_dict = self.sort_animals()
        for letter, animals in animal_dict.items():
            animal_str = ", ".join(animals)
            print(f"{letter}: {animal_str}")
    
ramat_gan_safari = Zoo("Dalu's Zoo")   
ramat_gan_safari.animals = ["Lion","Elephant","Giraffe","Gorilla","Tiger","Monkey","Alligator","Aardvark","Horse","Zebra"]
ramat_gan_safari.add_animal("Cheetah")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Horse")
ramat_gan_safari.sell_animal("Turtle")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()