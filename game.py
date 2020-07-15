#A number guessing game.
greeting= """
	      Hello.
	   Welcome to the 
	Number Guessing Game!!!

	   The rules are:
	guess the secret number 
	in less than 11 tries
	"""
print()
print()
print(greeting)
print()
print()
playerName= input("What is your name? >>>>").title()
print()
print()
print(f"{playerName}, we are glad to have you playing today!")
print()
print()
bestgame=11

def guessing_game():
	bestgame=11

	import random
	secretNumber= random.randint(1,100)
	# print(f"Shhhhh, the secretNumber is {secretNumber}.")
	tooLow=0
	tooHigh=100
	guessCount= 1
	guess= None
	while guess != secretNumber:
		userGuess = input("Guess a number between 0 and 100.  >>>")
		print()
		print()
		if userGuess.isdigit() ==False:
			print(f"Silly {playerName}, that's not a number!")
			print()
			print()
			userGuess
		else:
			if int(userGuess) < 1 or int(userGuess) > 99:
				print(f"Silly {playerName}, that's not a number between 0 and 100!")
				userGuess
			elif int(userGuess) > secretNumber and guessCount < 11:
				print(f"This was guess number {guessCount}.  Your guess was too high. Try again.")
				guessCount +=1
				print()
				print()
				
			elif int(userGuess) < secretNumber and guessCount < 11:
				print(f"This was guess number {guessCount}.  Your guess was too low.  Try again.")
				guessCount +=1
				print()
				print()
			elif guessCount == 11:
				print(f"""
	 	  Sorry, {playerName}, 
	You did not guess the secret number. 
  Because you already tried {guessCount} times, 
	     the game is over!
		""")
				break
				print()
				print()
			else: 	
				print(f"""
  Congratulations, {playerName}, 
{secretNumber} was the correct number 
and you got it in only {guessCount} tries!
	  You win!!!!  
	  Game over.
		""")
				break
	if guessCount < bestgame:
		bestgame=guessCount
	elif bestgame < 11:
		print(f"""
  Congratulations also on making the 
number 1 spot on the high score board!!
      You got the answer in only
          {guessCount} tries.
           Very impressive!!
	  """)
		print()
		print()
	elif bestgame==11:
		print(f"Play again to see if you can beat the game in {guessCount} tries!!!")
	else:
		print(f"This wasn't your best score though, play again to see if you can beat the game in {bestgame} tries!!!")
		print()
		print()
		print(f"Last game you guessed in {guessCount} tries.  See if you can beat that this time!")
		print()
		print()
	playAgain= input("Would you like to play again? Enter Y or N. >>>>>>")
	print()
	print()
	if playAgain.upper() == "Y":
		print()
		print()
		print(f"""
	Ok, {playerName}, try to beat your
	 best score in the Guessing Game!! 
     So far, best score is {guessCount} tries.
		""")
		print()
		print()
		guessing_game()
	elif playAgain.upper() == "N":
		print()
		print()
		print(f"Ok, {playerName}, thanks for playing the Guessing Game!!")
		print()
		print()
	else:
		print("That is not a valid input.")
		playAgain
guessing_game()
