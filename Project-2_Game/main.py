import random
randNumber = random.randint(1,100)
userGuess = None
numOfGuess = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    numOfGuess += 1
    if (userGuess==randNumber):
        print("Hurrah!! You did it, Your guess is right!!")
    else:
        if(userGuess>randNumber):
            print("Your guess is wrong, Enter a smaller number")
        else:
            print("Your guess is wrong, Enter a larger number") 

if(numOfGuess<=5):
    print("Congratulations!! You are the Winner")    
else:
    print("Sorry, You Lose!! Better Luck Next Time")

print(f"The number is {randNumber}")
print(f"You did in {numOfGuess} guesses !! ")

with open('hiscore.txt', "r") as f:
    hiscore = int(f.read())
if(numOfGuess<hiscore):
    print("You have just broken the record!!")
    with open('hiscore.txt', "w") as f:
        f.write(str(numOfGuess))    
