#A number guessing game.
def guessing_game():
	import random
	greeting= """
	      Hello.
	   Welcome to the 
	Number Guessing Game!!!"""
	print()
	print()
	print(greeting)
	print()
	print()
	playerName= input("What is your name? >>>>").title()
	print()
	print()
	print(f"{playerName}, we are glad to have you playing today")
	print()
	print()
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
			elif int(userGuess) > secretNumber:
				print(f"This was guess number {guessCount}.  Your guess was too high. Try again.")
				guessCount +=1
				print()
				print()
				
			elif int(userGuess) < secretNumber:
				print(f"This was guess number {guessCount}.  Your guess was too low.  Try again.")
				guessCount +=1
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
guessing_game()