"""
Author: Dhiraj Meenavilli
Date: October/01/2019
Title: Word Puzzle Version 3
"""
import random
############ --------------- Variables --------------------- ##############
filename = 'instructions.txt'
is_win = False
num_guesses = 4
words = ['kiwi','bannana','feet','nine']
answear = words[random.randrange(4)]
puzzle = []
########### --------------- Functions ---------------------- ###############
def display_instructions(filename):
	instructions = open(filename,"r")
	instructions = instructions.read()
	print(instructions)

def display_puzzle_string(puzzle):
	print(" ".join(puzzle))

def get_guess(num_guesses):
	print("Guesses:", num_guesses)
	guess = input("What do you think the letters in this word are ")
	return guess


def update_puzzle_string(puzzle, answear, guess):
	update = 0
	for i in range(len(answear)):
		if guess == answear[i]:
			if puzzle[i] == guess:
				update = 0
			else:
				puzzle[i] = guess
				update = 1
	return update

def is_word_found(puzzle):
	complete = 1
	for i in range(len(puzzle)):
		if puzzle[i] == "_":
			complete = 0
	return complete

def display_results(is_win,answear):
	if is_win == True:
		print("Congratulations you succesfully guessed", answear)

	if is_win == False:
		print("Unfortunatley you've run out of guesses the answear was", answear)

def play_game(puzzle,answear,num_guesses):
	guess = get_guess(num_guesses)
	update = update_puzzle_string(puzzle,answear,guess)
	complete = is_word_found(puzzle)
	if complete == 1:
		return True,update
	else:
		return False,update

def main(puzzle,answear,num_guesses):
	display_puzzle_string(puzzle)
	is_win,update = play_game(puzzle,answear,num_guesses)
	return is_win,update

########### --------------- Program Starts Here ------------ ###############
for i in range(len(answear)):
	puzzle.append("_")

display_instructions(filename)

while num_guesses > 0 and is_win == False:
	is_win,update = main(puzzle,answear,num_guesses)
	if update == 0:
		num_guesses = num_guesses - 1
	if update == 1:
		num_guesses += 1

display_results(is_win,answear)
