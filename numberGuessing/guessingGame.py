chance = 0
number = 9

while chance < 5:
    guess = int(input("Enter your guess: "))
    if(guess > number):
        print("Number is too high")
        chance = chance + 1
    
    elif(guess < number):
        print("Number too small")
        chance = chance + 1

    
    elif(guess == number):
        print("CONGRATULATIONS YOU WON")
        break

if not chance < 5:
    print("YOU LOSE, Your chances are over, TRY AGAIN")