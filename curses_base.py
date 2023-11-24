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

    reaper_death_summoning_spell = Curse("Reaper Death summoning spell",
                                         description="Can summon Angel of Death from its prison. Requires a place, "
                                                     "where an awful carnage has happened. It ha to be performed at "
                                                     "midnight. Requires sacrifice of a lot of people and demons.",
                                         episodes={"S05": [10], "S10": [23]})
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
                              episodes={"S08": [12], "S09": [21], "S12": [13]})
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

    demon_curing_spell = Curse("Demon-curing spell", description="Spell used by Father Thompson to cure a demon. One "
                                                                 "has to inject 8 doses of purified blood (from a man, "
                                                                 "that was in a confession, but blood consecrated by "
                                                                 "a priest will do) into a demon separated by one hour "
                                                                 "breaks.", episodes={"S09": [23], "S10": [3]})

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

    angel_tracking_spell_with_grace = Curse("Angel tracking spell with a Grace",
                                            description="Spell, that allows to track an angel. Is performed with "
                                                        "a part of the Grace of an Angel, that left his vessel after "
                                                        "extracting it. Ingredients are put in the bowl with Grace as "
                                                        "last ingredient.", episodes={"S09": [11]})

    mark_of_cain = Curse("Mark of Cain", description="A curse, that Lucyfer himself put on Cain for killing his "
                                                     "brother. It looks like a mirrored version of the letter 'F' with "
                                                     "additional horizontal line. A mark can be transferred to "
                                                     "another person that is worthy of it (a killer). When a man with "
                                                     "the Mark of Cain holds the blade, the mark starts to shine red. "
                                                     "A person with the Mark of Cain (holding the First Blade) can "
                                                     "counteract telekinetic abilities of a Knights of Hell. That "
                                                     "person can also telekinetically bring the blade to himself. If a "
                                                     "person with the Mark of Cain is killed - he becomes a demon "
                                                     "(according to the ending of S09E23). According to Metatron it is "
                                                     "God-level (or Lucyfer-level) magic. The book of the Damned is "
                                                     "calling to the person with the Mark of Cain. According to Reaper "
                                                     "Death, nothing can kill a person, that has the Mark. GOD created "
                                                     "the Mark, that would serve as both lock and key, which he "
                                                     "entrusted to his most valued lieutenant - Lucifer, but the Mark "
                                                     "began to assert its own will, revealed itself as the First Curse "
                                                     "and began to corrupt. Lucyfer became jealous of Man and GOD "
                                                     "banished him to Hell. Mark of Cain is removed in S10E23.",
                         episodes={"S09": [11, 12, 16, 17, 18, 21],
                                   "S10": [1, 2, 3, 9, 10, 11, 12, 13, 17, 18, 21, 22, 23], "S11": [1, 2, 5, 6, 9]})
    mark_of_cain.clues = [CursesClues.people_acting_weirdly, CursesClues.less_affected_by_telekinesis_of_knight_of_hell,
                          CursesClues.high_strength, CursesClues.black_eyes, CursesClues.increased_regeneration,
                          CursesClues.weird_dreams]
    mark_of_cain.disable_methods = [CursesDisableMethods.age_changing_spell]

    willpower_removing_spell = Curse("Willpower removing spell", description="Spell, that lowers or removes the power "
                                                                             "of will of a person. Used by Magnus.",
                                     episodes={"S09": [16]})
    willpower_removing_spell.clues = [CursesClues.people_acting_weirdly, CursesClues.people_doing_what_they_are_told]
    willpower_removing_spell.disable_methods = [CursesDisableMethods.wait_for_it_to_pass]

    angel_siren_spell = Curse("Angel Siren spell", description="Spell used to attract Angels. Made of a symbol "
                                                               "combined with Griffin feathers, bones of a Fairy and "
                                                               "most importantly - Gabriel's horn.")
    angel_siren_spell.clues = [CursesClues.people_dead_weirdly]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 10:

    defigere_et_depurgare_spell = Curse("Defigere et depurgare spell", description="'To bind and purge' spell. Used to "
                                                                                   "kill demons.",
                                        episodes={"S10": [7]})
    defigere_et_depurgare_spell.clues = [CursesClues.people_dead_weirdly, CursesClues.black_goo]

    attack_dog_spell = Curse("Attack-dog spell", description="Used on a human/angel to turn him into an attack dog. "
                                                             "Human after a while will die because of it, an angel can "
                                                             "withstand the power.",
                             episodes={"S10": [7, 23], "S11": [1, 2, 3]})
    attack_dog_spell.clues = [CursesClues.people_acting_weirdly, CursesClues.high_strength, CursesClues.red_eyes]
    attack_dog_spell.disable_methods = [CursesDisableMethods.rowenas_attack_dog_disable_spell]

    spirit_leaving_body_spell = Curse("Spirit leaving body spell",
                                      description="Spell, that allows ones spirit to leave the body and go to another "
                                                  "person. One needs another persons belonging to cast the spell.",
                                      episodes={"S10": [10]})
    spirit_leaving_body_spell.clues = [CursesClues.white_eyes]

    age_changing_spell = Curse("Age changing spell", description="Spell, that allows to change a persons age (to a "
                                                                 "previous one - so make people younger), by "
                                                                 "physically making their bodies as they were in that "
                                                                 "age.", episodes={"S10": [12]})
    age_changing_spell.clues = [CursesClues.can_make_people_younger, CursesClues.hex_bag_hidden_somewhere]
    age_changing_spell.disable_methods = [CursesDisableMethods.squeeze_the_hex]

    mark_of_cain_removing_spell = Curse("Mark of Cain removing spell",
                                        description="Spell, that allows to remove the Mark of Cain completely out of "
                                                    "a person. There are a few ingredients required: 'Something made "
                                                    "by GOD, but forbidden to man' - The Forbidden Fruit (Quince), "
                                                    "'Something made by man, but forbidden by GOD' - The Golden Calf, "
                                                    "'Something you love' - kill the thing you love the most and "
                                                    "a genetic material of the person, that has the Mark.",
                                        episodes={"S10": [23]})
    rowenas_immobilization_spell = Curse("Rowena's immobilization spell",
                                         description="Spell, that allows to immobilize entities such as Demons and "
                                                     "Angels.", episodes={"S10": [23]})

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 11:

    talking_to_being_in_lucifers_cage_spell = Curse("Talking to being in Lucifer's Cage spell",
                                                    description="Spell, that allows to communicate with a being, that "
                                                                "is in Lucifer's cage. It is found in the Book of the "
                                                                "Damned by Rowena in S11E09.", episodes={"S11": [9]})
    talking_to_being_in_lucifers_cage_spell.disable_methods = [CursesDisableMethods.will_of_lucifer]

    kiss_of_death = Curse("Kiss of death", description="Aramaic curse. It is transmittable, the last person, that got "
                                                       "kissed - dies. To make yourself safe, you have to kiss another "
                                                       "person, but if that person dies, the curse comes back for you.",
                          episodes={"S11": [13]})
    kiss_of_death.clues = [CursesClues.sealed_with_a_kiss, CursesClues.the_last_person_that_got_kissed_dies]
    kiss_of_death.disable_methods = [CursesDisableMethods.kill_the_witch_that_cursed_a_person]

    spell_of_gathering = Curse("Spell of Gathering", description="It's an incantation used to 'focus power of "
                                                                 "celestial beings against all drawn forms of "
                                                                 "evasion.' The spell was designed to clear all "
                                                                 "mystical or occult blockages. It requires a power of "
                                                                 "an archangel.", episodes={"S11": [14]})

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 12:

    memory_curse = Curse("Memory curse", description="When a person is cursed, their memory slowly fades away. First "
                                                     "little things fade away, later person forgets habits, their "
                                                     "name, things they do for a long time. Then they forget how to "
                                                     "speak, how to swallow and breathe. Eventually becoming a child. "
                                                     "Curse is casted via an archaic Celtic Glyphs - Ogham Chraobh. "
                                                     "The Druids used it in their rituals calling it the Language of "
                                                     "the Trees. There is only one family of witches, that does this "
                                                     "magic - Loughlin family. Rowena knows them a bit. Members are "
                                                     "Gideon, Boyd and Catriona (children). Family possessed a "
                                                     "powerful book of Druidic magic called the Black Grimoire.",
                         episodes={"S12": [11]})
    memory_curse.clues = [CursesClues.slow_loss_of_the_memory]
    memory_curse.disable_methods = [CursesDisableMethods.grimoire_spell]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 13:

    spell_to_travel_to_alternate_timeline = Curse("Spell to travel to alternate timeline",
                                                  description="Spell allows one person to travel to alternate "
                                                              "timeline. There is only one type of spell, but one was "
                                                              "faked by Donatello. The right on requires four major "
                                                              "ingredients: Archangel Grace, a fruit from the Tree of "
                                                              "Life, the Seal of Solomon (purple gem, that was found "
                                                              "by Men of Letters), the blood of 'a most holy man' and "
                                                              "something, that has been there. "
                                                              "The second one was faked by Donatello, but what he "
                                                              "wrote is as follows: Cleanse the Holy Altar with "
                                                              "sacramental water, built on a bed of Godsroot. Bless "
                                                              "the Altar in the tongue of GOD, coat a bronze bowl with "
                                                              "the Oil of Bramelin, combine Dragon's Blood, Wolfsbane, "
                                                              "Angelica root and crush into a fine paste. Sprinkle "
                                                              "with Goofer dust. <Unknown> Mortar and Pescle, combine "
                                                              "Dead Sea brine, Virgin Lamb's blood and the bone? of a "
                                                              "lesser saint. <Unknown> mixture, paint three symbols "
                                                              "<unknown> surrounding the Altar. <Unknown> pastes into "
                                                              "the <unknown>. Mix thoroughly, top with dried "
                                                              "<unknown>. Recipe from S13E14 from the page, that "
                                                              "Donatello deciphered from the Demon Tablet. The portal "
                                                              "stays open for 24h. If too small amount of Grace is "
                                                              "used, the rift stays open for very litle time (even a "
                                                              "few seconds).",
                                                  episodes={"S13": [7, 14, 17, 21, 22]})
    spell_to_travel_to_alternate_timeline.clues = [CursesClues.rip_in_the_air]
    spell_to_travel_to_alternate_timeline.disable_methods = [CursesDisableMethods.wait_for_it_to_pass]

    nephilim_tracking_spell = Curse("Nephilim tracking spell",
                                    description="Spell, that allows to track a Nephilim. It dates back to the time of "
                                                "King Solomon, who commissioned it to keep tabs on Queen of Sheba, who "
                                                "according to the lore was half-angel.", episodes={"S13": [8]})

    love_spell = Curse("Love spell", description="A spell, that allows a person to fall in love in another person.",
                       episodes={"S13": [11]})
    love_spell.clues = [CursesClues.blinding_love, CursesClues.people_acting_weirdly, CursesClues.people_dead_weirdly,
                        CursesClues.hex_bag_hidden_somewhere]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # SEASON 14:

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

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
