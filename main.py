
from Student import Student
from School import School
import random
import math
# Initialize 5 schools

# Loop 1000 times
# Initialize student
# Assign preferences to student

# Run mechanism

def initializeSchools(n):
    schoolsList = []
    for id in range(n):
        quality = random.uniform(0,1)
        school = School(id,quality)
        schoolsList.append(school)
    return schoolsList

def initializeStudents(n,schools):
    studentsList = []

    for id in range(n):

        type = True
        # if id < n/2:
        #     type = False

        student = Student(id,type,schools)
        studentsList.append(student)

    return studentsList
        # initialize
def bostonMechanism(schools,students):
    # while unassigned student exists
    # enumerate round number - k
    #   loop over schools
        # school pref dictionary = {}
            # get students with that school as kth choice
            #  store in dict {stud_id: dist_to_school}
        # set categories / asssign students
    studentAssignments = {}
    roundNum = 0
    while(unassignedStudents(students)): #assigning students to schools
        # print(roundNum)
        for school in schools:
            for student in students:
                # Getting student's kth preference
                if student.preferences[roundNum] == school.id and student.school is None:
                    if student.distances[school.id] < 0.25:
                        school.c1.append(student)
                    elif student.distances[school.id] < 0.5:
                        school.c2.append(student)
                    elif student.distances[school.id] < 0.75:
                        school.c3.append(student)
                    else:
                        school.c4.append(student)

            setStudents(school) #Assign students to the schools

            studentAssignments[school.id] = school.students
            # print(studentAssignments)
        roundNum += 1
    return studentAssignments

def setStudents(school):


    assignStudents = []

    # Category 1 Assignment
    if len(school.c1) <= school.spotsRemaining:
        school.students.extend(school.c1)
        school.spotsRemaining -= len(school.c1)
        assignStudents.extend(school.c1)
    elif school.spotsRemaining > 0:
        school.students.extend(school.c1[0:school.spotsRemaining])
        assignStudents.extend(school.c1[0:school.spotsRemaining])
        school.spotsRemaining -= len(school.c1[0:school.spotsRemaining])

        # school.spotsRemaining = 0

    # Category 2 Assignment
    if len(school.c2) <= school.spotsRemaining:
        school.students.extend(school.c2)
        school.spotsRemaining -= len(school.c2)
        assignStudents.extend(school.c2)
    elif school.spotsRemaining > 0:
        school.students.extend(school.c2[0:school.spotsRemaining])
        assignStudents.extend(school.c2[0:school.spotsRemaining])
        school.spotsRemaining -= len(school.c2[0:school.spotsRemaining])

        # school.spotsRemaining = 0

    # Category 3 Assignment
    if len(school.c3) <= school.spotsRemaining:
        school.students.extend(school.c3)
        school.spotsRemaining -= len(school.c3)
        assignStudents.extend(school.c3)
    elif school.spotsRemaining > 0:
        school.students.extend(school.c3[0:school.spotsRemaining])
        assignStudents.extend(school.c3[0:school.spotsRemaining])
        school.spotsRemaining -= len(school.c3[0:school.spotsRemaining])

        # school.spotsRemaining = 0

    # Category 4 Assignment
    if len(school.c4) <= school.spotsRemaining:
        school.students.extend(school.c4)
        school.spotsRemaining -= len(school.c4)
        assignStudents.extend(school.c4)


    elif school.spotsRemaining > 0:
        school.students.extend(school.c4[0:school.spotsRemaining])
        assignStudents.extend(school.c4[0:school.spotsRemaining])
        school.spotsRemaining -= len(school.c4[0:school.spotsRemaining])
        # school.spotsRemaining = 0

    setStudentSchool(assignStudents,school.id)
    school.c1 = []
    school.c2 = []
    school.c3 = []
    school.c4 = []

def setStudentSchool(students,schoolID):
    for student in students:
        student.school = schoolID


def unassignedStudents(students):
    for student in students:
        if student.school is None:
            # print(student)
            return True
    return False


if __name__ == "__main__":
    schools = initializeSchools(2)
    students = initializeStudents(5, schools)
    liarFrac = 0.1
    numSophisticated = int(math.ceil(len(students) * liarFrac))
    studentsSet = set(students)
    sophisticadStud = set(random.sample(studentsSet, numSophisticated))
    sincereStud = studentsSet - sophisticadStud
    allSchools = {}

    for school in schools:
        studentPrefs = [0 for i in range(len(schools))]
        for student in students:
            for i in range(len(student.prefNoRand)):
                if school.id == student.prefNoRand[i]:

                    studentPrefs[i] += 1
        allSchools[school.id] = studentPrefs
    print("allSchools = ", allSchools)








    # resultsBM = bostonMechanism(schools,students)
    # print(resultsBM)
    # for key, value in resultsBM.items():
    #     print("School ", key)
    #     for student in value:
    #         print("Student: ", student.id)
    #     print("\n")

    # resultsGS = galeShapley(schools,students)

    # Do something with results
