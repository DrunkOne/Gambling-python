def welcome():
    print("Welcome to the Casino!")
    print("What do you want to do?")
    print("[1] Gamble? [2] Check Balance? [3] Quit?")
    print("--------------------------------------")

def select():
    while True:
        user_input = input("I want to: ")
        try:
            user_input = int(user_input)
        except:
            print("Fucking dumbass, I'm asking for a number not an essay.")
        else:
            if user_input > 0 and user_input < 4:
                break
            else:
                print("STUPID FUCK, BETWEEN 1 AND 3")
    return user_input