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

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 3:

        self.curse = Curse("Unknown curse", episodes={"S03": [9]})
        self.curse.clues = [CursesClues.hex_bag_hidden_somewhere, CursesClues.people_dead_weirdly,
                            CursesClues.weird_electronics_behavior, CursesClues.people_feeling_weird_or_bad]
        self.curse.disable_methods = [CursesDisableMethods.burn_the_hex, CursesDisableMethods.magic_brew]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 4:

        self.yellow_fever = Curse("Yellow fever", description="Sickness that is transferred from a ghost (Buru Buru) "
                                                              "of a person and then it behaves like any other disease. "
                                                              "People get anxious, then scared, then more scared "
                                                              "and at the end, their heart gives up. "
                                                              "Symptoms also include hallucinations.",
                                  episodes={"S04": [6]})
        self.yellow_fever.clues = [CursesClues.
                                   missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                                   CursesClues.people_dead_weirdly, CursesClues.people_acting_weirdly,
                                   CursesClues.no_hex_bags, CursesClues.emf, CursesClues.no_sulfur,
                                   CursesClues.people_scared_of_everything, CursesClues.hallucinations]
        self.yellow_fever.disable_methods = [CursesDisableMethods.disable_the_spirit_that_causes_it]

        self.samhain_summoning_spell = Curse("Samhain summoning spell", description="Spell, that can summon Samhain. "
                                                                                    "The ritual can only be performed "
                                                                                    "every 600 years before the 31st "
                                                                                    "of October.")
        self.samhain_summoning_spell.clues = [CursesClues.people_dead_weirdly, CursesClues.hex_bag_hidden_somewhere]

        self.babylonian_wishing_curse = Curse("Babylonian wishing curse",
                                              description="A curse, that grants wishes, then turns them bad. "
                                                          "Is a part of an object (a coin for example). "
                                                          "A spell was made by babylonian priests for Tiamat "
                                                          "(A Babylonian god of primordial chaos).",
                                              episodes={"S04": [8]})
        self.babylonian_wishing_curse.clues = [CursesClues.strange_different_things_happening, CursesClues.magical_coin]
        self.babylonian_wishing_curse.disable_methods = \
            [CursesDisableMethods.first_person_that_wished_has_to_remove_the_coin, CursesDisableMethods.melt_the_coin]

        self.death_transfer_spell = Curse("Death Transfer Spell", description="Spell, that allows to transfer death "
                                                                              "from one person to another.",
                                          episodes={"S04": [12]})
        self.death_transfer_spell.clues = [CursesClues.people_dead_weirdly, CursesClues.card_found_on_a_victim]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 5:

        self.reaper_death_summoning_spell = Curse("Reaper Death summoning spell",
                                                  description="Can summon Angel of Death from its prison. "
                                                              "Requires a place, where an awful carnage has happened. "
                                                              "It ha to be performed at midnight. "
                                                              "Requires sacrifice of a lot of people and demons.",
                                                  episodes={"S05": [10]})
        self.reaper_death_summoning_spell.clues = \
            [CursesClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
             CursesClues.small_earth_quake, CursesClues.number_of_reapers_appearing]

        self.soul_swapping_spell = Curse("Soul swapping spell", description="Allows to switch souls of 2 people.",
                                         episodes={"S05": [12]})
        self.soul_swapping_spell.clues = [CursesClues.can_switch_souls_of_people]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 6:

        self.angel_tracking_spell = Curse("Angel tracking spell", description="Spell, that allows to track an angel. "
                                                                              "Is performed with a myrrh, human blood "
                                                                              "and a drawn symbol. "
                                                                              "An enochian spell is then said with "
                                                                              "holy water put in the bowl.",
                                          episodes={"S06": [3]})

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
