__author__ = 'rogermao'

class person:

    def __init__(self,name):
        self.name = name
        self.gender = ""
        self.conflictDates = []
        self.experience = -1
        self.largeGroup = True
        self.nineThirty = True
        self.twelveThirty = True
        self.largeGroupCount = 0
        self.nineThirtyCount = 0
        self.twelveThirtyCount = 0
        self.car = False
        self.dates = []

    def addLargeGroup(self):
        self.largeGroupCount += 1

    def addNineThirty(self):
        self.nineThirtyCount += 1

    def addTwelveThirty(self):
        self.twelveThirtyCount += 1
