from mandatory_exercise import Dog
import random
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    def train(self):
        self.bark()
        self.trained = True
    def play(self,*dog_names):
        print(f"{self.name}, {dog_names} all play together")
    def do_a_trick(self):
        tricks = [f"{self.name} does a barrel roll",f"{self.name} stands on his back legs",f"{self.name} shakes your hand",f"{self.name} plays dead"]
        if self.trained is True:
            print(random.choice(tricks))
Tommy = PetDog("Tommy",6,15)
Tommy.train()
Tommy.play("Becky","Cruz","Ripper","Ronny","Fred")
Tommy.do_a_trick()

