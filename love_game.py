import random

x=random.randint(0,1000000)
y=input("Enter your gender - m or f\n")

if y=="m":
    if x%2==0 :
        print("Yes, she loves you")
    else:
        print("No, she doesn't love you")
elif y=="f":
    if x%2==0:
        print("Yes, he loves you very much")
    else:
        print("No, he doesn't")