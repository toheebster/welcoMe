__author__ = 'rogermao'
import Service

class Schedule:

    def __init__(self, roster):
        #initialize services
        self.services = []
        self.roster = roster

    def schedule(self):
        for service in services:
            whichService = service.which
            expPeople = roster.getByExperience(5)
            numGuys = 0
            numGirls = 0
            if whichService.equals("Large Group"):

                expPeople = roster.getByExperience(5)
                expPeople = [(person,person.largeGroupCount) for person in expPeople]
                expPeople = sorted(expPeople, key=lambda x:x[1])
                expPerson = expPeople[0]
                expPerson.addLargeGroup()
                if expPerson.gender == "F":
                    numGirls += 1
                else
                    numGuys += 1
                service.addWelcomer(expPerson)

                guys = roster.getByGender("M")
                guys = [(guys,guys.largeGroupCount) for guy in guys]
                guys = sorted(guys, key=lambda x:x[1])
                girls = roster.getByGender("F")
                girls = [(girls,girls.largeGroupCount) for girl in girls]
                girls = sorted(girls, key=lambda x:x[1])

            else if whichService.equals("9:30"):

            else if whichService.equals("12:30"):


            expPeople = roster.getByExperience(5)
            expPeople = [(person,person.
            for
            service.welcomers.append(roster.get

