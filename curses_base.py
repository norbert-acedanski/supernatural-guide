import re
from curse import Curse
from colors import Colors


class CursesBase:
    def __init__(self):
        self.symptoms = ["sealed with a kiss", "the last person that got kissed dies (reverse order - first kisses, dies last)", "slow loss of the memory"]
        self.disable_method = ["kill the Witch that cursed a person"]
        self.chosen_symptoms = []
        
        # SEASON 1:



        # SEASON 2:



        # SEASON 3:



        # SEASON 4:



        # SEASON 5:



        # SEASON 6:



        # SEASON 7:



        # SEASON 8:



        # SEASON 9:



        # SEASON 10:



        # SEASON 11:

        self.kiss_of_death = Curse("Kiss of death (Arameic curse)")
        self.kiss_of_death.symptoms = [self.symptoms[0], self.symptoms[1]]
        self.kiss_of_death.disable_methods = [self.disable_method[0]]

        # SEASON 12:

        self.memory_curse = Curse("Memory curse")
        self.memory_curse.symptoms = [self.symptoms[2]]
        self.memory_curse.disable_methods = [self.disable_method[0]]

        # SEASON 13:



        # SEASON 14:



        # SEASON 15:



        self.curses = [self.kiss_of_death, self.memory_curse]

    def print_all_sorted_symptoms(self):
        print(Colors.BOLD + Colors.YELLOW + "\nBase of all clues:" + Colors.ENDC)
        sorted_symptoms = sorted(self.symptoms)
        for symptom_number, symptom in enumerate(sorted_symptoms, 1):
            print(" *%5d  " % symptom_number + symptom)

    def print_all_symptoms(self):
        print(Colors.BOLD + Colors.YELLOW + "\nBase of all clues:" + Colors.ENDC)
        for symptom_number, symptom in enumerate(self.symptoms, 1):
            print(" *%5d  " % symptom_number + symptom)
    
    def choose_symptoms(self):
        symptoms = input(Colors.UNDERLINE + "\nChoose clues:" + Colors.ENDC + " ")
        symptoms = re.sub('[a-zA-Z,&^%$#@?|/:;"_=]', ' ', symptoms)
        self.chosen_symptoms = [int(symptom) - 1 for symptom in symptoms.split() if (symptom.isdigit() and int(symptom) <= len(self.symptoms))]
        if not self.chosen_symptoms:
            print("No clues chosen. Try again")
            self.choose_symptoms()

    def print_all_matches(self):
        curse_symptom_list = [0] * len(self.curses)
        for curse_number, curse in enumerate(self.curses):
            if curse.symptoms is not None:
                for symptom in curse.symptoms:
                    for chosen_symptom in self.chosen_symptoms:
                        if symptom == self.symptoms[chosen_symptom]:
                            curse_symptom_list[curse_number] += 1
        for curse_number, curse_match_count in enumerate(curse_symptom_list):
            if curse_match_count != 0:
                print(Colors.BOLD + Colors.BLUE + "\n" + str(curse_match_count) + "/" + str(len(self.chosen_symptoms)) + " Matches:" + Colors.ENDC, end=" ")
                self.curses[curse_number].print_all()

    def print_all_curses(self):
        for curse in self.curses:
            curse.print_all()

    def print_curses_names(self):
        sorted_curses = sorted([curse.name for curse in self.curses])
        print(Colors.RED + Colors.BOLD + "All curses:" + Colors.ENDC)
        for curse in sorted_curses:
            print(" *  " + curse)
