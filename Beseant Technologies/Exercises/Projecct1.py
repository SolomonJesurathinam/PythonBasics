from random import randint

FinalValue = 0

while(True):

    input("Press Enter to roll:")
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    add = roll1 + roll2
    maximum = max(roll1,roll2)

    FinalValue += maximum
    if(roll1==roll2):
        add1 = roll1+roll2
        print("You have rolled {} and {}. Score is {} ".format(roll1, roll2,add1))
        print("Total points is {}".format(FinalValue+roll1))
        break

    print("You have rolled {} and {}. Score is {} ".format(roll1, roll2, maximum))


