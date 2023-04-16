from colors import Colors
from object import Object
from objects_data import ObjectAbilities, ObjectMaintenance, ObjectDestroyMethods, JohnWinchesterJournal


class ObjectsBase:
    def __init__(self):
        self.abilities = [ability for key, ability in list(ObjectAbilities.__dict__.items())
                          if not key.startswith("__")]
        self.maintenance_methods = [method for key, method in list(ObjectMaintenance.__dict__.items())
                                    if not key.startswith("__")]

        # SEASON 1:

        # TODO: Watch each episode until S04E18 that contains John's journal
        # List of episodes, that the journal appears in:
        # https://supernatural.fandom.com/wiki/John_Winchester%27s_Journal#Appearances
        self.john_winchesters_journal = Object("John Winchester's Journal",
                                               description="A journal of John Winchester, that contains a lot "
                                                           "information about monsters in Supernatural Universe.",
                                               episodes={"S01": [], "S04": [19], "S06": [1, 8, 12], "S07": [8, 11]})
        self.john_winchesters_journal._information = {"S04E19": JohnWinchesterJournal.entry_about_johns_other_son,
                                                      "S06E12": JohnWinchesterJournal.entry_about_a_skinwalker}

        self.colt_of_colt = Object("Colt of Colt", description="Colt made by Samuel Colt in 1835, when Halley's Comet "
                                                               "was overhead and the same night those men died "
                                                               "at the Alamo. He made it for a hunter along with "
                                                               "13 bullets. Bullets can be crafted for this gun. "
                                                               "Can kill everything in all creation except 5 entities: "
                                                               "Archangel Lucyfer, unknown 4 left.",
                                   episodes={"S01": [20, 21, 22], "S02": [1, 22], "S03": [4, 5, 9], "S05": [10],
                                             "S06": [18]})
        self.colt_of_colt.abilities = [ObjectAbilities.can_kill_anything]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 2:

        self.charm_against_demons = Object("Charm against demons", description="Fend off possessions. Stops a demon "
                                                                               "from taking a person as a host.",
                                           episodes={"S02": [14], "S03": [12]})
        self.charm_against_demons.abilities = [ObjectAbilities.unables_possessions]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 3:

        self.demon_killing_knife = Object("Demon killing knife", description="Can literally kill demons, "
                                                                             "not get them back to hell. "
                                                                             "Cannot kill certain kinds of demons.",
                                          episodes={"S03": [1, 9, 16], "S04": [1, 9, 20, 22],
                                                    "S05": [1, 10, 14, 17, 20, 21, 22], "S06": [10, 20, 21],
                                                    "S07": [8, 15, 17, 21]})
        self.demon_killing_knife.abilities = [ObjectAbilities.can_kill_demons, ObjectAbilities.cannot_kill_angels]

        self.lucky_rabbits_foot = Object("Lucky rabbits foot",
                                         description="Person, who touches it becomes incredibly lucky. If another "
                                                     "person touches it, the previous one becomes incredibly unlucky "
                                                     "and dies in a week. To make one, you have to cut rabbits foot in "
                                                     "a cemetery under a full moon on a Friday the 13th.",
                                         episodes={"S03": [3]})
        self.lucky_rabbits_foot.abilities = [ObjectAbilities.grants_incredible_luck]
        self.lucky_rabbits_foot.destroy_methods = [ObjectDestroyMethods.burn_it]

        self.sleep_potion = Object("Sleep Potion", description="Made of African Dream Root. Was use by shaman and "
                                                               "medicine men for centuries. It is used for "
                                                               "dream-walking - entering another person's dreams.",
                                   episodes={"S03": [10]})
        self.sleep_potion.abilities = [ObjectAbilities.can_make_a_person_sleep_for_days,
                                       ObjectAbilities.brings_back_dreams_for_those_that_dont_have_them,
                                       ObjectAbilities.gives_people_control_over_dreams]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 4:

        self.sigil_against_angels = Object("Sigil against angels", description="Sigil made with blood, that can send "
                                                                               "angels back to heaven. Can be used to "
                                                                               "send back a specific angel type.",
                                           episodes={"S04": [10, 22], "S05": [13, 18], "S06": [3], "S07": [21]})
        self.sigil_against_angels.abilities = [ObjectAbilities.can_send_angels_back_to_heaven]

        self.angel_grace = Object("Angel grace", description="A power source for an angel", episodes={"S04": [10]})
        self.angel_grace.abilities = [ObjectAbilities.can_appear_as_falling_meteor,
                                      ObjectAbilities.the_place_it_hits_is_not_destroyed_but_flourishes,
                                      ObjectAbilities.can_kill_entities_when_reconnecting_with_an_angel]

        self.reaper_imprison_sigil = Object("Reaper imprison sigil", description="Sigil, that can trap a reaper.",
                                            episodes={"S04": [15]})
        self.reaper_imprison_sigil.abilities = [ObjectAbilities.traps_a_reaper]

        self.angel_protection_sigil = Object("Angel protection sigil", description="Angels can't get past it, "
                                                                                   "when the place is marked with it.",
                                             episodes={"S04": [15]})
        self.angel_protection_sigil.abilities = [ObjectAbilities.angels_cant_get_past_it]

        self.angel_blade = Object("Angel blade", description="A triangular, silvery blade, that each angel has.",
                                  episodes={"S04": [16], "S05": [1, 13, 18], "S06": [3, 10, 17, 18, 22], "S07": [21]})
        self.angel_blade.abilities = [ObjectAbilities.can_kill_angels]

        self.lucifers_cage = Object("Lucifer's Cage", description="A prison build specifically to contain archangelic "
                                                                  "powers (not seen yet). Can be opened with all "
                                                                  "4 rings of the horseman. There is fire there.",
                                    episodes={"S06": [13]})
        self.lucifers_cage.abilities = [ObjectAbilities.traps_an_archangel, ObjectAbilities.traps_a_soul_of_a_person]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 5:

        self.sword_of_archangel_michael = Object("Sword of Archangel Michael", description="A vessel, that Archangel "
                                                                                           "Michael possesses - a very "
                                                                                           "special person, that can "
                                                                                           "hold archangels power.",
                                                 episodes={"S05": [1]})

        self.enochian_sigil = Object("Enochian Sigil", description="Hides from every angel in creation "
                                                                   "(archangels included).", episodes={"S05": [1, 2]})
        self.enochian_sigil.abilities = [ObjectAbilities.hides_a_person_from_all_angels]

        self.magic_amulet = Object("Magic Amulet", description="It burns hot in God's presence. It is an Amulet, "
                                                               "that Sam gave Dean, when they were kids.",
                                   episodes={"S03": [8], "S05": [2, 16]})

        self.ring_of_war = Object("Ring of War", description="Can give people hallucinations. One of the four rings "
                                                             "of the Horseman.", episodes={"S05": [2]})
        self.ring_of_war.abilities = [ObjectAbilities.can_give_hallucinations]

        self.human_soul = Object("Human soul", description="As an object is very bright. Can be collected of a person.",
                                 episodes={"S05": [14], "S06": [11]})

        self.ring_of_famine = Object("Ring of Famine", description="Can give people starving sensation "
                                                                   "for things they lack/desire. One of the four rings "
                                                                   "of the Horseman.",
                                     episodes={"S05": [14]})
        self.ring_of_famine.abilities = [ObjectAbilities.can_give_incredible_starving_sensation_for_something]

        self.archangel_blade = Object("Archangel blade", description="A triangular, silvery blade, "
                                                                     "that each archangel has.", episodes={"S05": [19]})
        self.archangel_blade.abilities = [ObjectAbilities.can_kill_archangels]

        self.ring_of_pestilence = Object("Ring of Pestilence", description="Can give people diseases of any kind. "
                                                                           "One of the four rings of the Horseman.",
                                         episodes={"S05": [19, 21]})
        self.ring_of_pestilence.abilities = [ObjectAbilities.can_give_incredible_starving_sensation_for_something]

        self.ring_of_death = Object("Ring of Death", description="Can kill anyone. One of the four rings "
                                                                 "of the Horseman.",
                                    episodes={"S05": [21], "S06": [11]})
        self.ring_of_death.abilities = [ObjectAbilities.can_give_incredible_starving_sensation_for_something,
                                        ObjectAbilities.person_with_it_can_teleport]

        self.scythe_of_death = Object("Scythe of Death", description="A weapon used to kill people, demons, "
                                                                     "angels, reapers, etc.", episodes={"S05": [21]})
        self.scythe_of_death.abilities = [ObjectAbilities.can_kill_demons, ObjectAbilities.can_kill_demons,
                                          ObjectAbilities.can_kill_reapers]

        self.combined_rings_of_horseman = Object("Combined rings of Horseman",
                                                 description="All four rings combined into a key to Lucifer's cage.",
                                                 episodes={"S05": [22]})
        self.combined_rings_of_horseman.abilities = [ObjectAbilities.can_open_lucifers_cage_with_a_spell]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 6:

        self.staff_of_moses = Object("Staff of Moses", description="Can cause Egyptian plagues", episodes={"S06": [3]})
        self.staff_of_moses.abilities = [ObjectAbilities.can_cause_egyptian_plague_like_events]

        self.heavens_cristal = Object("Heavens Cristal", description="Crystal, that when used at someone "
                                                                     "(has to be looked at) will turn that person "
                                                                     "into a pillar of salt (like what happened to "
                                                                     "Lot's wife).", episodes={"S06": [3]})
        self.heavens_cristal.abilities = [ObjectAbilities.can_turn_a_person_into_a_pillar_of_salt]

        self.gabriels_horn_of_truth = Object("Gabriel's Horn of truth", description="Can make people speak the truth. "
                                                                                    "Not seen, only mentioned in S06E06.")

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 7:

        self.cursed_ballet_shoes = Object("Cursed ballet shoes", description="When worn, they deprive the person's "
                                                                             "will and cause that person to dance "
                                                                             "without stopping, killing them "
                                                                             "in a process.", episodes={"S07": [16]})
        self.cursed_ballet_shoes.abilities = [ObjectAbilities.fit_their_size_to_a_person, ObjectAbilities.can_teleport,
                                              ObjectAbilities.makes_a_person_dance_until_they_die]
        self.cursed_ballet_shoes.destroy_methods = [ObjectDestroyMethods.take_them_off_to_disable]

        self.cursed_kettle = Object("Cursed kettle", description="When on fire, makes a person drink boiling water.",
                                    episodes={"S07": [16]})
        self.cursed_kettle.abilities = [ObjectAbilities.makes_a_person_drink_boiling_water]

        self.cursed_gramophone = Object("Cursed Gramophone", description="When playing, whispers to people and "
                                                                         "makes them do horrible things.",
                                        episodes={"S07": [16]})
        self.cursed_gramophone.abilities = [ObjectAbilities.can_whisper_to_people,
                                            ObjectAbilities.makes_a_person_do_horrible_things]

        self.cursed_vintage_gentlemans_magazine = Object("Cursed vintage gentleman's magazine",
                                                         description="Only mentioned and in the box in S07E16.")

        self.word_of_god = Object("Word of GOD", description="A stone, that is inscribed with literal Word of God. "
                                                             "Written by Metatron - his scribe. "
                                                             "He took down dictation, when creation was being formed. "
                                                             "There are many words of GOD.", episodes={"S07": [21]})
        self.word_of_god.abilities = [ObjectAbilities.can_cause_storms, ObjectAbilities.can_cause_women_to_go_to_labour,
                                      ObjectAbilities.when_opened_causes_a_person_to_become_a_prophet]

        # SEASON 8:

        # SEASON 9:

        # SEASON 10:

        # SEASON 11:

        # SEASON 12:

        # SEASON 13:

        # SEASON 14:

        # SEASON 15:

        self.objects = [obj for obj in self.__dict__.values() if isinstance(obj, Object)]

    def print_objects_names(self):
        sorted_objects = sorted([obj.name for obj in self.objects])
        print(Colors.RED + Colors.BOLD + "All objects:" + Colors.ENDC)
        for obj in sorted_objects:
            print(" *  " + obj)

    def print_all_objects(self):
        for obj in self.objects:
            obj.print_all()
