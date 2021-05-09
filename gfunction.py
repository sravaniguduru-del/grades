def readStudentNames():
    studentScores = dict()
    file = open("student-grade-math.csv")
    for line in file:
        tokens = line.split(",")
        studentName = tokens.pop(0)
        scores = list(map(int,tokens ))
        studentScores[studentName] = scores
    file.close()
    return studentScores
    

def calculateGrades(studentDict):
    studentGrades = dict()
    for name,values in studentDict.items():
        grade = sum(values)/len(values)
        studentGrades[name] = grade
    return studentGrades


def writeGrades(studentGrades):
    file = open("student.txt","w")
    for stname,stgrade in studentGrades.items():
         file.write(stname+ "=" +str(stgrade)+  "\n")
    file.close()
scores = readStudentNames()
grades = calculateGrades(scores)
print(grades)
writeGrades(grades)




    

