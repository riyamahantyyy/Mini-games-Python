import random
randomno=random.randint(1,100)
#print(randomno)
guess=0
USER= None

while(USER!=randomno):
    USER=int(input("enter your guess: "))
    guess+=1
    if(USER==randomno):
        print("yupieee!!correct guess!!")
    else:
        if(USER > randomno):
            print("oups!!enter a smaller number")
        else:
            print("oups!!enter a larger nummber")
 
print(f"you guessed the number in {guess} guesses")
with open("hiscore.txt","r")as f:
    hiscore = int(f.read())

if(guess<hiscore):
    print("you have just broken the high score!")
    with open("hiscore.txt","w")as f:
        f.write(str(guess))
