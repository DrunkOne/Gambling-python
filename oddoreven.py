import random, economy

def odd_or_even(p1):
    gamble = economy.make_bet(p1) # Queries gamble amount (Check bal) Returns gamble amount

    # Queries Input for Odd or Even
    while True:
        err = f"Incorrect Input"
        pick = input("Pick Odd or Even: ")
        if pick == "odd" or pick == "even" or pick == "Odd" or pick == "Even":
            print(f"You've picked: {pick}")
            if pick == "odd" or pick == "Odd":
                a = "odd"
            else:
                a = "even"
            break
        else:
            print(err)
            continue
    
    # Get random number
    x = random.randrange(1, 10)
    if x % 2 == 0 :
        print(f"{x} is EVEN!")
        b = "even"
    else:
        print(f"{x} is ODD!")
        b = "odd"
    
    # Win / Lose conditions
    if a != b:
        result = False
    else:
        result = True

    #economy player module
    economy.win_lose(p1, result, gamble)

# Debugging
p1 = economy.player("daniel", 1, 300)
while True:
    odd_or_even(p1)

