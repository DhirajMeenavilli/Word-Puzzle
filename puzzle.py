"""
Title: Word Puzzle
Date: September/17/2019
Author: Dhiraj Meenavilli
"""

word = '_iwi'
print(word)
letter_guess = input("What do you think the correct letter is. ").lower()

if letter_guess == 'k':
	print("Congratulations you guessed the word kiwi right.")
else:
	print("Not quite the correct word was kiwi")
