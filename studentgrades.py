student = dict()
filename = open("/Users/Sravani/grades/student-grade-math.csv")
for lines in filename:
    studentname = lines.split(",")
    studentpop = studentname.pop(0)
    studentint = list(map(int, studentname))
    student[studentpop] = studentint
print(student)
filename.close()

grades = dict()
for name,grade in student.items():
    studentsum = sum(grade)/len(grade)
    grades[name] = studentsum
print(grades)


file = open("student.txt","w")
for stname,stgrade in grades.items():
   file.write(stname+ "=" +str(stgrade)+  "\n")
file.close()

