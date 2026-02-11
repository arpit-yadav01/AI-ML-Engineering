print("marks analyzer")

marks=[]

for i in range (5):
    mark= int(input("the marks{i+1}"))
    marks.append(mark)
    print("\nAll Marks:", marks)
    total = sum(marks)
    average= total/len(marks)

    print("Total Marks:", total)
    print("Average Marks:", average)

# Find highest & lowest
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))


#new lines