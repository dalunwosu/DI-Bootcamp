from game import Game


def get_user_menu_choice():
    while True:
        print(f"""Choose one of the options below: \n p to play\n r to display results\n q to quit""")
        player_choice = input("Choose an option: ")
        if player_choice in ["p", "r", "x", "q"]:
            return player_choice
        else:
            print("Invalid choice. Please try again")


def print_results(results):
    print("Thank you for playing!")
    print("Results:")
    print(f"Wins: {results['win']}, Losses: {results['loss']}, Draws: {results['draw']} ")


def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "p":
            game = Game()
            result = game.play()
            if result == 'Win':
                results['win'] += 1
            elif result == 'Loss':
                results['loss'] += 1
            else:
                results['draw'] += 1
        elif choice == "r":
            print_results(results)
        elif choice == "q":
            print_results(results)
            break


main()
