import re
from Curses import Curse
from Colors import bcolors

class CursesBase():
    def __init__(self):
        self.symptoms = ["sealed with a kiss", "the last person that got kissed dies (reverse order - first kisses, dies last)", "slow loss of the memory"]
        self.disableMethod = ["kill the Witch that cursed a person"]
        self.chosenSymptoms = []
        
        # SESON 1:



        # SESON 3:



        # SESON 3:



        # SESON 4:



        # SESON 5:



        # SESON 6:



        # SESON 7:



        # SESON 8:



        # SESON 9:



        # SESON 10:



        # SESON 11:

        self.KissOfDeath = Curse("Kiss of death (Arameic curse)")
        self.KissOfDeath.symptoms = [self.symptoms[0], self.symptoms[1]]
        self.KissOfDeath.disableMethods = [self.disableMethod[0]]

        # SESON 12:

        self.MemoryCurse = Curse("Memory curse")
        self.MemoryCurse.symptoms = [self.symptoms[2]]
        self.MemoryCurse.disableMethods = [self.disableMethod[0]]

        # SESON 13:



        # SESON 14:



        # SESON 15:



        self.Curses = [self.KissOfDeath, self.MemoryCurse]

    def printAllSortedSymptoms(self):
        sortedSymptoms = [None]*len(self.symptoms)
        print(bcolors.BOLD + bcolors.YELLOW + "\nBase of all symptoms:" + bcolors.ENDC)
        i = 0
        sortedSymptoms = sorted(self.symptoms)
        for symptom in sortedSymptoms:
            print(" *%5d  " % (i + 1) + symptom)
            i += 1

    def printAllSymptoms(self):
        print(bcolors.BOLD + bcolors.YELLOW + "\nBase of all symptoms:" + bcolors.ENDC)
        i = 0
        for symptom in self.symptoms:
            print(" *%5d  " % (i + 1) + symptom)
            i += 1
    
    def chooseSymptoms(self):
        symptoms = input(bcolors.UNDERLINE + "\nChoose symptoms:" + bcolors.ENDC + " ")
        symptoms = re.sub('[a-zA-Z,&^%$#@?|/:;"_=]', ' ', symptoms)
        self.chosenSymptoms = [int(symptom) - 1 for symptom in symptoms.split() if (symptom.isdigit() and int(symptom) <= len(self.symptoms))]
        if self.chosenSymptoms == []:
            print("No symptoms chosen. Try again")
            self.chooseSymptoms()

    def printAllMachtes(self):
        curseSymptomList = [None]*len(self.Curses)
        for curse in range(len(self.Curses)):
            curseSymptomList[curse] = 0
        i = 0
        for curse in self.Curses:
            if curse.symptoms is not None:
                for symptom in curse.symptoms:
                    for choosenSympton in self.chosenSymptoms:
                        if symptom == self.symptoms[choosenSympton]:
                            curseSymptomList[i] += 1
            i += 1
        for number in range(len(curseSymptomList)):
            if curseSymptomList[number] != 0:
                print(bcolors.BOLD + bcolors.BLUE + "\n" + str(curseSymptomList[number]) + "/" + str(len(self.chosenSymptoms)) + " Matches:" + bcolors.ENDC, end=" ")
                self.Curses[number].printAll()

    def printAllCurses(self):
        for curse in self.Curses:
            curse.printAll()

    def printCursesNames(self):
        sortedCurses = [None]*len(self.Curses)
        i = 0
        for curse in self.Curses:
            sortedCurses[i] = curse.name
            i += 1
        sortedCurses = sorted(sortedCurses)
        print(bcolors.RED + bcolors.BOLD + "All curses:" + bcolors.ENDC)
        for name in range(len(sortedCurses)):
            print(" *  " + sortedCurses[name])