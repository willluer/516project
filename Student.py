import random
import operator

class Student:
    def __init__(self,id,type,schools):
        self.id = id
        self.distances = [random.uniform(0,1) for i in range(len(schools))]
        self.preferences = [1, 0]
        # self.preferences = self.initPreferences(schools)
        self.school = None

        self.type = type
        # If type == True, then student sincere
        # if type == False, then student sophisticated

    def initPreferences(self, schools):
        valueList = {}
        keys = []
        for school in schools:
            quality = school.quality
            schoolID = school.id
            dist = self.distances[schoolID]
            r = random.uniform(0,1)

            value = 1/dist + quality + r
            valueList[schoolID] = value

        sortedValues = sorted(valueList.items(), key=operator.itemgetter(1))

        # print(sortedValues)
        for i in range(len(sortedValues)):
            keys.append(sortedValues[len(sortedValues)-i-1][0])

        return keys
