from Colors import bcolors

class Monster:
    def __init__(self, name, discription = ""):
        self.name = name
        self.discription = discription
        self.symptoms = None
        self.killMethods = None
        self.disableMethods = None
        self.cureMethods = None

    def symptomsBase(self, symptoms = []):
        self.symptoms = symptoms

    def killMethodsBase(self, killMethods = []):
        self.killMethods = killMethods

    def disableMethodsBase(self, disableMethods = []):
        self.disableMethods = disableMethods

    def cureMethodsBase(self, cureMethods = []):
        self.cureMethods = cureMethods

    def printName(self):
        print(bcolors.GREEN + "\n" + self.name + ":" + bcolors.ENDC)

    def printDiscription(self):
        if self.discription != "":
            print("   " + self.discription)

    def printSymptomsBase(self):
        print(bcolors.YELLOW + "Clues:" + bcolors.ENDC)
        if self.symptoms == None:
            print("  »  None found")
        else:
            for symptom in self.symptoms:
                print("  »  " + symptom)

    def printDisableMethods(self):
        if self.disableMethods != None:
            print(bcolors.MAGENTA + "Disable Methods:" + bcolors.ENDC)
            for method in self.disableMethods:
                print("  »  " + method)

    def printKillMethodsBase(self):
        print(bcolors.RED + "Kill methods:" + bcolors.ENDC)
        if self.killMethods == None:
            print("  »  None found")
        else:
            for killMethod in self.killMethods:
                print("  »  " + killMethod)

    def printCureMethodsBase(self):
        if self.cureMethods != None:
            print(bcolors.CYAN + "Cure methods:" + bcolors.ENDC)
            for cure in self.cureMethods:
                print("  »  " + cure)


    def printAll(self):
        self.printName()
        self.printDiscription()
        self.printSymptomsBase()
        self.printDisableMethods()
        self.printKillMethodsBase()
        self.printCureMethodsBase()