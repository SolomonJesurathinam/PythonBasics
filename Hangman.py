import random
import re
count = 0

def hangman():
    global count
    if count == 1:
        print("   ----- \n"
              "  |     | \n"
              "  |       \n"
              "  |       \n"
              "  |       \n"
              "  |       \n"
              "__|__\n")
    elif count == 2:
        print("   ----- \n"
              "  |     | \n"
              "  |     | \n"
              "  |       \n"
              "  |       \n"
              "  |       \n"
              "__|__\n")
    elif(count == 3):
        print("   ----- \n"
              "  |     | \n"
              "  |     | \n"
              "  |     | \n"
              "  |       \n"
              "  |       \n"
              "__|__\n")
    elif(count == 4):
        print("   ----- \n"
              "  |     | \n"
              "  |     | \n"
              "  |     | \n"
              "  |     O \n"
              "  |       \n"
              "__|__\n")
    elif(count == 5):
        print("   ----- \n"
              "  |     | \n"
              "  |     | \n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "__|__\n")
    elif(count == 6):
        print("   ----- \n"
              "  |     | \n"
              "  |     | \n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \  \n"
              "__|__\n")
        print("You failed")
        print("The color is "+randomColors)
        quit()


colors = ["blue", "green", "brown", "grey", "red", "white", "pink", "yellow", "black", "maroon", "purple", "orange",]
randomColors = random.choice(colors)
#print(randomColors)
output = "-"*len(randomColors)
print("Guess the color "+output)
def game():
    global output
    global count
    indexes = ([m.start() for m in re.finditer(guessLetter, randomColors)])
    if guessLetter in randomColors:
        for index in indexes:
            output = output[:index] + guessLetter + output[index+1:]
    else:
        print("Enter again")
        count += 1
        hangman()
    print(output)

    if(output == randomColors):
        print("You won")
        quit()

while(True):
    guessLetter = input("Enter a character: ").lower()
    if(len(guessLetter) == 1):
        game()
    elif(len(guessLetter) == 0 or len(guessLetter) >=2):
        print("Enter a Letter")


