import random

botList = ["R", "P", "S"]
comCount = 0
userCount = 0

print("*"*20 +" Welcome to Rock Paper Sccissors Game "+"*"*20 +"\n")
name = input("Please enter your name: ").strip().title();
print("Hi {}, Let's start the game \n".format(name))

def game():
    global comCount
    global userCount
    botValue = random.choice(botList)
    if(botValue == userValue):
        print("Computer value is {}".format(botValue))
        print("Game Tie\n")
    elif(botValue == "R" and userValue =="S"):
        print("Computer value is {}".format(botValue))
        print("I win\n")
        comCount += 1
    elif(botValue == "P" and userValue =="R"):
        print("Computer value is {}".format(botValue))
        print("I win\n")
        comCount += 1
    elif(botValue == "S" and userValue =="P"):
        print("Computer value is {}".format(botValue))
        print("I win\n")
        comCount += 1
    else:
        print("Computer value is {}".format(botValue))
        print("You win\n")
        userCount += 1

while(True):
    userValue = input("Choose any one: Enter only first lettter: [R]ocks, [P]apers, [S]cissors - ").strip().upper()
    if((userValue == "R") or (userValue == "S") or (userValue == "P")):
        print("\nGame started")
        game()
    elif(userValue == "EXIT"):
        break;
    else:
        print("Please enter a valid input or type exit to quit the game \n")

print("I won {} times and you won {} times".format(comCount,userCount))