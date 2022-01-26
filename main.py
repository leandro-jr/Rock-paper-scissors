# Rock, paper and scissors game.
from random import choice
from time import sleep

def rules(user):
    print("Rules:")
    print("At the end of the count, choose rock, paper or scissors.")
    print("Rock beats scissors.")
    print("scissors beats paper.")
    print("scissors beats rock.")
    print(f"If {user} and the computer choose the same, it's a draw.")
    print("You begin with 5 lives")
    print("Type 'exit' to quit the game.")
    print("Type 'help' to display the rules again.")
    print()


def who_won_game(user, pc_lives, user_lives):
    if pc_lives == 0:
        print("-" * 50)
        print()
        print(f"{user} won the game!!!")
        print()
        print("-" * 50)
        return 1
    elif user_lives == 0:
        print("-" * 50)
        print()
        print(f"The computer won the game!!!")
        print()
        print("-" * 50)
        return 1
    else:
        return 0


def who_won_round(user, user_choice: str, pc_choice: str) -> int:
    loose = f"{user} lost!"
    won = f"{user} won!"
    draw = "it's a draw"
    who_beats_who = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    if not user_choice in who_beats_who:
        print("You must choose rock, paper or scissors")
        return 0
    elif who_beats_who.get(user_choice) == pc_choice:
        print(won)
        return 1
    elif who_beats_who.get(pc_choice) == user_choice:
        print(loose)
        return -1
    else:
        print(draw)
        return 0


def playing(user: str):
    user_lives = 5
    pc_lives = 5
    game_choices = ("rock", "paper", "scissors")

    while True:
        ready = input("Ready!? [type 'y' to proceed]: ")
        if ready == 'y':
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("1")
            sleep(1)
            print("GO!")

            user_choice = input("Type rock, paper or scissors: ").lower()
            pc_choice = choice(game_choices)

            if user_choice == "exit":
                break
            elif user_choice == "help":
                rules(user)

            print(f"The computer choose {pc_choice}")
            result = who_won_round(user, user_choice, pc_choice)
            if result == 1:
                pc_lives -= 1
            elif result == -1:
                user_lives -= 1

            if who_won_game(user, pc_lives, user_lives) == 1:
                break
            else:
                print()
                print(f"{user} has {user_lives} lives left.")
                print(f"The computer has {pc_lives} lives left.")


def main():
    print("-" * 50)
    print()
    print("Welcome to Rock, paper and scissors game created by Leandro Almeida")
    print()
    print("-" * 50)

    user = input("Player's name: ")
    print(f"Hi, {user}. Let's see if you can beat me")
    print()

    rules(user)
    playing(user)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
