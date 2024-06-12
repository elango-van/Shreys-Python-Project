lst1=("Stone","Paper","Scissor")

import random

i=1
up=0
cmp=0

try:
    while i<=10:
        cmptr = random.choice(lst1)
        x=int(input("Choose from options:\n0.Stone 1.Paper 2.Scissor\n"))
        user=lst1[x]
        if user=="Stone" and cmptr=="Scissor":
            print("You won as you choose "+user+" vs "+cmptr)
            up=up+1
            print(f"Your Score: {up} vs Computer Score: {cmp}")
            i=i+1
        elif user=="Stone" and cmptr=="Paper":
            print("You lost as you choose "+user+" vs "+cmptr)
            cmp=cmp+1
            print(f"Your Score: {up} vs Computer Score: {cmp}")
            i=i+1
        elif user==cmptr:
            print("Draw as "+user+" is same as "+cmptr)
            print(f"Your Score: {up} vs Computer Score: {cmp}")
            i=i+1
        elif user=="Paper" and cmptr=="Stone":
            print("You won as you choose " + user + " vs " + cmptr)
            up=up+1
            print(f"Your Score: {up} vs Computer Score: {cmp}")
            i=i+1
        elif user=="Paper" and cmptr=="Scissor":
            print("You lost as you choose "+user+" vs "+cmptr)
            cmp=cmp+1
            print(f"Your Score: {up} vs Computer Score: {cmp}")
            i=i+1
        elif user=="Scissor" and cmptr=="Paper":
            print("You won as you choose " + user + " vs " + cmptr)
            up=up+1
            print(f"Your Score: {up} vs Computer Score: {cmp}")
            i=i+1
        elif user=="Scissor" and cmptr=="Stone":
            print("You lost as you choose "+user+" vs "+cmptr)
            cmp=cmp+1
            print(f"Your Score: {up} vs Computer Score: {cmp}")
            i=i+1

        if i==11:
            if up==cmp:
                print("It's a draw")
            elif up<cmp:
                print("Sorry, you lost this time. Try again.")
            else:
                print("Congrats, You are a winner. Wanna challenge me again?")

        if i==11:
            ask = input("Press y to exit or any other key to keep playing")
            if ask == "y":
                exit(input("Bye Bye"))
                break
            else:
                i = 1
except:
    print("Check code")