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
        if amount > self.money:
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
        gamble = input("Make a bet: ")
        if player.check_balance(p1, gamble):
            break
    return gamble

p1 = ("daniel", 1, 300)
make_bet(p1)