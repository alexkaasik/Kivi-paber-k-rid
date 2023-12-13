from random import randint

P1score = 0
P2score = 0
Round = 0

while (True):
    try:
        Rounds = int(input("Put how many rounds: "))
        break
    except:
        pass

print('')

print("c = Player vs computer")
print("2 = Player vs player")
print("q = Quit")

while (True):
    pick0 = str(input("what will u do?: "))
    if pick0.lower() == "q":
        exit()
    elif pick0.lower() == "c" or pick0.lower() == "2":
        break
    else:
        print("pick a valid option")

print("")

while ( Round <= Rounds):

    pick1 = ["Kivi","Paber","Käärid"]

    Pick1Player=5
    Pick2Player=5

    print("1 = Kivi")
    print("2 = Paber")
    print("3 = Käärid")

    while True:
        try:
            Pick1Player = int(input("Player 1 give a option: "))-1
        except:
            pass

        if Pick1Player < 3 and not (Pick1Player < 0):
            break

        print("try again")

    while True:
        try:
            if pick0.lower() == "c":
                Pick2Player = randint(0,3)
            else:
                Pick2Player = int(input("Player 2 give a option: "))-1
        except:
            pass

        if Pick2Player < 3 and not (Pick2Player < 0):
            break

        print("try again")

    x = int( Pick1Player - Pick2Player )

    if x == 0:
        print("tie")
        print("try again")
        continue
    elif x == 1 or x == -2:
        print("player 1 won\n")
        P1score+=1
    elif x == -1 or x == 2:
        print("player 2 won\n")
        P2score+=1
    
    Round+=1
    
print(f"Score: P1={P1score}points, P2={P2score}points")