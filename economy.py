class player:
    def __init__(self, name, level, money):
        self.name = name
        self.level = level
        self.money = money
    def add_money(self, amount):
        self.money += amount
    def min_money(self, amount):
        self.money -= amount
    def check_balance(self, amount):
        if amount > self.money or self.money <= 0:
            print(f"You don't have enough to play!")
            print(f"Final balance: ${self.money}")
            return False
        return True
    
def create_player():
    p1 = player(
        name = input("What is your name? "),
        level = 1,
        money = 300
    )
    return p1

def check_account(p1):
    try:
        p1.name
        print("Account Exists!")
        print(f"Current balance: ${p1.money}")
    except:
        print("Account doesn't exist, creating account...")
        return create_player(p1)

def make_bet(p1):
    while True:
        try:
            gamble = int(input("Make a bet: "))
            if gamble <= 0:
                print("Nice try dipshit")
                continue
            elif p1.check_balance(gamble):
                break
        except ValueError:
            print("Please enter a valid number.")
    return gamble

def win_lose(p1, result, gamble):
    if result == False:
        print(f"You lost! -{gamble}")
        p1.min_money(gamble)
    else:
        print(f"You win! +{gamble}")
        p1.add_money(gamble)
    print(f"Remaining balance: {p1.money}")

# Debugging
#p1 = player("daniel", 1, 300)
#win_lose(p1, False, 200)
#win_lose(p1, True, 100)