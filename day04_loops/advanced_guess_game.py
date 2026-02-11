print("guess the number")

secretnumber=6

attempt= 0
max_attemt=5

while max_attemt>attempt:
    guess= int(input("enter the number betweeb 1 ot 10 "))
    attempt+=1

    if(guess== secretnumber):
        print("you guess the correct number")
        break
    elif guess > secretnumber:
         print("to high")

    else:
        print ("too low")

    print("Attempts left:", max_attemt - attempt)

    if attempt== max_attemt and guess != secretnumber:  
        print("no more attempt is left ")
        print("game over " , secretnumber)
