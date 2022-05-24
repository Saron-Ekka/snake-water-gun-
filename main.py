print("..........SNAKE WATER GUN..........")

def game():
    print("Do you want to play?")
    play= str(input()).lower()
    if play == "no":
        quit()
    elif play == "yes":
        print("okay! let's play :)")
    else:
        print("wrong input")
        game()
game()

print("how many times do you bet? ENTER ONLY INTEGER")
n = int(input())


print("S stands for SNAKE")
print("W stands for WATER")
print("G stands for GUN")

z=0

for i in range(n):
    import random

    a = random.randint(1, 3)
    if a == 1:
        comp = 's'
    elif a == 2:
        comp = 'w'
    elif a == 3:
        comp = 'g'

    print("Choose S | W | G ")
    player = str(input()).lower()
    print("Computer choosed " + comp )
    x = True
    if comp == 's':
        if player == 's':
            x = "tie"
        elif player == 'w':
            x = False
        elif player == 'g':
            x = True
        else:
            x=None
            print("wrong input!! one chance wasted")


    if comp == 'w':
        if player == 'w':
            x = "tie"
        elif player == 'g':
            x = False
        elif player == 's':
            x = True
        else:
            x =None
            print("wrong input!! one chance wasted")

    if comp == 'g':
        if player == 'g':
            x ="tie"
        elif player == 's':
            x = False
        elif player == 'w':
            x = True
        else:
            x = None
            print("wrong input!! one chance wasted")

    if x == True:
        z=z+1
        print("Player WON!  COMPUTER LOOSE")
    elif x == False:
        print("PLAYER LOOSE  COMPUTER WON!")
    elif x == "tie":
        print("Tie")


print("your total points is "+ str(z) + " out of " + str(n) + " chances.")







