import random


def play_again():
    want_to_play = input("Would you like to play? Y or N: ")
    while want_to_play.upper() == "Y":
        start_game()
    else:
        print("Good bye!")
        exit()


user_name = input("What's your name?  ")


def start_game():
    print("Hello, {}! Nice to see you here. Hope you'll enjoy our Guessing Game!".format(user_name))
    attempt_number = 1
    number = random.randint(1, 10)
    try:
        solution = int(input("Guess the number between 1 and 10!  "))
    except ValueError:
        print("Sorry, it should be a number between 1 and 10.")
    if solution < 0:
        raise ValueError("Oops! Name a number between 1 and 10!  ")
    if solution > 11:
        raise ValueError("Hmm! We need a number between 1 and 10!  ")
    else:
        while solution != number:
            if solution <= number:
                print("It's higher!")
            else:
                print("It's lower!")
            solution = int(input("Try again! Guess the number between 1 and 10!  "))
            attempt_number += 1
        print("You've got it. It took {} attempts to guess the number.".format(attempt_number))
        play_again()


if __name__ == '__main__':
    start_game()
