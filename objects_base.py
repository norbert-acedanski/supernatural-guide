from colors import Colors
from object import Object
from objects_data import ObjectAbilities, ObjectMaintenance, ObjectDestroyMethods, JohnWinchesterJournal


class ObjectsBase:

    # SEASON 1:

    # TODO: Watch each episode until S04E18 that contains John's journal
    # List of episodes, that the journal appears in:
    # https://supernatural.fandom.com/wiki/John_Winchester%27s_Journal#Appearances
    john_winchesters_journal = Object("John Winchester's Journal",
                                      description="A journal of John Winchester, that contains a lot information about "
                                                  "monsters in Supernatural Universe.",
                                      episodes={"S01": [], "S04": [19], "S06": [1, 8, 12], "S07": [8, 11],
                                                "S08": [8, 12], "S09": [11]})
    john_winchesters_journal._information = {"S04E19": JohnWinchesterJournal.entry_about_johns_other_son,
                                             "S06E12": JohnWinchesterJournal.entry_about_a_skinwalker,
                                             "S08E12": JohnWinchesterJournal.entry_about_torturing_a_demon,
                                             "S09E11": JohnWinchesterJournal.entry_about_killing_a_demon_abaddon_and_locker}

    colt_of_colt = Object("Colt of Colt", description="Colt made by Samuel Colt in 1835, when Halley's Comet was "
                                                      "overhead and the same night those men died at the Alamo. "
                                                      "He made it for a hunter along with 13 bullets. Bullets can be "
                                                      "crafted for this gun. Can kill everything in all creation "
                                                      "except 5 entities: Archangel Lucyfer, unknown 4 left.",
                          episodes={"S01": [20, 21, 22], "S02": [1, 22], "S03": [4, 5, 9], "S05": [10], "S06": [18]})
    colt_of_colt.abilities = [ObjectAbilities.can_kill_anything]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 2:

    charm_against_demons = Object("Charm against demons", description="Fend off possessions. Stops a demon from taking "
                                                                      "a person as a host. Can also be tattooed on "
                                                                      "a body.",
                                  episodes={"S02": [14], "S03": [12], "S08": [2]})
    charm_against_demons.abilities = [ObjectAbilities.unables_possessions]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 3:

    demon_killing_knife = Object("Demon killing knife", description="The knife origins are in the Kurds as stated by "
                                                                    "Henry Winchester in S08E12. Can literally kill "
                                                                    "demons, not get them back to hell. Cannot kill "
                                                                    "certain kinds of demons.",
                                 episodes={"S03": [1, 9, 16], "S04": [1, 9, 20, 22], "S05": [1, 10, 14, 17, 20, 21, 22],
                                           "S06": [10, 20, 21], "S07": [8, 15, 17, 21],
                                           "S08": [1, 2, 7, 10, 14, 17, 19, 23], "S09": [2, 4, 11, 14, 16, 17],
                                           "S10": [2, 3, 7]})
    demon_killing_knife.abilities = [ObjectAbilities.can_kill_demons, ObjectAbilities.cannot_kill_angels,
                                     ObjectAbilities.cannot_kill_knights_of_hell]

    lucky_rabbits_foot = Object("Lucky rabbits foot", description="Person, who touches it becomes incredibly lucky. "
                                                                  "If another person touches it, the previous one "
                                                                  "becomes incredibly unlucky and dies in a week. "
                                                                  "To make one, you have to cut rabbits foot in "
                                                                  "a cemetery under a full moon on a Friday the 13th.",
                                episodes={"S03": [3]})
    lucky_rabbits_foot.abilities = [ObjectAbilities.grants_incredible_luck]
    lucky_rabbits_foot.destroy_methods = [ObjectDestroyMethods.burn_it]

    sleep_potion = Object("Sleep Potion", description="Made of African Dream Root. Was use by shaman and medicine men "
                                                      "for centuries. It is used for dream-walking - entering another "
                                                      "person's dreams.", episodes={"S03": [10], "S08": [20]})
    sleep_potion.abilities = [ObjectAbilities.can_make_a_person_sleep_for_days,
                              ObjectAbilities.brings_back_dreams_for_those_that_dont_have_them,
                              ObjectAbilities.gives_people_control_over_dreams,
                              ObjectAbilities.allows_to_enter_another_persons_dream]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 4:

    sigil_against_angels = Object("Sigil against angels", description="Sigil made with blood, that can send angels "
                                                                      "back to heaven. Can be used to send back "
                                                                      "a specific angel type.",
                                  # TODO: Check where else is the sigil used
                                  episodes={"S04": [10, 22], "S05": [13, 18], "S06": [3], "S07": [21], "S09": [1]})
    sigil_against_angels.abilities = [ObjectAbilities.can_send_angels_back_to_heaven]

    angel_grace = Object("Angel grace", description="A power source for an angel. Another Angel can take the Grace to "
                                                    "power itself, but it does not last forever. When it burns up it "
                                                    "has to be refilled.", episodes={"S04": [10], "S08": [23],
                                                                                     "S10": [3]})
    angel_grace.abilities = [ObjectAbilities.can_appear_as_falling_meteor,
                             ObjectAbilities.the_place_it_hits_is_not_destroyed_but_flourishes,
                             ObjectAbilities.can_kill_entities_when_reconnecting_with_an_angel]

    reaper_imprison_sigil = Object("Reaper imprison sigil", description="Sigil, that can trap a reaper.",
                                   episodes={"S04": [15]})
    reaper_imprison_sigil.abilities = [ObjectAbilities.traps_a_reaper]

    angel_protection_sigil = Object("Angel protection sigil", description="Angels can't get past it, when the place is "
                                                                          "marked with it.",
                                    # TODO: Check where else is the sigil used
                                    episodes={"S04": [15], "S09": [1, 18]})
    angel_protection_sigil.abilities = [ObjectAbilities.angels_cant_get_past_it]

    angel_blade = Object("Angel blade", description="A triangular, silvery blade, that each angel has.",
                         episodes={"S04": [16], "S05": [1, 13, 18], "S06": [3, 10, 17, 18, 22], "S07": [21],
                                   "S08": [7, 10, 17, 21, 22, 23], "S09": [1, 2, 3, 6, 9, 10, 11, 14, 16, 18, 21, 22, 23],
                                   "S10": [1, 3, 7, 9, 10, 13]})
    angel_blade.abilities = [ObjectAbilities.can_kill_angels, ObjectAbilities.can_kill_demons]

    lucifers_cage = Object("Lucifer's Cage", description="A prison build specifically to contain archangelic powers "
                                                         "(not seen yet). Can be opened with all 4 rings of "
                                                         "the horseman. There is fire there.", episodes={"S06": [13]})
    lucifers_cage.abilities = [ObjectAbilities.traps_an_archangel, ObjectAbilities.traps_a_soul_of_a_person]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 5:

    sword_of_archangel_michael = Object("Sword of Archangel Michael", description="A vessel, that Archangel Michael "
                                                                                  "possesses - a very special person, "
                                                                                  "that can hold archangels power.",
                                        episodes={"S05": [1]})

    enochian_sigil = Object("Enochian Sigil", description="Hides from every angel in creation (archangels included).",
                            episodes={"S05": [1, 2]})
    enochian_sigil.abilities = [ObjectAbilities.hides_a_person_from_all_angels]

    magic_amulet = Object("Magic Amulet", description="It burns hot in God's presence. It is an Amulet, that Sam gave "
                                                      "Dean, when they were kids.",
                          episodes={"S03": [8], "S05": [2, 16]})

    ring_of_war = Object("Ring of War", description="Can give people hallucinations. One of the four rings of "
                                                    "the Horseman.", episodes={"S05": [2]})
    ring_of_war.abilities = [ObjectAbilities.can_give_hallucinations]

    human_soul = Object("Human soul", description="As an object is very bright. Can be collected of a person. Released "
                                                  "soul of a person will find a way back to a body.",
                        episodes={"S05": [14], "S06": [11], "S08": [19], "S09": [17]})

    ring_of_famine = Object("Ring of Famine", description="Can give people starving sensation for things they "
                                                          "lack/desire. One of the four rings of the Horseman.",
                            episodes={"S05": [14]})
    ring_of_famine.abilities = [ObjectAbilities.can_give_incredible_starving_sensation_for_something]

    archangel_blade = Object("Archangel blade", description="A triangular, silvery blade, that each archangel has.",
                             episodes={"S05": [19]})
    archangel_blade.abilities = [ObjectAbilities.can_kill_archangels]

    ring_of_pestilence = Object("Ring of Pestilence", description="Can give people diseases of any kind. One of the "
                                                                  "four rings of the Horseman.",
                                episodes={"S05": [19, 21]})
    ring_of_pestilence.abilities = [ObjectAbilities.can_give_incredible_starving_sensation_for_something]

    ring_of_death = Object("Ring of Death", description="Can kill anyone. One of the four rings of the Horseman.",
                           episodes={"S05": [21], "S06": [11]})
    ring_of_death.abilities = [ObjectAbilities.can_give_incredible_starving_sensation_for_something,
                               ObjectAbilities.person_with_it_can_teleport]

    scythe_of_death = Object("Scythe of Death", description="A weapon used to kill people, demons, angels, reapers, "
                                                            "etc.", episodes={"S05": [21]})
    scythe_of_death.abilities = [ObjectAbilities.can_kill_demons, ObjectAbilities.can_kill_demons,
                                 ObjectAbilities.can_kill_reapers]

    combined_rings_of_horseman = Object("Combined rings of Horseman", description="All four rings combined into a key "
                                                                                  "to Lucifer's cage.",
                                        episodes={"S05": [22]})
    combined_rings_of_horseman.abilities = [ObjectAbilities.can_open_lucifers_cage_with_a_spell]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 6:

    staff_of_moses = Object("Staff of Moses", description="Can cause Egyptian plagues", episodes={"S06": [3]})
    staff_of_moses.abilities = [ObjectAbilities.can_cause_egyptian_plague_like_events]

    heavens_cristal = Object("Heavens Cristal", description="Crystal, that when used at someone (has to be looked at) "
                                                            "will turn that person into a pillar of salt (like what "
                                                            "happened to Lot's wife).", episodes={"S06": [3]})
    heavens_cristal.abilities = [ObjectAbilities.can_turn_a_person_into_a_pillar_of_salt]

    gabriels_horn_of_truth = Object("Gabriel's Horn of truth",
                                    description="Can make people speak the truth. Mentioned in S06E06. It can be used "
                                                "to attract Angels with help of a spell. Ingredients are a drawn "
                                                "symbol, Griffin feathers and bones of a Fairy (no matter what realm "
                                                "they're from - according to Gadreel).", episodes={"S09": [18]})
    gabriels_horn_of_truth.abilities = [ObjectAbilities.can_attract_angels]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 7:

    cursed_ballet_shoes = Object("Cursed ballet shoes", description="When worn, they deprive the person's will and "
                                                                    "cause that person to dance without stopping, "
                                                                    "killing them in a process.",
                                 episodes={"S07": [16]})
    cursed_ballet_shoes.abilities = [ObjectAbilities.fit_their_size_to_a_person, ObjectAbilities.can_teleport,
                                     ObjectAbilities.makes_a_person_dance_until_they_die]
    cursed_ballet_shoes.destroy_methods = [ObjectDestroyMethods.take_them_off_to_disable]

    cursed_kettle = Object("Cursed kettle", description="When on fire, makes a person drink boiling water.",
                           episodes={"S07": [16]})
    cursed_kettle.abilities = [ObjectAbilities.makes_a_person_drink_boiling_water]

    cursed_gramophone = Object("Cursed Gramophone", description="When playing, whispers to people and makes them do "
                                                                "horrible things.", episodes={"S07": [16]})
    cursed_gramophone.abilities = [ObjectAbilities.can_whisper_to_people,
                                   ObjectAbilities.makes_a_person_do_horrible_things]

    cursed_vintage_gentlemans_magazine = Object("Cursed vintage gentleman's magazine",
                                                description="Only mentioned and in the box in S07E16.")

    word_of_god = Object("Word of GOD", description="A stone, that is inscribed with literal Word of God. "
                                                    "Written by Angel Metatron - his scribe. He took down dictation, "
                                                    "when creation was being formed. There are many words of GOD. "
                                                    "Words of GOD are inscribed in angel cores. "
                                                    "First found Word of God has information on Leviathans "
                                                    "and how to kill them. "
                                                    "Second tablet has information about Demons, how to kill them "
                                                    "and how to close the Gates of Hell. "
                                                    "Third tablet (inscribed in angel core and stashed in stone form "
                                                    "by Lucyfer) has information about Angels and how to make "
                                                    "them fall. Found in Lucyfer crypt in S08E17.",
                         episodes={"S07": [21], "S08": [1, 2, 10, 17, 21, 23], "S09": [9, 10, 23]})
    word_of_god.abilities = [ObjectAbilities.can_cause_storms, ObjectAbilities.can_cause_women_to_go_to_labour,
                             ObjectAbilities.when_opened_causes_a_person_to_become_a_prophet]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 8:

    mjolnir = Object("Mjolnir", description="The hammer of Thor.", episodes={"S08": [2]})
    mjolnir.abilities = [ObjectAbilities.can_kill_pagan_gods]

    demonic_handcuffs = Object("Demonic handcuffs", description="When worn by a Demon, it cannot teleport, "
                                                                "leave the body or use demon magic.",
                               episodes={"S08": [23], "S09": [10, 14, 16], "S10": [2]})
    demonic_handcuffs.abilities = [ObjectAbilities.traps_a_demon]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 9:

    key_to_ozz = Object("Key to Ozz", description="Inserted into any door, opens a portal to Ozz (a golden path). "
                                                  "There were 6 keys forged from Ozz steel and can only be repaired in "
                                                  "that magical realm (according to Clive Dillon).",
                        episodes={"S09": [4], "S10": [11]})
    key_to_ozz.abilities = [ObjectAbilities.can_open_portal_to_ozz]

    possessing_angel_weakening_sigil = Object("Possessing Angel weakening sigil",
                                              description="A Sigil, that allows to temporarily hobble an angel, that "
                                                          "possesses a human - leaving him no control over the vessel. "
                                                          "When altered - does not work as it should.",
                                              episodes={"S09": [9]})
    possessing_angel_weakening_sigil.abilities = [ObjectAbilities.can_temporarily_weaken_a_possessing_angel]

    first_blade = Object("First Blade", description="First weapon used to kill the first human victim. Archangels used "
                                                    "it to kill the Knights of Hell. That is what everyone thinks "
                                                    "happened. The truth is, Cain killed Knights of Hell with it. "
                                                    "A spell consisting of 6 elements, one of which is essence of "
                                                    "Kraken. A mixture of ingredients should be poured out on a map "
                                                    "and lit with a match. The blade is a part of a jaw of an animal. "
                                                    "The first blade has to be used with a Mark of Cain. Without the "
                                                    "mark, the blade is useless. When a man with the Mark of Cain "
                                                    "holds the blade, the mark starts to shine red. A person with Mark "
                                                    "of Cain can telekinetically bring the blade to himself.",
                         episodes={"S09": [11, 16, 21, 22, 23], "S10": [1, 2, 10, 13]})
    first_blade.abilities = [ObjectAbilities.can_kill_knights_of_hell, ObjectAbilities.can_kill_reapers,
                             ObjectAbilities.can_kill_angels]

    energy_focusing_sigil = Object("Energy Focusing Sigil", description="A spell, that allows to focus energy (for "
                                                                        "example killed angel can focus the energy to "
                                                                        "kill people and other angels.",
                                   episodes={"S09": [22, 23]})
    energy_focusing_sigil.abilities = [ObjectAbilities.can_focus_energy]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 10:
    inner_key_of_ozz = Object("Inner Key of Ozz", description="Object, that can enter a soul of a person and unleash "
                                                              "his/her darkness (Create good and bad people out of one "
                                                              "soul). Can also be used to bind two halves back "
                                                              "together.")
    inner_key_of_ozz.abilities = [ObjectAbilities.can_split_soul_into_good_and_bad_parts,
                                  ObjectAbilities.can_bind_split_soul_back_together]

    # SEASON 11:

    # SEASON 12:

    # SEASON 13:

    # SEASON 14:

    # SEASON 15:

    def __init__(self):
        self.objects = [obj for obj in self.__class__.__dict__.values() if isinstance(obj, Object)]
        self.abilities = [ability for key, ability in list(ObjectAbilities.__dict__.items())
                          if not key.startswith("__")]
        self.maintenance_methods = [method for key, method in list(ObjectMaintenance.__dict__.items())
                                    if not key.startswith("__")]

    def print_objects_names(self):
        sorted_objects = sorted([obj.name for obj in self.objects])
        print(Colors.RED + Colors.BOLD + "All objects:" + Colors.ENDC)
        for obj in sorted_objects:
            print(" *  " + obj)

    def print_all_objects(self):
        for obj in self.objects:
            obj.print_all()
