from Colors import bcolors


class Monster:
    def __init__(self, name, description =""):
        self.name = name
        self.description = description
        self.symptoms = None
        self.kill_methods = None
        self.disable_methods = None
        self.cure_methods = None

    def symptoms_base(self, symptoms=[]):
        self.symptoms = symptoms

    def kill_methods_base(self, kill_methods=[]):
        self.kill_methods = kill_methods

    def disable_methods_base(self, disable_methods=[]):
        self.disable_methods = disable_methods

    def cure_methods_base(self, cure_methods=[]):
        self.cure_methods = cure_methods

    def print_name(self):
        print(bcolors.GREEN + "\n" + self.name + ":" + bcolors.ENDC)

    def print_description(self):
        if self.description != "":
            print("   " + self.description)

    def print_symptoms_base(self):
        print(bcolors.YELLOW + "Clues:" + bcolors.ENDC)
        if self.symptoms is not None:
            for symptom in self.symptoms:
                print("  »  " + symptom)
        else:
            print("  »  None found")

    def print_disable_methods(self):
        if self.disable_methods is not None:
            print(bcolors.MAGENTA + "Disable Methods:" + bcolors.ENDC)
            for method in self.disable_methods:
                print("  »  " + method)

    def print_kill_methods_base(self):
        print(bcolors.RED + "Kill methods:" + bcolors.ENDC)
        if self.kill_methods is not None:
            for kill_method in self.kill_methods:
                print("  »  " + kill_method)
        else:
            print("  »  None found")

    def print_cure_methods_base(self):
        if self.cure_methods is not None:
            print(bcolors.CYAN + "Cure methods:" + bcolors.ENDC)
            for cure in self.cure_methods:
                print("  »  " + cure)

    def print_all(self):
        self.print_name()
        self.print_description()
        self.print_symptoms_base()
        self.print_disable_methods()
        self.print_kill_methods_base()
        self.print_cure_methods_base()
