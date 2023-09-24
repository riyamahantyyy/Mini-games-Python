import random

def game(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True
    elif comp=='p':
        if you=='s':
            return True
        elif you=='r':
            return False
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False

print("computer's turn: rock(r),paper(p) or scissor(s)?")
randno=random.randint(1,3)
if randno==1:
    comp='r'
if randno==2:
    comp='p'
if randno==3:
    comp='s'
you=input("Your turn: rock(r),paper(p) or scissor(s)?")
a=game(comp,you)
print(f"computer chose {comp}")
print(f"you chose {you}")
if a==None:
    print("Tie!!")
elif a:
    printf("you win!!")
else:
    print("you loose!!")
