import random, economy

p1 = economy.player("daniel", 1, 300)

def make_bet(p1):
    while True:
        gamble = input("Make a bet: ")
        if economy.player.check_balance(p1, gamble):
            break
    return gamble

def odd_or_even(p1, gamble):
    a = "odd"
    b = "even"
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
    
    x = random.randrange(1, 10)
    if x % 2 == 0 :
        print(f"{x} is EVEN!")
        b = "even"
    else:
        print(f"{x} is ODD!")
        b = "odd"
    
    if a != b:
        print("You lost!")
        economy.player.min_money(p1, gamble)
    else:
        print("You win!")
        economy.player.add_money(p1, gamble)

odd_or_even(make_bet(p1))
    


