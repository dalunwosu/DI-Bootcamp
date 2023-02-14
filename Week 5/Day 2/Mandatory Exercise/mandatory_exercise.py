#Exercise 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    pass
if __name__ == "__main__":
    bengal = Bengal("Benjy",4)
    chartreux = Chartreux("Charlie",8)
    siamese = Siamese("Sammy",6)

    all_cats = [bengal,chartreux,siamese]

    sara_pets = Pets(all_cats)
    sara_pets.walk()

#Exercise 2
class Dog:
    def __init__(self,name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f"{self.name} is barking"
    def run_speed(self):
        speed = (self.weight/self.age)*10
        print(f"{self.name}'s running speed is {speed}Km/hr")
    def fight(self,other_dog):
        if (self.weight**2/self.age)*10>(other_dog.weight**2/other_dog.age)*10:
            print(f"{self.name} won the fight ")
        else:
            print(f"{other_dog.name} won the fight")

if __name__ == "__main__":
    tom = Dog("Tom",5,20)
    angela = Dog("Angela",3,15)
    brandy = Dog("Brandy",10,25)
    tom.bark()
    angela.bark()
    brandy.bark()
    tom.run_speed()
    angela.run_speed()
    brandy.run_speed()
    tom.fight(angela)
    brandy.fight(tom)
    angela.fight(brandy)





