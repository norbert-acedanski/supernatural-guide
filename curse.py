from colors import Colors


class Curse:
    def __init__(self, name):
        self.name = name
        self.clues = None
        self.disable_methods = None

    def clues_base(self, clues=None):
        self.clues = clues

    def disable_methods_base(self, disable_methods=None):
        self.disable_methods = disable_methods

    def print_name(self):
        print(Colors.GREEN + "\n" + self.name + ":" + Colors.ENDC)
    
    def print_clues_base(self):
        print(Colors.YELLOW + "Clues:" + Colors.ENDC)
        if self.clues is not None:
            for clue in self.clues:
                print("  *  " + clue)
        else:
            print("  *  None found")

    def print_disable_methods(self):
        print(Colors.MAGENTA + "Disable Methods:" + Colors.ENDC)
        if self.disable_methods is not None:
            for method in self.disable_methods:
                print("  *  " + method)
        else:
            print("  *  None found...")

    def print_all(self):
        self.print_name()
        self.print_clues_base()
        self.print_disable_methods()