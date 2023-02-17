import random


class Game:
    def __init__(self):
        self.user = self.get_user_item()
        self.computer = self.get_computer_item()

    def get_user_item(self):
        choice = input("Choose Between Rock, Paper and Scissors: ")
        print("r for rock, p for paper, s for scissors")
        while choice not in ["rock", "paper", "scissors "]:
            choice = input(
                "Wrong Choice. Please Choose Between Rock, Paper and Scissors: ").lower()
        return choice

    def get_computer_item(self):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        return computer_choice

    def get_game_result(self):
        if self.user == "rock" and self.computer == "scissors" or self.user == "paper" and self.computer == "rock" or self.user == "scissors" and self.computer == "paper":
            return "Win"
        elif self.user == self.computer:
            return "Draw"
        else:
            return "Loss"

    def play(self):
        print(
            f"You chose: {self.user}. The computer chose: {self.computer}. Result: {self.get_game_result()}")
        return self.get_game_result()
