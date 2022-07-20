found = False
number = 32
x = 0
while not(found):
 guess = int(input("Guess a number between 1 and 100: "))
 if guess == number:
   print("You guessed it! " +str(x)+ " incorrect tries!")
   found = True
 elif guess < number:
   print("Your guess is too low.")
   x = x+1
 else:
   print("Your guess is too high.")
   x = x+1