__author__ = 'rogermao'
import csv
import Person


class roster:

    data = []

    def __init__(self):
        self.data = {}

    def parseFile(self, filename):
        file = open(filename)

        dataFile = csv.reader(file)

        data = [line for line in dataFile]
        data = data[1:]

        for row in data:
            name = row[0]
            person = Person(name)
            person.gender = row[1]
            person.conflictDates = row[2].split(",")
            person.experience = row[3]
            conflictServices = row[4].split(",")
            if "Large Group" in conflictServices:
                person.largeGroup = True
            if "9:30" in conflictServices:
                person.nineThirty = True
            if "12:30" in conflictServices:
                person.twelveThirty = True
            person.car = row[5]
            data.append(person)

    def getData(self):
        return self.data

    def getNames(self):
        return [person.name for person in self.data]

    def getByName(self,name):
        return [person for person in self.data if person.name == name]

    def getByExperience(self,experience):
        return [person for person in self.data if person.experience == experience]
