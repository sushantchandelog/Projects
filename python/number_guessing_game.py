
import random

number = random.randint(1, 100)

print("Number Guessing Game")
print("I am Thinking of number between 1 to 100")

guess = int(input("Enter your Guess : "))

if guess == number:
  print("Correct ! You guessed the Number")
elif guess < number:
  print("Too low")
else:
  print('high')

print("The Number was :", number)

# using it with the While loop
print(f"Enter the Range of number to start the game")
START = int(input("Enter the Range : "))
END  = int(input("Enter the range : "))
number = random.randint(START , END)

print("Starting the Game")
print(f"Guess the number between {START} - {END}")

guess = 0

while guess != number:
  guess = int(input("Enter The guess Number: "))

  if guess < number :
    print("Try Again, LOW!")
  elif guess > number:
    print("Try Again , HIGH!")
  else:
    print("You Guessed the Number !")

print("Game Over And Number is", number)

