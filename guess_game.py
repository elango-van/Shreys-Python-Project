# Dict = {"Quad":"Shape with 4 sides","Tri":"Shape with 3 sides",
#         "Pentagon":"Shape with 5 sides","Hexagon":"Shape with 6 sides"}
# var1=input("Please enter the word for obtaining it's meaning\n ")
# print(Dict[var1])

n=45
runno=1

while runno<=6:
    if runno==1:
        play=input("Lives- "+str(runno+4)+"\nGuess the no- ")
        runno=runno+1
    elif runno<=5:
        play = input("Lives left- " + str(6 - runno) + "\nGuess the no- ")
        runno=runno+1
    elif runno==6:
        print("Lives left- " + str(6 - runno)+"\nGame over!, Try again")
        play=input("Do you want to play again, if yes enter y. To exit press n- ")
        if play=="y":
            runno=1
        elif play=="n":
            print("Exit confirmed by user")
            break
    else:
        continue

    if play.isnumeric():
        if int(play)==n :
            print("Congratulations, you guessed it correct")
            play = input("Do you want to play again, if yes enter y. To exit press n- ")
            if play == "y":
                runno = 1
            elif play == "n":
                print("Exit confirmed by user")
                break
        elif int(play)>n:
            print("Decrease the no to guess it correct")
        elif int(play)<n:
            print("Increase the no to guess it correct")
        else:
            continue