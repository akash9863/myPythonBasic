import random

def gameWin(comp,you):
    if comp=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True
    elif comp==you:
        return None
    

print("Computer's turn: Snake(s) or Water(w) or Gun(g) ? ")
randNo = random.randint(1,2)

if randNo==1:
    comp="s"
elif randNo==2:
    comp="w"
elif randNo==3:
    comp="g"

you=input("Your turn: Snake(s) or Water(w) or Gun(g) ? ")
a=gameWin(comp,you)

print(f"Copmuter choose: {comp}")
print(f"You choose: {you }")

if a== None:
    print("The game is a Tie !")
elif a:
    print("You WIN !!")
else: 
    print("You Loose")