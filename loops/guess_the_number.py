import random
secret_number = random.randint(1, 100)
attempts = 0

print("Guess a number between 1 and 100")
while True:
    guess = int(input("Your guess?"))
    attempts = attempts + 1 
    if guess < secret_number:
        print("my number is bigger")
    elif guess > secret_number:
        print("my number is smaller")
    else:
        print("WOW...you guessed right")
        print("your guesses:" + str(attempts))
        break 
