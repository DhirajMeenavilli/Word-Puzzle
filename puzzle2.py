"""
Author: Dhiraj Meenavilli
Date: Sept.27.2019
Title: Puzzle Version 2
"""
import random
correct = 0
list = ["kiwi","mango","pineapple","watermelon","goose"]
picked = list[random.randrange(5)]
display = []
word = []

for i in range(len(picked)):
	display.append("_")
	word.append(picked[i])

word = "".join(word)
display = " ".join(display)

print("Try and guess the word. You can guess one letter at a time. Each time you guess I will show you which letters have been correctly guessed and which letters are still missing. You will have 4 guesses to guess all of the letters. Good luck!")
print("The answear so far is",display)
def main():
	guess = input("Guess a letter: ").lower()
	return guess

guess = main()

display = display.split()

for i in range(len(word)):
	if guess == word[i]:
		correct = 1
		display[i] = guess

display = " ".join(display)

print("The answear so far is",display)

if correct == 1:
	print("Good job you found the word",word)

else:
	print("Not quite the correct word was",word)
