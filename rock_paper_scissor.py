import random
def game():
    print("Welcome To Rock Paper Scissor Game :>")
    user_input=int(input("Enter your option: \n1.Rock \n2.Paper\n3.Scissor \n4.Exit\n"))
    process(user_input)
def process(ui):
    system_input=random.choice(range(1,4))
    if(ui==4):
        exit()
    else:
        if(ui==system_input):
            print("Match Draw")
            process(game())
        else:
            if(ui==1 and system_input==2 or ui==2 and system_input==3 or ui==3 and system_input==1 or ui==1 and system_input==2):
                print("Oops! You lose the game:<")
                process(game())
            else:
                print("Great You won the game:>")
                process(game())
game()
