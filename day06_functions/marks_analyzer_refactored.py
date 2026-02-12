# print("students marks using the function")

# def get_marks():
#   marks=[]
#   for i  in range (5):
#     mark= int(input(f"the marks wil be {i+1}  "))

#     marks.append(mark)

#   return marks

# def calculate_total(marks):
#     return sum(marks)

# def average(total, count):
#    return total/count

# def highest(marks):
#    return max(marks)

# def lowest (marks):
#    return min(marks)


# marks = get_marks()
# total = calculate_total(marks)
# avg = average(total, len(marks))

# print("\nAll Marks:", marks)
# print("Total:", total)
# print("Average:", avg)
# print("Highest:", highest(marks))
# print("Lowest:", lowest(marks))


print("the student marks using the function ")

def get_marks():
    marks=[]
    for i in range (5):
        mark = int(input(f"enter the marks {i+1}  "))
        marks.append(mark)

    return marks   


def totalmarks(marks):
    return sum(marks)

def averagemarks(total, count ):
    return total/count

def highest(marks):
    return max(marks)

def lowest(marks):
    return min (marks )


marks =  get_marks()
total=  totalmarks(marks)
avg= averagemarks(total, len(marks))


print("\n ", marks )

print(" total marks " ,total )

print(" averge marks " , avg)

print(" maximum marks " , highest(marks))
print("lowest " , lowest(marks))
                  

