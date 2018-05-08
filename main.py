
from Student import Student
from School import School
import random
import math
import copy
import pandas
import matplotlib.pyplot as plt
import numpy as np
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

def initializeStudents(n,schools,frac):
    studentsList = []

    for id in range(n):

        type = True
        # if id < n/2:
        #     type = False

        student = Student(id,type,schools)
        studentsList.append(student)
    students = studentsList
    # Separate sincere from sophisticated students
    liarFrac = frac
    numSophisticated = int(math.ceil(len(students) * liarFrac))
    studentsSet = set(students)
    sophisticatedStud = set(random.sample(studentsSet, numSophisticated))
    sincereStud = studentsSet - sophisticatedStud

    allSchools = {}


    # Calculate dictionary of (school: [total preference count])
    # {School 1: [Number 1st, Number 2nd,...], School 2: [Number 1st, Number 2nd,...], School 3: ...}
    # Used to determine sophisticated students preferences
    for school in schools:
        studentPrefs = [0 for i in range(len(schools))]
        for student in students:
            if student.priorities[school.id] == 1 or student.priorities[school.id] == 2:
                if school.id == student.prefNoRand[0]:
                    studentPrefs[0] += 1
                if school.id == student.prefNoRand[1]:
                    studentPrefs[1] += 1
        allSchools[school.id] = studentPrefs
    # print("allSchools = ", allSchools)
    #
    before = sophisticatedStud.copy()
    sophisticatedStud = setFakePreferences(sophisticatedStud, schools, allSchools)
    # print(sophisticatedStud)

    counter = 0

    # Iterate through sophisticated students
    # Update fakePreferences based on known data

    # sophisticatedStud = setFakePreferences(sophisticadStud,schools,allSchools)
    #
    allStudents = list(sophisticatedStud.union(sincereStud))

    return allStudents


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
                # Getting student's kth preferences
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

def bostonMechanismFake(schools,students):
    # while unassigned student exists
    # enumerate round number - k
    #   loop over schools
        # school pref dictionary = {}
            # get students with that school as kth choice
            #  store in dict {stud_id: dist_to_school}
        # set categories / asssign students
    studentAssignments = {}

    roundNum = 0
    # print("Entering BMFake")
    while(unassignedStudents(students)): #assigning students to schools
        # print(roundNum)
        for school in schools:
            for student in students:
                #print("roundNum = ", roundNum)
                # Getting student's kth preferences
                if student.type == True:
                    # print("using real prefs")
                    prefs = student.preferences
                else:
                    # print("using fake prefs")
                    #print(student.fakePreferences == student.preferences)
                    prefs = student.fakePreferences
                if prefs[roundNum] == school.id and student.school is None:
                    #print("pref checking ", prefs)
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
            #print(studentAssignments)
        roundNum += 1
    #print(studentAssignments)
    return studentAssignments

def setStudents(school):


    assignStudents = []

    # Category 1 Assignment
    if len(school.c1) <= school.spotsRemaining:
        school.students.extend(school.c1)
        school.spotsRemaining -= len(school.c1)
        assignStudents.extend(school.c1)
        #print("Adding 1", school.c1)
    elif school.spotsRemaining > 0:
        school.students.extend(school.c1[0:school.spotsRemaining])
        assignStudents.extend(school.c1[0:school.spotsRemaining])
        school.spotsRemaining -= len(school.c1[0:school.spotsRemaining])
        #print("Adding 1x", school.c1[0:school.spotsRemaining])
        # school.spotsRemaining = 0

    # Category 2 Assignment
    if len(school.c2) <= school.spotsRemaining:
        school.students.extend(school.c2)
        school.spotsRemaining -= len(school.c2)
        assignStudents.extend(school.c2)
        #print("Adding 2", school.c2)
    elif school.spotsRemaining > 0:
        school.students.extend(school.c2[0:school.spotsRemaining])
        assignStudents.extend(school.c2[0:school.spotsRemaining])
        school.spotsRemaining -= len(school.c2[0:school.spotsRemaining])
        #print("Adding 2x", school.c2[0:school.spotsRemaining])

        # school.spotsRemaining = 0

    # Category 3 Assignment
    if len(school.c3) <= school.spotsRemaining:
        school.students.extend(school.c3)
        school.spotsRemaining -= len(school.c3)
        assignStudents.extend(school.c3)
        #print("Adding 3", school.c3)
    elif school.spotsRemaining > 0:
        school.students.extend(school.c3[0:school.spotsRemaining])
        assignStudents.extend(school.c3[0:school.spotsRemaining])
        school.spotsRemaining -= len(school.c3[0:school.spotsRemaining])
        #print("Adding 3x", school.c3[0:school.spotsRemaining])

        # school.spotsRemaining = 0

    # Category 4 Assignment
    if len(school.c4) <= school.spotsRemaining:
        school.students.extend(school.c4)
        school.spotsRemaining -= len(school.c4)
        assignStudents.extend(school.c4)
        #print("Adding 4", school.c4)

    elif school.spotsRemaining > 0:
        school.students.extend(school.c4[0:school.spotsRemaining])
        assignStudents.extend(school.c4[0:school.spotsRemaining])
        school.spotsRemaining -= len(school.c4[0:school.spotsRemaining])
        #print("Adding 4x", school.c4[0:school.spotsRemaining])
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

def setFakePreferences(soph,schools,allSchools):
    # print(soph)

    changeCount = 0
    for student in soph:
        student.type = False
        currSchool = student.preferences[0]
        # print("Student's priorities = ", student.priorities)
        # print("Student's preferences = ", student.preferences)
        # print("School popularity = ", allSchools)
        # print("Curr school = ", currSchool)
        if student.priorities[currSchool] > 2:
            # print("Student not a priority")
            if allSchools.get(currSchool)[0] > schools[currSchool].spots:
                # print("Not enough spots")
                for j in range(1, len(student.preferences)):
                    testSchool = student.preferences[j]
                    # print("Priority at school ", testSchool, " is ", student.priorities[testSchool])
                    if student.priorities[testSchool] <= 2:
                        # print("Found school where a priority")
                        if allSchools.get(testSchool)[0] < schools[testSchool].spots:
                            # print("\n\nfound achievable school")
                            # print("j = " , j)
                            pref = student.preferences.copy()
                            student.fakePreferences[j] = pref[0]
                            student.fakePreferences[0] = pref[j]
                            #$print("Changed from",student.preferences, "to",student.fakePreferences)
                            changeCount += 1
                            break
    print("Number of sophisticated who changed =" , changeCount, "Out of", len(soph), "total")
    return soph



def clearSchools(schools):
    for school in schools:
        school.students = []
        school.spotsRemaining = school.spots
        school.c1 = []
        school.c2 = []
        school.c3 = []
        school.c4 = []
    return schools

def checkResults(BM, BMFake):
    changed = True
    bmIds = {}
    for key, value in BM.items():
        addArray = []
        for student in value:
            addArray.append(student.id)
        bmIds[key] = addArray
    bmFake = {}
    for key, value in BMFake.items():
        addArray = []
        for student in value:
            addArray.append(student.id)
        bmFake[key] = addArray
    print(bmIds)
    print(bmFake)
    for key, value  in bmIds.items():
        # print()
        # print(len(set(value)))
        # print(len(set(bmFake[key])))
        if set(value) != set(bmFake[key]):
            print("Honest values", sorted(set(value)))
            print("Fake values ", sorted(set(bmFake[key])))
            print(set(value) - set(bmFake[key]))
            changed = False


    return changed

def assignmentCount(assignments, students):
    numStudents = len(students)
    sum = 0
    for key,value in assignments.items():
        sum += len(value)
    # print("Sum = ", sum)
    if sum >= numStudents:
        return True
    else:
        return False

def updateStudents(allStudents, student, school, removeStud):
    for updatedStud in allStudents:
        if updatedStud.id == student.id:
            student.school = school.id
        if updatedStud.id == removeStud.id:
            updatedStud.id = None
    return allStudents

def schoolRejection(student,school, assignment,allStudents):
    # school checks where student stands in their priority list
    # if student is higher than ppl already in take students out and put this student in
    # else reject students
    # return new assignment list
    # print("School = ", school)

    priority = student.priorities[school.id]
    if school.spotsRemaining > 0:
        if school.id in assignment:
            assignment[school.id].append(student)
            student.school = school.id

        else:
            assignment[school.id] = [student]
            student.school = school.id
        return assignment,student, allStudents,1

    else:
        # print("IN ELSE")
        if priority == 1:
            # print("P1")
            for priorityList in [school.c4,school.c3,school.c2]:
                if len(priorityList) > 0:
                    studentToRemove = random.choice(priorityList)
                    print(len(assignment[school.id]))
                    assignment[school.id].remove(studentToRemove)
                    print(len(assignment[school.id]))
                    studentToRemove.school = None
                    # print("student.school before = ", student.school)
                    student.school = school.id
                    # print("student.school after = ", student.school)

                    allStudents = updateStudents(allStudents, student, school, studentToRemove)
                    school.students.remove(studentToRemove)
                    assignment[school.id].append(student)
                    print(len(assignment[school.id]))
                    return assignment,student, allStudents,0
                else:
                    student.rejectedFrom.append(school.id)
                    return assignment, student,allStudents,0

        elif priority == 2:
            # print("P2")
            for priorityList in [school.c4,school.c3]:
                if len(priorityList) > 0:
                    studentToRemove = random.choice(priorityList)
                    assignment[school.id].remove(studentToRemove)
                    studentToRemove.school = None
                    student.school = school.id
                    allStudents = updateStudents(allStudents, student, school, studentToRemove)
                    school.students.remove(studentToRemove)
                    assignment[school.id].append(student)
                    return assignment,student, allStudents,0
                else:
                    student.rejectedFrom.append(school.id)
                    return assignment, student,allStudents,0
        elif priority == 3:
            # print("P3")
            for priorityList in [school.c4]:
                if len(priorityList) > 0:
                    studentToRemove = random.choice(priorityList)
                    assignment[school.id].remove(studentToRemove)
                    studentToRemove.school = None
                    student.school = school.id
                    allStudents = updateStudents(allStudents, student, school, studentToRemove)
                    school.students.remove(studentToRemove)
                    assignment[school.id].append(student)
                    return assignment,student, allStudents,0
                else:
                    student.rejectedFrom.append(school.id)
                    return assignment, student,allStudents,0
        else:
            # Don't add anybody
            student.rejectedFrom.append(school.id)
            return assignment,student, allStudents,0


def getSchool(schools,id):
    for school in schools:
        if school.id == id:
            return school

def printAssignments(assignments):
    for key, value in assignments.items():
        print("School ", key)
        for student in value:
            print("Student: ", student.id)
        print("\n")


def galeShapley(schools, students):

    assignments = {}

    while(not assignmentCount(assignments,students)):
        # print("assignment at beginning: ", printAssignments(assignments))
        # for student in students:
        student = random.choice(students)
        if student.school == None:
            for i in range(len(student.preferences)):
                if student.type:
                    pref = student.preferences
                else:
                    pref = student.preferences
                if pref[i] not in student.rejectedFrom:
                    favSchool = pref[i]
                    favSchoolObject = getSchool(schools,favSchool)
                    # print("SCHOOL REJECTION", schoolRejection(student,favSchoolObject,assignments,students))
                    assignments,student,students,dec = schoolRejection(student,favSchoolObject,assignments,students)
                    # print("Current student: ",student.id)
                    # print("Current student REject list: ",student.rejectedFrom)
                    #
                    # print("assignment at end: ", printAssignments(assignments))

                    favSchoolObject.spotsRemaining -= dec
                    # print(assignments, "\n")
                    # print("student.school = ", student.school)
                    break

        # else:
            # print("Student already assigned")
    # print(assignments)
    # printAssignments(assignments)
    return assignments

def galeShapleyFake(schools, students):

    assignments = {}

    while(not assignmentCount(assignments,students)):
        # print("assignment at beginning: ", printAssignments(assignments))
        # for student in students:
        student = random.choice(students)
        if student.school == None:
            for i in range(len(student.preferences)):
                if student.type:
                    pref = student.preferences
                else:
                    pref = student.fakePreferences
                if pref[i] not in student.rejectedFrom:
                    favSchool = pref[i]
                    favSchoolObject = getSchool(schools,favSchool)
                    # print("SCHOOL REJECTION", schoolRejection(student,favSchoolObject,assignments,students))
                    assignments,student,students,dec = schoolRejection(student,favSchoolObject,assignments,students)
                    # print("Current student: ",student.id)
                    # print("Current student REject list: ",student.rejectedFrom)
                    #
                    # print("assignment at end: ", printAssignments(assignments))

                    favSchoolObject.spotsRemaining -= dec
                    # print(assignments, "\n")
                    # print("student.school = ", student.school)
                    break

        # else:
            # print("Student already assigned")
    # print(assignments)
    # printAssignments(assignments)
    return assignments

def isBetterOff(assignments):
    averageLiar = []
    averageTruthful = []
    for key, value in assignments.items():
        for student in value:
            if student.type == True:
                preference = student.preferences.index(key)
                averageTruthful.append(preference)
            else:
                preference = student.preferences.index(key)
                averageLiar.append(preference)

    if len(averageLiar) > 0 and len(averageTruthful) > 0:
        avgLiar = sum(averageLiar)/len(averageLiar)
        avgTruth = sum(averageTruthful)/len(averageTruthful)
        return avgLiar,avgTruth
    elif len(averageLiar) == 0 and len(averageTruthful) > 0:
        avgTruth = sum(averageTruthful)/len(averageTruthful)
        return 0,avgTruth
    elif len(averageLiar) > 0 and len(averageTruthful) == 0:
        avgLiar = sum(averageLiar)/len(averageLiar)
        return avgLiar,0
    else:
        return 0,0




def bordaCount(assignments):
    sum = 0
    numSchools = len(assignments.keys())
    for key, value in assignments.items():
        for student in value:
            preference = student.preferences.index(key)
            sum += (numSchools - preference-1)
            # print("Preference: ", preference, "Adding: ", (numSchools - preference-1))

    return sum

if __name__ == "__main__":
    # Initialization
    schools = initializeSchools(5)
    allStudents = initializeStudents(1000, schools, 1)
    #
    # gsSchools = copy.deepcopy(schools)
    # gsStudents = copy.deepcopy(allStudents)


    # Add check to BM to check sincere vs sophisticated
    # allStudentsCopy = copy.deepcopy(allStudents)
    # resultsBM = bostonMechanism(schools,allStudents)
    # borda = bordaCount(resultsBM)
    # print("Boston Borda: ", borda)
    # # print(resultsBM)
    # clearedSchools = clearSchools(schools)
    # # for key, value in resultsBM.items():
    # #     print("School ", key)
    # #     for student in value:
    # #         print("Student: ", student.id)
    # #     print("\n")
    # allStudentsCopy2 = copy.deepcopy(allStudents)
    # resultsFake = bostonMechanismFake(schools, allStudents)
    # bordaFake = bordaCount(resultsFake)
    # print("Boston Borda: ", bordaFake)
    # # for key, value in resultsFake.items():
    # #     print("School ", key)
    # #     for student in value:
    # #         print("Student: ", student.id)
    # #     print("\n")
    # same = checkResults(resultsBM, resultsFake)
    # print ("Results are the same = ", same)
    # print(resultsFake)
    #
    #

    #
    # averages = {}
    # difVals = {}
    # averagesSincere = {}
    # difValsSincere = {}
    # avgPref = []
    # avgPrefSincere = []
    # # liarFracs = np.linspace(0,1,25)
    # liarFracs = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    # schoolsNumber = [3,4,5,6,7,8]
    # schoolsNumber = 5
    # studentsNumber = np.linspace(100,1000,10)
    # # 0.25,0.5,0.75,1]
    # for j in studentsNumber:
    #     iterations = 10
    #
    #     runningSum = 0
    #     liar = []
    #     truth = []
    #
    #     runningSumSincere = 0
    #     liarSincere = []
    #     truthSincere = []
    #
    #     for i in range(iterations):
    #         # if i % 5 == 0:
    #         #     print ("Iteration: ", i)
    #
    #         schools = initializeSchools(schoolsNumber)
    #         allStudents = initializeStudents(int(j), schools, 0.33)
    #         schoolsCopy = copy.deepcopy(schools)
    #         allStudentsCopy = copy.deepcopy(allStudents)
    #
    #         bostonResults = bostonMechanismFake(schools,allStudents)
    #         # print("Assignment with sophisticated: ")
    #         # printAssignments(bostonResults)
    #         borda = bordaCount(bostonResults)
    #         runningSum += borda
    #         liarVal, truthVal = isBetterOff(bostonResults)
    #         liar.append(liarVal)
    #         truth.append(truthVal)
    #
    #         bostonResultsSincere = bostonMechanism(schoolsCopy,allStudentsCopy)
    #         # print("Assignment without sophisticated: ")
    #         # printAssignments(bostonResultsSincere)
    #         bordaSincere = bordaCount(bostonResultsSincere)
    #         runningSumSincere += bordaSincere
    #         liarValSincere, truthValSincere = isBetterOff(bostonResultsSincere)
    #         liarSincere.append(liarValSincere)
    #         truthSincere.append(truthValSincere)
    #     averages[j] = runningSum/(iterations*j)
    #     finalLiar = sum(liar)/len(liar)
    #     finalTruth = sum(truth)/len(truth)
    #     listVals = [finalLiar, finalTruth]
    #     difVals[j] = listVals
    #
    #     averagesSincere[j] = runningSumSincere/iterations
    #     finalLiarSincere = sum(liarSincere)/len(liarSincere)
    #     finalTruthSincere = sum(truthSincere)/len(truthSincere)
    #     listValsSincere = [finalLiarSincere, finalTruthSincere]
    #     difValsSincere[j] = listValsSincere
    #
    #     # df.to_csv('resultsGS' + str(j) + '.csv')
    # print("Boston Mechanism averages for fake: ", averages)
    # print("How much better of BM: ", difVals)
    # print()
    # print("ALL SINCERE: Boston Mechanism averages for fake: ", averagesSincere)
    # print("ALL SINCERE: How much better of BM: ", difValsSincere)
    #
    # avgFake = averages.values()
    # print(avgFake)
    # print(schools)
    # plt.scatter(studentsNumber,avgFake)
    # plt.title("Social Utility (Measured via Borda Count)")
    # plt.xlabel("Number of Students")
    # plt.ylabel("Borda Count")
    # plt.show()

    # avgPrefsSincere = np.asarray(list(difValsSincere.values()))
    # avgPrefs = np.asarray(list(difVals.values()))
    # print(np.shape(avgPrefsSincere[:,0]))
    # print(avgPrefsSincere)
    # plt.scatter(liarFracs,avgPrefs[:,0],s=20,label="Average Liar Preference")
    # plt.scatter(liarFracs,avgPrefsSincere[:,0],s=20,label="Average Sincere Preference")
    # plt.title("Average preferences")
    # plt.xlabel("Liar fraction")
    # plt.ylabel("Average")
    # plt.legend()
    # plt.show()

    schoolsNumber = [3,4,5,6,7,8]


    averages = {}
    averagesFake = {}
    difVals = {}
    difValsFake = {}
    liarFracs = np.linspace(0,1,20)
    studentsNumber = np.linspace(0,1000,10)
    for j in studentsNumber:
        runningSum = 0
        runningSumFake = 0
        iterations = 5
        # df = pandas.DataFrame(columns=['Iteration', 'Liar Fraction', 'Borda Result'])
        # df['Iteration'] = list(range(iterations))
        # df['LiarFrac'] = [j] * iterations
        for i in range(iterations):
            if i % 10 == 0:
                print ("Iteration: ", i)

            schools = initializeSchools(5)
            allStudents = initializeStudents(int(j), schools, 0.33)
            schoolsCopy = copy.deepcopy(schools)
            allStudentsCopy = copy.deepcopy(allStudents)

            # All Sincere
            resultsGS = galeShapley(schools,allStudents)
            borda = bordaCount(resultsGS)
            vals = list(isBetterOff(resultsGS))
            difVals[j]= vals

            # Sincere and Sophisticated
            resultsGSFake = galeShapleyFake(schoolsCopy,allStudentsCopy)
            bordaFake = bordaCount(resultsGSFake)
            valsFake = list(isBetterOff(resultsGSFake))
            difValsFake[j]= valsFake


            runningSum += borda
            runningSumFake += bordaFake
            # df.loc[i]['Borda Result'] = borda
        averages[j] = runningSum/iterations/j
        averagesFake[j] = runningSumFake/(iterations*j)
        # df.to_csv('resultsGS' + str(j) + '.csv')
    print("Gale Shapely averages: ", averages)
    print("How much better of GS: ", difVals)
    print("FAKE: Gale Shapely averages: ", averagesFake)
    print("FAKE: How much better of GS: ", difValsFake)

    avgFake = averagesFake.values()
    avgTrue = averages.values()
    plt.scatter(studentsNumber,avgTrue,label="With Sophisticated")
    # plt.scatter(liarFracs,avgTrue,label="All Sincere")
    plt.title("Social Utility (Measured via Borda Count)")
    plt.xlabel("Number of Students")
    plt.ylabel("Average")
    # plt.legend()
    plt.show()
    #
    # avgPrefsSincere = np.asarray(list(difVals.values()))
    # avgPrefs = np.asarray(list(difValsFake.values()))
    # print(np.shape(avgPrefsSincere[:,0]))
    # print(avgPrefsSincere)
    # plt.scatter(liarFracs,avgPrefs[:,0],s=20,label="Average Liar Preference")
    # plt.scatter(liarFracs,avgPrefsSincere[:,0],s=20,label="Average Sincere Preference")
    # plt.title("Average preferences")
    # plt.xlabel("Liar fraction")
    # plt.ylabel("Average")
    # plt.legend()
    # plt.show()
