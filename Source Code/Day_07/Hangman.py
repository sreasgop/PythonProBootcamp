# This version of Hangman will let the user guess till he finishes the entire word. 

import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["apple", "banana", "cherry", "strawberry", "guava", "grape", "blueberry", "jackfruit"]
word = random.choice(word_list)
placeholder = len(word) * "_"

print(word+"\n"+placeholder+"\n")
 

correct_letters = []

game_over = False

lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""  


    for letter in word: 
        if guess==letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(display)

    if "_" not in display: 
        print("You Won!")
        game_over = True

    if guess not in word: 
        lives -= 1
        print(f"Wrong Guess! Lives remaining: {lives}")
        if lives == 0:
            game_over = True
            print("Game Over! You Lose.")
    
    print(stages[lives])
