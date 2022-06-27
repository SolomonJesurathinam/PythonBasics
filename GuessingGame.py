import random

count = 1
randomNum = 0
name = input("Hi Welcome to Number Guessing Game, Please type your name: ").strip()
greetings = "Hi {}, Lets start the game(yes/no): ".format(name)

def randomm():
    global randomNum
    randomNum = random.randint(1,11)
    #print(randomNum)
    global count
    count = 1

def numgame():
    global count
    while(True):
        usernum = input("Enter a random numer from 1 to 10: ").strip()
        if usernum.isdigit():
            usernum = int(usernum)
            if(usernum >0) and (usernum<11):
                if(randomNum < usernum):
                    print("Guessed number is larger, guess again")
                    count += count
                elif(randomNum > usernum):
                    print("Guessed number is smaller, guess again")
                    count = count + 1
                elif(randomNum == usernum):
                    print("Hoorrayyyy you guessed the number {} in {} count".format(str(usernum),str(count)))
                    break;
            else:
                print("Range is from 1 to 10, Lets start again\n")
        else:
            print("Enter a number \n")

while(True):
    gameBoolean = input(greetings)
    if(gameBoolean.lower() == "yes"):
        print("Game started")
        randomm()
        numgame()
    elif(gameBoolean.lower() == "no"):
        print("Thank you {}, Bye".format(name))
        break;
    else:
        print("Please enter yes/no")



