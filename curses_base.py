import re
from typing import List

from curse import Curse
from curses_data import CursesClues, CursesDisableMethods
from colors import Colors


class CursesBase:

    # SEASON 1:

    revenge_curse = Curse("Revenge Curse", description="Casted by Chief of the Village of Native Americans in Atoka "
                                                       "Valley. Chief said, that no white man would ever tarnish this "
                                                       "land again. Nature would rise up and protect the valley.",
                          episodes={"S01": [8]})
    revenge_curse.clues = [CursesClues.missing_or_dead_people_regularly_in_the_same_area,
                           CursesClues.people_dead_weirdly, CursesClues.weird_animal_behavior]
    revenge_curse.kill_methods = [CursesDisableMethods.surviving_the_curse]

    reaper_trapping_spell = Curse("Reaper trapping spell", description="Spell, that controls a reaper or traps it.",
                                  episodes={"S01": [12], "S07": [10]})
    reaper_trapping_spell.clues = [CursesClues.control_over_a_reaper, CursesClues.black_altar,
                                   CursesClues.controlled_with_a_spell_and_a_cross]
    reaper_trapping_spell.disable_methods = [CursesDisableMethods.destroy_the_coptic_cross,
                                             CursesDisableMethods.destroy_the_black_altar]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 2:

    hoodoo_protection_spell = Curse("Hoodoo protection spell", description="Protects against evil spirits",
                                    episodes={"S02": [11]})
    hoodoo_protection_spell.clues = [CursesClues.drawn_quincunx]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 3:

    killing_curse = Curse("Killing curse", description="Spell, that kills a person in a specific way.",
                          episodes={"S03": [9], "S07": [5]})
    killing_curse.clues = [CursesClues.hex_bag_hidden_somewhere, CursesClues.coin_hidden_somewhere,
                           CursesClues.people_dead_weirdly, CursesClues.weird_electronics_behavior,
                           CursesClues.people_feeling_weird_or_bad]
    killing_curse.disable_methods = [CursesDisableMethods.burn_the_hex, CursesDisableMethods.destroy_the_coin,
                                     CursesDisableMethods.magic_brew]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 4:

    yellow_fever = Curse("Yellow fever", description="Sickness that is transferred from a ghost (Buru Buru) "
                                                     "of a person and then it behaves like any other disease. "
                                                     "People get anxious, then scared, then more scared and "
                                                     "at the end, their heart gives up. "
                                                     "Symptoms also include hallucinations.", episodes={"S04": [6]})
    yellow_fever.clues = [CursesClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                          CursesClues.people_dead_weirdly, CursesClues.people_acting_weirdly, CursesClues.no_hex_bags,
                          CursesClues.emf, CursesClues.no_sulfur, CursesClues.people_scared_of_everything,
                          CursesClues.hallucinations]
    yellow_fever.disable_methods = [CursesDisableMethods.disable_the_spirit_that_causes_it]

    samhain_summoning_spell = Curse("Samhain summoning spell", description="Spell, that can summon Samhain. The ritual "
                                                                           "can only be performed every 600 years "
                                                                           "before the 31st of October.")
    samhain_summoning_spell.clues = [CursesClues.people_dead_weirdly, CursesClues.hex_bag_hidden_somewhere]

    babylonian_wishing_curse = Curse("Babylonian wishing curse", description="A curse, that grants wishes, then turns "
                                                                             "them bad. Is a part of an object (a coin "
                                                                             "for example). A spell was made by "
                                                                             "babylonian priests for Tiamat "
                                                                             "(A Babylonian god of primordial chaos).",
                                     episodes={"S04": [8]})
    babylonian_wishing_curse.clues = [CursesClues.strange_different_things_happening, CursesClues.magical_coin]
    babylonian_wishing_curse.disable_methods = [CursesDisableMethods.first_person_that_wished_has_to_remove_the_coin,
                                                CursesDisableMethods.melt_the_coin]

    death_transfer_spell = Curse("Death Transfer Spell", description="Spell, that allows to transfer death from "
                                                                     "one person to another.", episodes={"S04": [12]})
    death_transfer_spell.clues = [CursesClues.people_dead_weirdly, CursesClues.card_found_on_a_victim]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 5:

    reaper_death_summoning_spell = Curse("Reaper Death summoning spell", description="Can summon Angel of Death from "
                                                                                     "its prison. Requires a place, "
                                                                                     "where an awful carnage has "
                                                                                     "happened. It ha to be performed "
                                                                                     "at midnight. Requires sacrifice "
                                                                                     "of a lot of people and demons.",
                                         episodes={"S05": [10]})
    reaper_death_summoning_spell.clues = \
        [CursesClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
         CursesClues.small_earth_quake, CursesClues.number_of_reapers_appearing]

    soul_swapping_spell = Curse("Soul swapping spell", description="Allows to switch souls of 2 people.",
                                episodes={"S05": [12]})
    soul_swapping_spell.clues = [CursesClues.can_switch_souls_of_people]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 6:

    angel_tracking_spell = Curse("Angel tracking spell", description="Spell, that allows to track an angel. "
                                                                     "Is performed with a myrrh, human blood "
                                                                     "and a drawn symbol. An enochian spell is then "
                                                                     "said with holy water put in the bowl.",
                                 episodes={"S06": [3]})

    truth_curse = Curse("Truth Curse", description="People wish to hear the truth and it happens - all people tell "
                                                   "this person only the truth. It is caused by goddess Veritas",
                        episodes={"S06": [6]})
    truth_curse.clues = [CursesClues.people_dead_weirdly, CursesClues.suicides, CursesClues.no_emf,
                         CursesClues.no_sulfur, CursesClues.no_hex_bags, CursesClues.people_hear_truth_only,
                         CursesClues.does_not_work_on_people_without_souls]
    truth_curse.disable_methods = [CursesDisableMethods.kill_goddess_of_truth_veritas]

    timeline_change_spell = Curse("Timeline change spell", description="Spell made with salt, blood of a lamb "
                                                                       "and a bone of a lesser saint. Also a sigil "
                                                                       "has to be drawn.", episodes={"S06": [15]})
    timeline_change_spell.clues = [CursesClues.different_history, CursesClues.different_memories,
                                   CursesClues.strange_feeling_that_things_should_be_different]
    timeline_change_spell.disable_methods = [CursesDisableMethods.wait_for_an_opening_from_the_other_side]

    angel_summoning_spell = Curse("Angel summoning spell", description="Can summon a specific angel.",
                                  episodes={"S06": [21]})  # TODO: Check where else was this spell used.

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 7:

    death_binding_spell = Curse("Death Binding Spell", description="Spell, that binds Death. To perform it, you need "
                                                                   "'An act of God crystallized forever' - crystal "
                                                                   "made whe lightning structs sand broke into powder, "
                                                                   "unknown herbs, blood of a person. You mix the "
                                                                   "ingredients and say a spell.",
                                episodes={"S07": [1]})
    death_binding_spell.disable_methods = [CursesDisableMethods.will_of_an_angel_on_soul_juice]

    love_potion = Curse("Love potion", description="A potion, that allows a person to fall in love in another person.",
                        episodes={"S07": [8]})
    love_potion.clues = [CursesClues.blinding_love, CursesClues.people_acting_weirdly]

    fear_realizing_curse = Curse("Fear realizing curse", description="Curse, that allows to bring to life the fear of "
                                                                     "a person and send it to kill someone. "
                                                                     "It requires something, that belongs to the "
                                                                     "person, that is the target, and a drawing of the "
                                                                     "thing, that should kill that person.",
                                 episodes={"S07": [14]})

    fear_realizing_curse.clues = [CursesClues.seen_as_a_clown, CursesClues.people_dead_weirdly, CursesClues.no_sulfur,
                                  CursesClues.bite_marks_on_peoples_necks, CursesClues.no_cold_spots,
                                  CursesClues.people_seeing_things_or_figures, CursesClues.people_nightmares_come_true,
                                  CursesClues.strange_different_things_happening,
                                  CursesClues.people_seeing_strange_things]
    fear_realizing_curse.disable_methods = [CursesDisableMethods.kill_the_person_that_causes_it]

    demon_summoning_spell = Curse("Demon summoning spell", description="Spell, that allows a person to summon a demon "
                                                                       "into a person or as is. Requires a blood of "
                                                                       "an exorcist, that banished the demon in the "
                                                                       "first place, a part of a dog, abd a spell.",
                                  episodes={"S07": [15, 23]})

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 8:

    bringing_soul_from_purgatory_spell = Curse("Bringing soul from Purgatory spell",
                                               description="Can bring back a monster, which soul was taken "
                                                           "from purgatory.", episodes={"S08": [1]})
    bringing_soul_from_purgatory_spell.clues = [CursesClues.red_blood]

    demon_killing_spell = Curse("Demon killing spell", description="Spell of right ingredients burned by fire kills "
                                                                   "demons nearby. Written on a Word of GOD "
                                                                   "about demons.", episodes={"S08": [1, 7, 10]})
    demon_killing_spell.clues = [CursesClues.shadows_of_people_on_the_wall]

    closing_the_gates_of_hell_spell = Curse("Closing the Gates of Hell spell",
                                            description="Spell, that will banish all demons of the face of the Earth "
                                                        "and close the Gates of Hell forever. "
                                                        "The spell consists of 3 trials. "
                                                        "First is to kill a Hell hound and bathe in its blood. "
                                                        "Second is to resque an innocent soul from Hell "
                                                        "and deliver it to Heaven."
                                                        "Third is to cure a demon - on a sacred land a demon must be "
                                                        "injected with 8 doses of purified blood (from a man, that was "
                                                        "in a confession). After that, a modified exorcism has to be "
                                                        "performed and a blood of a purified person has to be put on "
                                                        "a demon face. "
                                                        "After each trial there is a spell to say. "
                                                        "After the last trial is completed and a spell is said, "
                                                        "the Gates of Hell will close, but the person, that does "
                                                        "the trials will die. That is what GOD intended - "
                                                        "the ultimate sacrifice. Spell hurts the person, that tries it "
                                                        "- starts to cough blood. Even angel healing cannot heal it.",
                                            episodes={"S08": [14, 15, 16, 17, 19, 21, 22, 23]})
    closing_the_gates_of_hell_spell.clues = [CursesClues.killed_hell_hound, CursesClues.blood_cough]

    bringing_demon_back_to_the_body_spell = Curse("Bringing demon back to the body spell",
                                                  description="Spell, that allows to bring back the demon, that tries "
                                                              "to escape a body. It's just a reversed exorcism "
                                                              "according to Sam.", episodes={"S08": [2]})

    time_travel_spell = Curse("Time travel spell", description="A spell, that (when combined with a drawing made of "
                                                               "human blood, angel feather, tears of a dragon, "
                                                               "a pinch of the Sands of Time and a week charge of "
                                                               "a soul) can move a person to another time "
                                                               "to a specific person or their relatives.",
                              episodes={"S08": [12]})
    time_travel_spell.clues = [CursesClues.people_appearing_out_of_nowhere]

    false_memories_spell = Curse("False memories spell", description="It is used to create false memories into another "
                                                                     "witch's mind.", episodes={"S08": [15]})
    false_memories_spell.clues = [CursesClues.people_dead_weirdly, CursesClues.different_memories,
                                  CursesClues.weird_dreams]

    banish_angels_to_earth_spell = Curse("Banish Angels to Earth spell",
                                         description="Spell to make every angel fall. Like the spell to close "
                                                     "the Gates of Hell, it consists of 3 ingredients. "
                                                     "First thing is to cut the heart of a Nephilim. "
                                                     "Second is to retrieve Cupid's bow. "
                                                     "The third one is an angelic grace (cut from Angel's throat). "
                                                     "Mixed until smoke rises from the ashes making each angel fall. "
                                                     "It's irreversible.",
                                         episodes={"S08": [22, 23], "S09": [6]})
    banish_angels_to_earth_spell.clues = [CursesClues.people_dead_weirdly, CursesClues.missing_heart,
                                          CursesClues.meteor_shower_over_earth]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 9:

    animal_characteristics_copy_spell = Curse("Animal characteristics copy spell",
                                              description="A spell, that allows a person to gain characteristics of "
                                                          "animals - like speed, strength, camouflage, etc. In order "
                                                          "to do that, a part of the animal has to be eaten and "
                                                          "a proper spell has to be spoken. It wears off depending on "
                                                          "the combined ingredients.", episodes={"S09": [5]})
    animal_characteristics_copy_spell.clues = [CursesClues.double_tongue, CursesClues.people_dead_weirdly,
                                               CursesClues.high_strength, CursesClues.no_hex_bags, CursesClues.claws,
                                               CursesClues.venom_necrosis, CursesClues.eats_whole_animals,
                                               CursesClues.no_bite_marks_on_peoples_necks, CursesClues.cat_eyes]

    inuit_animal_speaking_spell = Curse("Inuit animal speaking spell", description="Allows a person to hear animals "
                                                                                   "speaking and talking to them. "
                                                                                   "It is combined with a drink, then "
                                                                                   "there is a spell to say. It wears "
                                                                                   "off in couple of hours.",
                                        episodes={"S09": [5]})
    inuit_animal_speaking_spell.clues = [CursesClues.animal_like_behavior_of_a_person]

    # SEASON 10:



    # SEASON 11:

    kiss_of_death = Curse("Kiss of death (Aramaic curse)")
    kiss_of_death.clues = [CursesClues.sealed_with_a_kiss, CursesClues.the_last_person_that_got_kissed_dies]
    kiss_of_death.disable_methods = [CursesDisableMethods.kill_the_witch_that_cursed_a_person]

    # SEASON 12:

    memory_curse = Curse("Memory curse")
    memory_curse.clues = [CursesClues.slow_loss_of_the_memory]
    memory_curse.disable_methods = [CursesDisableMethods.kill_the_witch_that_cursed_a_person]

    # SEASON 13:



    # SEASON 14:



    # SEASON 15:


    def __init__(self):
        self.curses = [curse for curse in self.__class__.__dict__.values() if isinstance(curse, Curse)]
        self.clues = [clue for key, clue in list(CursesClues.__dict__.items()) if not key.startswith("__")]
        self.disable_methods = [d_method for key, d_method in list(CursesDisableMethods.__dict__.items())
                                if not key.startswith("__")]
        self.chosen_clues = []

    def print_all_sorted_clues(self):
        print(Colors.BOLD + Colors.YELLOW + "\nBase of all clues:" + Colors.ENDC)
        sorted_clues = sorted(self.clues)
        for clue_number, clue in enumerate(sorted_clues, 1):
            print(" *%5d " % clue_number, clue)

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
