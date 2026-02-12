print("lets a report of students ")

def get_marks():
    marks=[]
    for i in range (5):
        mark= int(input(f"enter the marks {i+1}: "))
        marks.append(mark)
    return marks

def total_marks (marks):
    return sum(marks)

def averagemarks(total , count):
    return total/count

def highest (marks):
    return  max(marks)

def lowest(marks):
    return min(marks)


def assign_grade(avg):
    if(avg>=90):
        return "A"
    elif avg>=75:
        return "B"
    else: 
        return "C"



marks= get_marks()
total = total_marks(marks)
avg = averagemarks(total , len(marks))
grade= assign_grade(avg)
high= highest(marks)
low = lowest(marks)
print("\n " , marks )
print("total marks " , total)
print("average marks " , avg)
print("highest", high)
print ("lowest " , low) 
print("grade is " , grade)


report = f"""
----- MARKS REPORT -----
Marks: {marks}
Total: {total}
Average: {avg}
Grade: {grade}
"""

print(report)

# Save to file
with open("report.txt", "w") as file:
    file.write(report)

print("✅ Report saved to report.txt")