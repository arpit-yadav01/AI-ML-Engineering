print("we are guessing the number")

secret_number =7

guess = int(input("enter the number between 1 to 10"))

if(guess== secret_number):
    print("you guess the correct number")
else:
  print ("you guess the wrong number")
  print("The correct number was:", secret_number)       