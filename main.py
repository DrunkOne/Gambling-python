import economy, menu

p1 = economy.player("daniel", 1, 300)

#User Input
def select():
    while True:
        user_input = menu.select()
        match user_input:
            case 1:
                gamble()
                continue
            case 2:
                checkbal()
                continue
            case 3:
                print("Nah man no quiting")
                continue

# Selection Screen
def gamble():
    print("Selected gamble")

def checkbal():
    print("Selected check balance")
    economy.check_account(p1)

def quit():
    pass

menu.welcome()
select()



    