import random

def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False

print("computer's turn: snake(s),water(w) or gun(g)?")
randno=random.randint(1,3)
if randno==1:
    comp='s'
if randno==2:
    comp='w'
if randno==3:
    comp='g'
you=input("Your turn: snake(s),water(w) or gun(g)?")
a=game(comp,you)
print(f"computer chose {comp}")
print(f"you chose {you}")
if a==None:
    print("Tie!!")
elif a:
    printf("you win!!")
else:
    print("you loose!!")
