import re
from typing import List

from curse import Curse
from curses_data import CursesClues, CursesDisableMethods
from colors import Colors


class CursesBase:
    def __init__(self):
        self.clues = [clue for key, clue in list(CursesClues.__dict__.items()) if not key.startswith("__")]
        self.disable_methods = [d_method for key, d_method in list(CursesDisableMethods.__dict__.items())
                                if not key.startswith("__")]
        self.chosen_clues = []
        
        # SEASON 1:

        self.revenge_curse = Curse("Revenge Curse", description="Casted by Chief of the Village of Native Americans "
                                                                "in Atoka Valley. Chief said, that no white man would "
                                                                "ever tarnish this land again. Nature would rise up "
                                                                "and protect the valley.",
                                   episodes={"S01": [8]})
        self.revenge_curse.clues = [CursesClues.missing_or_dead_people_regularly_in_the_same_area,
                                    CursesClues.people_dead_weirdly, CursesClues.weird_animal_behavior]
        self.revenge_curse.kill_methods = [CursesDisableMethods.surviving_the_curse]

        self.reaper_trapping_spell = Curse("Reaper trapping spell", description="Spell, that controls a reaper",
                                           episodes={"S01": [12]})
        self.reaper_trapping_spell.clues = [CursesClues.control_over_a_reaper, CursesClues.black_altar,
                                            CursesClues.controlled_with_a_spell_and_a_cross]
        self.reaper_trapping_spell.disable_methods = [CursesDisableMethods.destroy_the_coptic_cross,
                                                      CursesDisableMethods.destroy_the_black_altar]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 2:

        self.hoodoo_protection_spell = Curse("Hoodoo protection spell", description="Protects against evil spirits",
                                             episodes={"S02": [11]})
        self.hoodoo_protection_spell.clues = [CursesClues.drawn_quincunx]

        # SEASON 3:



        # SEASON 4:



        # SEASON 5:



        # SEASON 6:



        # SEASON 7:



        # SEASON 8:



        # SEASON 9:



        # SEASON 10:



        # SEASON 11:

        self.kiss_of_death = Curse("Kiss of death (Aramaic curse)")
        self.kiss_of_death.clues = [CursesClues.sealed_with_a_kiss, CursesClues.the_last_person_that_got_kissed_dies]
        self.kiss_of_death.disable_methods = [CursesDisableMethods.kill_the_witch_that_cursed_a_person]

        # SEASON 12:

        self.memory_curse = Curse("Memory curse")
        self.memory_curse.clues = [CursesClues.slow_loss_of_the_memory]
        self.memory_curse.disable_methods = [CursesDisableMethods.kill_the_witch_that_cursed_a_person]

        # SEASON 13:



        # SEASON 14:



        # SEASON 15:



        self.curses = [curse for curse in self.__dict__.values() if isinstance(curse, Curse)]

    def print_all_sorted_clues(self):
        print(Colors.BOLD + Colors.YELLOW + "\nBase of all clues:" + Colors.ENDC)
        sorted_clues = sorted(self.clues)
        for clue_number, clue in enumerate(sorted_clues, 1):
            print(" *%5d  " % clue_number + clue)

    def print_all_clues(self):
        print(Colors.BOLD + Colors.YELLOW + "\nBase of all clues:" + Colors.ENDC)
        for clue_number, clue in enumerate(self.clues, 1):
            print(" *%5d  " % clue_number + clue)
    
    def choose_clues(self) -> List[str]:
        clues = input(Colors.UNDERLINE + "\nChoose clues:" + Colors.ENDC + " ")
        clues = re.sub('[a-zA-Z,&^%$#@?|/:;"_=]', ' ', clues)
        chosen_clues = [self.clues[int(clue) - 1] for clue in clues.split()
                        if (clue.isdigit() and int(clue) <= len(self.clues))]
        return chosen_clues

    def print_all_matches(self, selected_clues: List[str]):
        curses_clues_dict = {}
        for curse_number, curse in enumerate(self.curses):
            if curse.clues is not None \
                    and (clues_intersection := len(set(curse.clues).intersection(set(selected_clues)))):
                curses_clues_dict[curse_number] = clues_intersection
        sorted_curses_clues_dict = {m: c for m, c in sorted(curses_clues_dict.items(), key=lambda item: item[1],
                                                            reverse=True)}
        print(f"\n{len(sorted_curses_clues_dict)} MATCHED CURSES FOUND: \n")
        for curse_number, number_of_matching_clues in sorted_curses_clues_dict.items():
            print(Colors.BOLD + Colors.BLUE + f"{number_of_matching_clues}/{len(selected_clues)} Matches:"
                  + Colors.ENDC, end=" ")
            self.curses[curse_number].print_all()
            print("")

    def print_all_curses(self):
        for curse in self.curses:
            curse.print_all()

    def print_curses_names(self):
        sorted_curses = sorted([curse.name for curse in self.curses])
        print(Colors.RED + Colors.BOLD + "All curses:" + Colors.ENDC)
        for curse in sorted_curses:
            print(" *  " + curse)
