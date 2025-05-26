import economy, menu, oddoreven 

# Selection Screen
def gamble():
    print("Selected gamble")
    print("Launching Odd or Even...")
    while True:
        oddoreven.odd_or_even(p1)
        cont = int(input("[1] Continue? or [2] Quit? "))
        if cont == 2:
            break

def checkbal():
    print("Selected check balance")
    economy.check_account(p1)

def quit():
    pass

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
                print("Fak U")
                break

# activate
p1 = economy.player("daniel", 1, 300)
menu.welcome()
select()



    