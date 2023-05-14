import random

# start Rock Paper Scissors game
print("The game has started, let's go!")

while True:
    
        # user input: r, p, s
        user = input('insert your option " Rock : r ", " Paper : p ", " Scissors : s ": ').lower()

        # import random library
        pc = random.choice(["r", "p", "s"])

        # Building logic game

        print(f"Player is : {user}")
        print(f"Pc is : {pc}")
        
        if user == "r" and pc == "s" or user == "p" and pc =="r" or user == "s" and pc == "p":
            print("is very good, you win")

        elif user == "s" and pc == "r" or user == "r" and pc =="p" or user == "p" and pc == "s":
            print("I'm sorry, pc won")

        elif user == pc:
            print("it's a tie")

        else :
            print('please insert your option " Rock : r ", " Paper : p ", " Scissors : s".' )

        repeat = input("Do you want to continue(y/n): ")
        if repeat == "n":
            break

print("Game exited")