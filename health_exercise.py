name=input("Select from the list below\n1.Rohan\n2.Ravi\n3.Rohit\n")
diet=input("Enter Diet")

def gettime():
    import datetime
    return datetime.datetime.now()

with open("Rohan.Diet.txt","a") as f:
    f.write("\n"+str(gettime())+diet)