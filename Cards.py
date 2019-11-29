import random
import sys
import time

Suits = "♠♣♥♦"
rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

Picks = []
picks = []
for i in range(0,52):
    picks.append(i)
    
    

for i in range(0,27):
    m = random.randrange(0,52-i,1)
    Picks.append(picks[m])
    del picks[m]
    


def typer(word):
    for c in word:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)   # Or whatever delay you'd like

def typerfast(word):
    for c in word:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)   # Or whatever delay you'd like


def splitter(D, d):
    for i in range(0,27):
        d[i%3].append(D[i])

def deal(deck, deckers, I):
    a = []
    b = []
    c = []
    A = [a,b,c]
    temp = []
    temp1 = []
    temp2 = []
    temp3 = []
    temps = [temp1,temp2,temp3]
    for i in range(0,27):
        if (i%3)==0:
            print()
        sys.stdout.write(deckers[i%3][i//3])
        A[i%3].append(deckers[i%3][i//3])
        sys.stdout.flush()
        #sys.stdout.write(", ")
        #sys.stdout.flush()
        time.sleep(0.2)
    print()
    print()
    typer("Which column's your card in?")
    print()
    typer("(Enter 1, 2, or 3.): ")
    num = int(input()) - 1
    d = A[num]
    del A[num]
    A.reverse()
    A.insert(I,d)
    for l in A:
        for i in l:
            temp.append(i)
    splitter(temp, temps)
    return temp, temps

typerfast(Suits*8)
print()
typer("Welcome to Nick's card show!")
print()
typerfast(Suits*8)
print()
print()
Deck = []
for i in range(0,27):
    k = Picks[i]
    Symbol = rank[k%13] + Suits[k//13]
    if len(Symbol)== 3:
        Symbol+=" "
    else:
        Symbol+="  "
    Deck.append(Symbol)

typer("Let's check the deck shall we.")
print()
for i in range(0,27):
    if (i%9)==0:
        print()
    sys.stdout.write(Deck[i])
    sys.stdout.flush()
    #sys.stdout.write(", ")
    #sys.stdout.flush()
    time.sleep(0.1)
print()
print()
typer("Pick a card friend.")
print()
typer("(hit enter when you've picked your card) ")
input()
print()
typer("Alrighty,")
time.sleep(0.1)
typer(" one more thing before we start.")
print()
time.sleep(0.7)
typer("What's your favourite number between 1 and 27?:")
target = int(input(" ")) - 1

o = target + 1
L = []
L.append(target//9)
target -= L[0]*9
L.append(target//3)
target -= L[1]*3
L.append(target)

L.reverse()



deck1 = []
deck2 = []
deck3 = []

decks = [deck1,deck2,deck3]

splitter(Deck, decks)
p = 0
Deck, decks = deal(Deck, decks, L[0])
Deck, decks = deal(Deck, decks, L[1])
Deck, decks = deal(Deck, decks, L[2])
print()
typer("Ok,")
time.sleep(0.1)
typer(" drum roll please.")
print()
print()
time.sleep(1)
for i in range(0,o-1):
    if i<9:
        typerfast(str(i+1) + ":  " + Deck[i])
    else:
        typerfast(str(i+1) + ": " + Deck[i])
    print()
    time.sleep((i/(2*o)) + 0.15)

print(".")
time.sleep(0.3)
print(".")
time.sleep(0.3)
print(".")
time.sleep(0.3)

typer("Was this your card?")
print()
time.sleep(0.3)
typer(str(o) +": " + Deck[o-1])
print()
ans = input()
print()
time.sleep(0.5)
if ans.lower() == "yes":
    typer(":)")
elif ans.lower() == "no":
    typer("Either you made a mistake or you're a liar.")
else:
    typer("I couldn't hard code every possible respone, ¯\_(ツ)_/¯.")
print()
time.sleep(5)





