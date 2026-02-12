print("The student marks using the function")

def get_marks():
    marks = []
    for i in range(5):
        mark = int(input(f"Enter the marks {i+1}: "))
        marks.append(mark)
    return marks   

def totalmarks(marks):
    return sum(marks)

def averagemarks(total, count):
    return total / count

def highest(marks):
    return max(marks)

def lowest(marks):
    return min(marks)

# ✅ New Grading Function
def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    else:
        return "C"


marks = get_marks()
total = totalmarks(marks)
avg = averagemarks(total, len(marks))
grade = assign_grade(avg)

print("\nAll Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", avg)
print("Highest Marks:", highest(marks))
print("Lowest Marks:", lowest(marks))
print("Grade:", grade)
