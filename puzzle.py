"""
Title: Word Puzzle
Date: September/17/2019
Author: Dhiraj Meenavilli
"""
import random

list_of_words = ('apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango')
word = list_of_words[0]
puzzle = word[1:]
print("_"+puzzle)
def main():
	letter_guess = input("What do you think the correct letter is. ").lower()
	return letter_guess

letter_guess = main()

if letter_guess == word[0]:
	print("Congratulations you guessed the word ", word)
else:
	print("Not quite the correct word was ", word)
