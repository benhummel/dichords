import random
import time

all_pitches = dict([
	(1, "A"),
	(2, "A#/Bb"),
	(3, "B"),
	(4, "C"),
	(5, "C#/Db"),
	(6, "D"),
	(7, "Eb"),
	(8, "E"),
	(9, "F"),
	(10, "F#/Gb"),
	(11, "G"),
	(12, "G#/Ab")
])

starting_pitch = ""
starting_pitch_index = 0
score = 0
round = 0

print("Clear your mind...")
time.sleep(1.25)
print("Remember, no chicken vision!")
time.sleep(1.25)

# choose game mode
def choose_mode():
	print("Choose your game mode:")
	time.sleep(.5)
	print("Easy (e), medium (m), or hard(h)?")
	mode = raw_input()
	return mode

modes = {
	"e": {
		"name": "easy",
		"num_steps_range": [1, 5],
		"possible_steps": [i for i in range(-4, 5) if i != 0],
		"score_multiplier": 1,
	},
	"m": {
		"name": "medium",
		"num_steps_range": [4, 9],
		"possible_steps": [i for i in range(-7, 8) if i != 0],
		"score_multiplier": 2,
	},
	"h": {
		"name": "hard",
		"num_steps_range": [8, 13],
		"possible_steps": [i for i in range(-11, 12) if i != 0],
		"score_multiplier": 3,
	}
}

mode = choose_mode()

if mode not in ["e", "m", "h"]:
	print("Whoops! That didn't work.")
	choose_mode()

print("You chose " + modes[mode]["name"] + ".")
num_steps_range = modes[mode]["num_steps_range"]
possible_steps = modes[mode]["possible_steps"]
score_multiplier = modes[mode]["score_multiplier"]

keep_playing = 1

while keep_playing == 1:
	round = round + 1
	num_steps = random.randrange(modes[mode]["num_steps_range"][0], modes[mode]["num_steps_range"][1])
	time.sleep(.75)
	print("Here we go...")
	time.sleep(1.25)
	print("###############################")
	print("ROUND " + str(round))
	print("###############################")
	time.sleep(1.25)
	starting_pitch_index = random.randrange(0,11)
	starting_pitch = all_pitches[starting_pitch_index]
	print("Our starting pitch is " + starting_pitch + ".")
	time.sleep(1.25)
	print("And we go...")
	time.sleep(1.25)

	i = 0
	total_movement = 0
	while i < num_steps:
		this_step_index = random.randrange(len(possible_steps))
		this_step = possible_steps[this_step_index]
		if(this_step < 0):
			print("Down " + str(abs(this_step)) + "...")
		else:
			print("Up " + str(abs(this_step)) + "...")
		i = i + 1
		total_movement = total_movement + this_step
		time.sleep(.75)

	total_movement = total_movement % 12
	ending_pitch_index = (starting_pitch_index + total_movement) % 12
	ending_pitch = all_pitches[ending_pitch_index]
	time.sleep(2)
	print("...and we end on the note:")
	time.sleep(.75)
	for i in all_pitches:
		print str(i) + ": " + all_pitches[i]

	user_guess = input()
	if all_pitches[user_guess] == ending_pitch:
		score = score + (1*score_multiplier)
		print("###############################")
		print("Awesome job! Our ending pitch was indeed " + ending_pitch + ".")
		print("Your score is now " + str(score))
		print("###############################")
		time.sleep(.75)
	else:
		print("Oops! That's not right - our ending pitch was " + ending_pitch + ".")
		print("###############################")
		print("Your score is now " + str(score))
		print("###############################")
		time.sleep(.75)
	print("Want to keep playing?")
	time.sleep(.75)
	print("Yes: 1")
	print("No: 0")
	keep_playing = input()

print("###############################")
print("Game over!")
time.sleep(.75)
print("Rounds played: " + str(round))
time.sleep(.75)
print("Score: " + str(score))

