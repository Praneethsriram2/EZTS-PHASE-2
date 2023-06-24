stud_grade=[]
stud_grade.append((1,"Praneeth"))
stud_grade.append((4,"natraj"))
print(stud_grade)
stud_grade.sort(reverse=True)
print("Yes")
print(stud_grade)
stud_grade.append((3,"Ajay"))
stud_grade.append((2,"Nithin"))
print(stud_grade)
stud_grade.sort(reverse=True)
print(stud_grade)
while stud_grade:
    print(stud_grade.pop(),end=' ')