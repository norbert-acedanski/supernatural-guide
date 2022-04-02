from Colors import bcolors

class Curse():
    def __init__(self, name):
        self.name = name
        self.symptoms = None
        self.disableMethods = None

    def symptomsBase(self, symptoms = []):
        self.symptoms = symptoms

    def disableMethodsBase(self, disableMethods = []):
        self.disableMethods = disableMethods

    def printName(self):
        print(bcolors.GREEN + "\n" + self.name + ":" + bcolors.ENDC)
    
    def printSymptomsBase(self):
        print(bcolors.YELLOW + "Clues:" + bcolors.ENDC)
        if self.symptoms != None:
            for symptom in self.symptoms:
                print("  *  " + symptom)
        else:
            print("  *  None found")

    def printDisableMethods(self):
            print(bcolors.MAGENTA + "Disable Methods:" + bcolors.ENDC)
            if self.disableMethods != None:
                for method in self.disableMethods:
                    print("  *  " + method)
            else:
                print("  *  None found...")

    def printAll(self):
        self.printName()
        self.printSymptomsBase()
        self.printDisableMethods()