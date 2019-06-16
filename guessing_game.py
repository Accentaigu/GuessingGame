"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""


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
  number = random.randint(1,10)
  try:
      solution = int(input("Guess the number between 1 and 10!  "))
  except ValueError:
      print("Sorry, it should be a number between 1 and 10.")
  if solution <= 0:
      raise ValueError("Oops! Name a number between 1 and 10!  ")
  if solution >= 11:
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
    # Kick off the program by calling the start_game function.
    start_game()

  """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
