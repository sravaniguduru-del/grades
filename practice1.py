def loadScoresFromFile(fileName):
    csvFileHanlde = open(fileName, 'r')
    scores = readScoresForAllStudents(csvFileHanlde)
    csvFileHanlde.close()
    return scores
# this function takes file handle and reads scores for each student from file
# calls readSingleStudentScores for each like item in the file
#Input - File handle
#output - Dictionary of student scores in the following format
#         {'name', [22, 44, 45, 67, 56, 67, 78, 89, 98 17]}
def readScoresForAllStudents(csvFile):
    studentScores = dict()
    for record in csvFile:
        name, values = readSingleStudentScores(record)
        studentScores[name] = values
    return studentScores
# function to read grades of a student into a an arry
# this fucntion return student name and array of grades
#
#input - String, Single line from CSV file. Each line supposed to have 
#eleven comma seprated values, a name followed by scores from 10 tests
def readSingleStudentScores(csvRecord):
    values = csvRecord.strip().split(',')
    name = values.pop(0)
    #scoreList = list()
    #for value in values:
    #   scoresList.append(str(value))
    #return name, scoresList
    
    return name, list(map(int, values))
#this finction takes dictionary of student scores and calculate grade for each 
#student. Grade is average of scores from 10 tests
#Input - Dictionary of scores, Key is student name abd value, an arry for 10 
#scores
#output - New dictionary with student name and single grade
#         ['name', 56] format
def computeGradesFromScores(scores):
    grades = dict()
    for name, values in scores.items():
        grade = sum(values)/len(values)
        grades[name] = grade
    return grades
def writeGradesToFile(gradesFileName, grades):
    gradesFileHanlde = open(gradesFileName, 'w')
    for name, grade in grades.items():
        gradesFileHanlde.write(name + ',' + str(grade) + '\n')
    #gradesFileHanlde.write(str(grades))
    gradesFileHanlde.close()
#finally the starting point for the programs
#calls the main funtion by passing math scores csv file name
scores = loadScoresFromFile("/Users/Sravani/grades/student-grade-math.csv")
grades = computeGradesFromScores(scores)
print(grades)
writeGradesToFile('studentst-grades-math.txt', grades)
#we can call t
#scores = loadScoresFromFile('student-grades-physics.csv')
#grades = computeGradesFromScores(scores)
#print(grades)
