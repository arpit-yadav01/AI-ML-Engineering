print("lets error handling in the python")


nums1= int(input("enter the first number : "))
nums2= int(input("enter the second number : "))
operation = input("u can enter the operation { + , - , *, / }")

try:
    if(operation == "+"):
        print("addditions " , nums1+nums2)

    elif(operation == "-"):
     print("sbstraction " ,nums1 - nums2)

    elif(operation== "*" ):
     print("multiplication" , nums1*nums2) 
    elif(operation == "/"):
        print("divide" , nums1/ nums2)
    else:
        print("the put a invalid operation")

except ValueError:
    print("you put the wrong number")
except ZeroDivisionError:
    print("you are dividing number with zero")

except Exception as e:
    print("the number are invalid")        