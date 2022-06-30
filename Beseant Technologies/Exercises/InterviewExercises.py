import math

def squareRoot():

    n = float(input("Enter a real number: "))
    print(n)
    squareRoot.sqroot = 0
    def formula(n1):
        g = n1/2
        a = g-(((g*g)-n1)/(2*g))
        print(a)
        i=0
        while(i<9):
            g=a
            a=g-(((g*g)-n1)/(2*g))
            print(a)
            i = i+1
        squareRoot.sqroot = a

    formula(n)
    if(math.sqrt(n) == squareRoot.sqroot):
        print("Values are matching, Code is correct")
    else:
        print("Code is wrong")

def greatName():

    name = input("Enter your name: ").strip().upper()
    j=0
    for x in name:
        if((j<len(name)-1) and (ord(name[j]) > ord(name[j+1]))):
            print("{} is not a great name".format(name.capitalize()))
            break
        j = j+1
    else:
        print("{} is a Great name".format(name.capitalize()))

def garden(garden):
    print(garden.replace(" ", "").count("@B"))

def interleave(string1,string2):
    final = ""
    if(len(string1) == len(string2)):
        i=0
        for x in string1:
            final = final + string1[i]+string2[i]
            i = i+1
        print(final)
    else:
        print("Not a equal string")

def worms(worm):
    i = 0
    count = 0
    for x in worm:
        if((worm[i] == "o") and (worm[i+1] != "o")):
            count = count + 1
            #print(count)
        i = i+1
        if((i == len(worm)-1) and (worm[i] == 'o')):
            count = count+1
            break
    print(count)

#squareRoot()
#greatName()
#garden("@B @ @ ")
#garden("@  B@")
#garden("@B@B@B")
#garden("")
#interleave("abc","def")
#interleave("111111","222222")
#interleave("123","4")
worms("ooo ooo")
worms("oo oo oo oo")
worms("  ")
worms("  o oo ooooo o o ")
