import difflib
import re
from typing import List

from monster import Monster
from monsters_data import MonstersClues, MonstersKillMethods, MonstersDisableMethods, MonstersCureMethods
from colors import Colors


class MonsterBase:
    # ---------------------------------------------------- SEASON 1 ----------------------------------------------------

    prince_of_hell = Monster("Prince of Hell", description="The oldest of old demons. One generation after Lilith. "
                                                           "They were turned by Lucyfer himself before the Atlantis "
                                                           "drowned. They were trained to be demonic generals in the "
                                                           "war against Heaven. Azazel - the yellow eyed demon that "
                                                           "made people with abilities, Ramiel, Asmodeus, Dagon. "
                                                           "Azazel was killed by Dean in S02E22. Ramiel is the second "
                                                           "Prince Winchesters encounter. Dagon appears in S12E13. She "
                                                           "is mostly known for her psychotic savagery. Dagon is "
                                                           "killed by Castiel and the power of Nephilim in S12E19. "
                                                           "Asmodeus appears in S13E02. Prince of Hell can improve his "
                                                           "power by ingesting Archangel Grace. Asmodeus is killed in "
                                                           "S13E18 by Archangel Gabriel.",
                             episodes={"S01": [1, 21, 22], "S02": [1, 21, 22], "S04": [3, 22], "S06": [1],
                                       "S12": [12, 13, 17, 19], "S13": [2, 7, 13, 17, 18]})
    # TODO: Check in which episodes does Azazel appear
    prince_of_hell.clues = [MonstersClues.people_burned_on_the_ceiling, MonstersClues.can_appear_out_of_thin_air,
                            MonstersClues.weird_things_behavior, MonstersClues.yellow_eyes, MonstersClues.weird_weather,
                            MonstersClues.children_of_victims_that_died_on_the_ceiling_have_abilities,
                            MonstersClues.mothers_burned_when_children_are_6_months_old, MonstersClues.cattle_deaths,
                            MonstersClues.one_can_make_a_deal_with_it, MonstersClues.angel_blade_is_ineffective,
                            MonstersClues.holy_water_does_not_affect_it, MonstersClues.travels_as_black_fog,
                            MonstersClues.can_posses_a_reaper, MonstersClues.can_make_themselves_appear_as_they_like,
                            MonstersClues.can_show_past_to_people, MonstersClues.demon_killing_knife_is_ineffective,
                            MonstersClues.can_kill_angels_with_a_touch, MonstersClues.temperature_fluctuations,
                            MonstersClues.telekinesis, MonstersClues.invulnerable, MonstersClues.can_teleport_people,
                            MonstersClues.can_kill_demons_with_power_of_will, MonstersClues.electrical_storms,
                            MonstersClues.can_vanish, MonstersClues.high_strength, MonstersClues.people_acting_weirdly,
                            MonstersClues.can_kill_people_with_a_thought, MonstersClues.mimics_human_voice,
                            MonstersClues.lack_of_body_control, MonstersClues.can_hurt_people_with_a_thought]
    prince_of_hell.kill_methods = [MonstersKillMethods.colt_of_colt_with_magic_bullets,
                                   MonstersKillMethods.lance_of_archangel_michael,
                                   MonstersKillMethods.will_of_a_nephilim, MonstersKillMethods.will_of_an_archangel]

    vengeful_spirit = Monster("Vengeful Spirit or Ghost (Bloody Mary, Hook Man)",
                              description="Appears, when somebody died tragically, committed suicide or was killed "
                                          "violently. Usually bound to a place or to things. Ghost can occasionally "
                                          "possess people. When they do, sometimes they can travel for a while before "
                                          "coming back to the usual haunting place. Can be summoned by Enochian, "
                                          "necromantic summoning rituals. Sometimes it's a spirit of a person, that is "
                                          "in the coma. Ghosts can be forced to rise and keep risen. "
                                          "If it is done with very powerful spell, then a Mark of Witness remains on "
                                          "them if t hey were killed by supernatural. Witnesses can be put to rest "
                                          "by a special spell (has to be cast over an open fire). A Ghost can be bound "
                                          "to an object, place or even electrical signals (like Wi-Fi).",
                              episodes={"S01": [1, 3, 5, 7, 9, 10, 13, 19], "S02": [6, 11, 16, 18, 19, 22],
                                        "S03": [5, 6, 13], "S04": [2, 7, 13, 15, 17], "S05": [9, 11, 12],
                                        "S06": [4, 11, 14], "S07": [4, 7, 10, 13, 17, 19], "S09": [7], "S10": [13, 16],
                                        "S11": [7, 23], "S12": [3, 6, 13], "S13": [5, 16], "S14": [4, 12, 13, 20],
                                        "S15": [1, 2, 3, 6]})
    vengeful_spirit.clues = [MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                             MonstersClues.people_dead_weirdly, MonstersClues.ghost_like_creature,
                             MonstersClues.weird_electronics_behavior, MonstersClues.weird_things_behavior,
                             MonstersClues.local_legend_about_somebody_killed_or_died, MonstersClues.ectoplasm,
                             MonstersClues.telekinesis, MonstersClues.invisible_entity, MonstersClues.emf,
                             MonstersClues.missing_body, MonstersClues.high_strength, MonstersClues.cold_spots,
                             MonstersClues.can_control_water, MonstersClues.people_seeing_things_or_figures,
                             MonstersClues.summoned_by_saying_bloody_marry_in_front_of_the_mirror,
                             MonstersClues.objects_seen_in_night_vision, MonstersClues.can_posses_a_person,
                             MonstersClues.missing_or_dead_people_regularly_in_the_same_area, MonstersClues.ozone_smell,
                             MonstersClues.seen_as_fire, MonstersClues.no_sulfur, MonstersClues.people_acting_weirdly,
                             MonstersClues.small_earth_quake, MonstersClues.seen_as_car_or_truck,
                             MonstersClues.flashing_lights, MonstersClues.seen_as_a_little_girl, MonstersClues.suicides,
                             MonstersClues.seen_as_a_drown_man, MonstersClues.strange_different_things_happening,
                             MonstersClues.no_missing_heart, MonstersClues.body_torn_apart, MonstersClues.no_black_fog,
                             MonstersClues.visions, MonstersClues.lack_of_body_control, MonstersClues.scars_on_victims,
                             MonstersClues.weird_fire_spontaneous_combustion, MonstersClues.can_control_electronics,
                             MonstersClues.can_absorb_other_ghost_energy, MonstersClues.victims_hear_voices,
                             MonstersClues.no_hex_bags, MonstersClues.travels_as_grey_fog, MonstersClues.weird_noises,
                             MonstersClues.amnesia_blackout, MonstersClues.holy_water_does_not_affect_it,
                             MonstersClues.attached_to_a_specific_object, MonstersClues.victims_hear_children_cry,
                             MonstersClues.leaves_frozen_marks, MonstersClues.frozen_heart,
                             MonstersClues.can_put_a_person_into_a_tv, MonstersClues.can_put_an_angel_into_a_tv]
    vengeful_spirit.disable_methods = [MonstersDisableMethods.bring_the_spirit_to_its_crime_place,
                                       MonstersDisableMethods.bring_the_spirit_what_it_wants,
                                       MonstersDisableMethods.iron_or_iron_bullets,
                                       MonstersDisableMethods.salt_or_salted_bullets, MonstersDisableMethods.holy_oil,
                                       MonstersDisableMethods.finish_its_unfinished_business]
    vengeful_spirit.kill_methods = [MonstersKillMethods.burn_salted_corpse,
                                    MonstersKillMethods.destroy_the_object_that_the_ghost_is_bound_to]

    wendigo = Monster("Wendigo", description="Wending in Cree Indian means 'evil, that devours'. These creatures can "
                                             "live to hundreds of years. Each Wendigo was once a man. It's a product "
                                             "of a cannibalism - people in camps/mineshafts/tribes due to lack of "
                                             "supplies eat others. Stores other man as a supply for winters as food.",
                      episodes={"S01": [2]})
    wendigo.clues = [MonstersClues.missing_or_dead_people_regularly_in_the_same_area, MonstersClues.moves_fast,
                     MonstersClues.strange_roar, MonstersClues.attacks_at_night, MonstersClues.able_to_use_doors,
                     MonstersClues.intelligent, MonstersClues.claws, MonstersClues.animal_like_attack,
                     MonstersClues.silent_area, MonstersClues.high_strength, MonstersClues.mimics_human_voice]
    wendigo.disable_methods = [MonstersDisableMethods.symbols_of_anasazi]
    wendigo.kill_methods = [MonstersKillMethods.burn_it]

    skinwalker = Monster("Skinwalker", description="Can change into an animal anytime. Can infect other people with a "
                                                   "single bite. Basically a werewolf cousin. Mentioned in S01E02.",
                         episodes={"S06": [8]})
    skinwalker.clues = [MonstersClues.claws, MonstersClues.moves_fast, MonstersClues.people_dead_weirdly,
                        MonstersClues.animal_like_attack, MonstersClues.missing_heart, MonstersClues.body_torn_apart,
                        MonstersClues.murders_not_during_full_moon_week, MonstersClues.can_change_into_a_dog,
                        MonstersClues.great_sense_of_smell]
    skinwalker.disable_methods = [MonstersDisableMethods.silver_or_silver_bullets]
    skinwalker.kill_methods = [MonstersKillMethods.silver_bullet_into_the_heart]

    black_dog = Monster("Black Dog", description="Not seen. Only mentioned in S01E02 and S02E08")
    black_dog.clues = [MonstersClues.claws, MonstersClues.moves_fast, MonstersClues.victims_see_black_dogs]

    water_wraith = Monster("Water Wraith", description="Not seen. Only mentioned in S01E03")
    water_wraith.clues = [MonstersClues.can_control_water]

    demon = Monster("Demon", description="In every religion there is information about demonic possessions. Demons are "
                                         "man that were stuck in Hell for a long time. A demon can be cured by "
                                         "Father Thompson's curing ritual.",
                    episodes={"S01": [4, 16, 21, 22], "S02": [1, 9, 14, 22], "S03": [1, 2, 4, 9, 12, 15, 16],
                              "S04": [1, 2, 3, 4, 9, 10, 12, 15, 16, 20, 21, 22],
                              "S05": [1, 6, 10, 12, 14, 17, 20, 21, 22], "S06": [7, 10, 18, 19, 20, 21, 22],
                              "S07": [8, 15, 17, 21, 23], "S08": [1, 2, 7, 10, 17, 19, 21, 22, 23],
                              "S09": [2, 6, 10, 11, 14, 16, 17, 21, 23], "S10": [1, 2, 3, 7, 9, 10, 13, 14, 16, 17, 21],
                              "S11": [1, 3, 6, 9, 10, 14, 15, 18, 22], "S12": [1, 2, 12, 15, 17, 21],
                              "S13": [2, 7, 8, 12, 13, 17, 18], "S14": [1, 11, 17, 20], "S15": [1, 2, 3, 8, 13]})
    demon.clues = [MonstersClues.black_eyes, MonstersClues.travels_as_black_fog, MonstersClues.emf,
                   MonstersClues.weird_electronics_behavior, MonstersClues.high_strength, MonstersClues.sulfur,
                   MonstersClues.burned_by_holy_water, MonstersClues.reacts_to_gods_name_in_latin,
                   MonstersClues.people_dead_weirdly, MonstersClues.with_a_binding_link_exorcism_does_not_work,
                   MonstersClues.people_acting_weirdly, MonstersClues.can_appear_out_of_thin_air,
                   MonstersClues.amnesia_blackout, MonstersClues.telekinesis, MonstersClues.can_vanish,
                   MonstersClues.lack_of_body_control, MonstersClues.can_hurt_people_with_a_thought,
                   MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                   MonstersClues.animals_dead_weirdly, MonstersClues.weird_things_behavior,

                   MonstersClues.black_blood]
    demon.kill_methods = [MonstersKillMethods.demon_killing_knife, MonstersKillMethods.angel_exorcism,
                          MonstersKillMethods.colt_of_colt_with_magic_bullets, MonstersKillMethods.demon_killing_spell,
                          MonstersKillMethods.angel_blade, MonstersKillMethods.first_blade, MonstersKillMethods.holy_oil,
                          MonstersKillMethods.defigere_et_depurgare_spell, MonstersKillMethods.will_of_an_archangel,

                          MonstersKillMethods.lance_of_archangel_michael]
    demon.disable_methods = [MonstersDisableMethods.holy_water, MonstersDisableMethods.holy_wood,
                             MonstersDisableMethods.exorcism, MonstersDisableMethods.devils_trap,
                             MonstersDisableMethods.witch_spell_to_get_a_demon_out_of_the_body,
                             MonstersDisableMethods.salt_or_salted_bullets, MonstersDisableMethods.demon_killing_knife,
                             MonstersDisableMethods.extrusion_by_people_with_abilities]

    shapeshifter = Monster("Shapeshifter", description="These creatures can transform themselves into other man or "
                                                       "animals. Can mate with humans (and other Shapeshifters) to "
                                                       "produce Shapeshifter offspring.",
                           episodes={"S01": [6], "S02": [12], "S04": [5], "S06": [2], "S09": [16, 20], "S10": [6],
                                     "S12": [20], "S13": [4, 10], "S15": [10]})
    shapeshifter.clues = [MonstersClues.can_take_form_of_other_people, MonstersClues.skin_left_behind,
                          MonstersClues.being_at_two_places_at_once, MonstersClues.bright_eyes, MonstersClues.no_sulfur,
                          MonstersClues.weird_animal_behavior, MonstersClues.can_copy_memories_of_other_people,
                          MonstersClues.people_dead_weirdly, MonstersClues.strange_different_things_happening,
                          MonstersClues.can_make_themselves_appear_as_they_like, MonstersClues.silver_burns_its_skin,
                          MonstersClues.no_emf, MonstersClues.missing_or_dead_people_regularly_in_the_same_area,
                          MonstersClues.high_strength, MonstersClues.no_flashing_lights, MonstersClues.no_cold_spots,
                          MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                          MonstersClues.no_missing_body]
    shapeshifter.kill_methods = [MonstersKillMethods.silver_bullet_into_the_heart, MonstersKillMethods.silver_blade,
                                 MonstersKillMethods.will_of_a_nephilim]
    shapeshifter.disable_methods = [MonstersDisableMethods.silver_or_silver_bullets]

    psychic = Monster("Psychic", description="A person, that can read minds, knows past, present and future of people "
                                             "or in general. Senses energies and spirits and can contact dead people "
                                             "(not only spirits, but also the ones in Heaven). Missouri Mosley was "
                                             "a friend of John Winchester. Pamela Barnes was a friend Sam, Dean and "
                                             "Bobby. One of the psychics is Oliver Pryce. Man of Letters were teaching "
                                             "him how to control his powers. Missouri is killed by Wraith in S13E03.",
                      episodes={"S01": [9], "S04": [1, 7, 15], "S05": [16], "S07": [8] , "S10": [17], "S12": [4],
                                "S13": [3, 9, 10], "S14": [15]})
    psychic.clues = [MonstersClues.psychic_abilities, MonstersClues.people_acting_weirdly, MonstersClues.telekinesis,
                     MonstersClues.people_dead_weirdly, MonstersClues.can_read_peoples_minds, MonstersClues.no_sulfur,
                     MonstersClues.people_speaking_languages, MonstersClues.headaches, MonstersClues.no_black_fog,
                     MonstersClues.head_filled_with_goopy_mush, MonstersClues.marks_on_victims_bodies,
                     MonstersClues.lack_of_body_control, MonstersClues.weird_noises, MonstersClues.mind_control,
                     MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
    psychic.kill_methods = [MonstersKillMethods.like_any_human]

    poltergeist = Monster("Poltergeist", episodes={"S01": [9]})
    poltergeist.clues = [MonstersClues.weird_noises, MonstersClues.flashing_lights, MonstersClues.telekinesis,
                         MonstersClues.weird_things_behavior]
    poltergeist.kill_methods = [MonstersKillMethods.angelica_root_mixture]

    norwegian_god_vanir = Monster("Norwegian god - Vanir",
                                  description="Norwegian God of the harvest, protection and prosperity. Once a year it "
                                              "requires a sacrifice of a man and a woman in order to maintain "
                                              "prosperity. Sacrifice takes place in April. Killed in S01E11.",
                                  episodes={"S01": [11]})
    norwegian_god_vanir.clues = [MonstersClues.missing_or_dead_people_regularly_in_the_same_area, MonstersClues.emf,
                                 MonstersClues.seen_as_a_scarecrow, MonstersClues.weird_noises]
    norwegian_god_vanir.disable_methods = [MonstersDisableMethods.bring_it_what_it_wants]
    norwegian_god_vanir.kill_methods = [MonstersKillMethods.burn_the_sacred_tree]

    rawhead = Monster("Rawhead", episodes={"S01": [12]})
    rawhead.kill_methods = [MonstersKillMethods.apply_large_voltage]

    reaper = Monster("Reaper", description="Can give and take life. Can also transfer illnesses of people. When gone, "
                                           "people are not dying. Rogue reape`rs (Ajay for example) can smuggle "
                                           "a person across Hell's border, Heaven and the Veil. They have secret ways "
                                           "in and out.When a reaper dies, there are electrical storms. One of the "
                                           "Reapers is Tesa (killed by Dean in S09E22). Reaper Billie is killed by "
                                           "Castiel in S12E09. That meant, that Billie got promoted to be the next "
                                           "Death (revealed in S13E05).",
                     episodes={"S01": [12], "S02": [1], "S04": [15], "S05": [10, 21], "S06": [11], "S07": [10],
                               "S08": [19], "S09": [3, 22], "S11": [2, 10, 17, 23], "S12": [6, 9], "S13": [5, 19],
                               "S14": [10, 20], "S15": [9, 12, 13, 16, 17, 18]})
    reaper.clues = [MonstersClues.people_dead_weirdly, MonstersClues.people_cured_miraculously,
                    MonstersClues.weird_things_behavior, MonstersClues.people_seeing_things_or_figures,
                    MonstersClues.seen_as_a_person_in_a_suit, MonstersClues.ghost_like_creature,
                    MonstersClues.visible_by_other_ghosts_and_people_close_to_death_only, MonstersClues.can_vanish,
                    MonstersClues.can_make_themselves_appear_as_they_like, MonstersClues.people_not_dying,
                    MonstersClues.strange_different_things_happening, MonstersClues.invisible_entity,
                    MonstersClues.electrical_storms, MonstersClues.can_appear_out_of_thin_air,
                    MonstersClues.bright_light, MonstersClues.can_collect_souls_of_the_dead, MonstersClues.telekinesis,
                    MonstersClues.can_teleport_nephilim]
    reaper.disable_methods = [MonstersDisableMethods.reaper_imprison_sigil, MonstersDisableMethods.angel_blade,
                              MonstersDisableMethods.scythe_of_death]
    reaper.kill_methods = [MonstersKillMethods.reaper_blade_combined_with_a_spell, MonstersKillMethods.angel_blade,
                           MonstersKillMethods.first_blade, MonstersKillMethods.rowenas_spell,
                           MonstersKillMethods.scythe_of_death]

    people_with_abilities = Monster("People with abilities", description="People, that were infants, when prince of "
                                                                         "Hell killed their mother on the ceiling. "
                                                                         "Can get stronger, when consuming demon "
                                                                         "blood. After using the blood for a long "
                                                                         "time, a person becomes addicted to it like "
                                                                         "to a drug. With enough power, that person's "
                                                                         "eyes become black as for a demon.",
                                    episodes={"S01": [14], "S02": [5, 10, 21, 22], "S03": [16],
                                              "S04": [1, 4, 7, 9, 15, 16, 18, 20, 21, 22], "S05": [14, 22]})
    people_with_abilities.clues = [MonstersClues.people_dead_weirdly, MonstersClues.weird_things_behavior,
                                   MonstersClues.telekinesis, MonstersClues.mind_control, MonstersClues.can_see_future,
                                   MonstersClues.able_to_electrocute, MonstersClues.people_seeing_things_or_figures,
                                   MonstersClues.their_mother_was_burned_on_the_ceiling_when_they_were_infants,
                                   MonstersClues.as_babies_fed_with_demon_blood, MonstersClues.can_control_demons,
                                   MonstersClues.immune_to_liliths_yellow_blast, MonstersClues.black_eyes,
                                   MonstersClues.can_send_demons_back_to_hell_with_power_of_will,
                                   MonstersClues.can_kill_demons_with_power_of_will]
    people_with_abilities.kill_methods = [MonstersKillMethods.like_any_human]

    crazy_humans = Monster("Crazy humans", description="Ordinary humans, that are mad or crazy. "
                                                       "Sometimes can be mistaken for ghosts or vampires. Thinman is "
                                                       "an example of two people working together to bring to life "
                                                       "a Thinman monster. In S13E11 there was a group of people, that "
                                                       "kidnapped people to sell their parts to monsters.",
                           episodes={"S01": [15], "S04": [11], "S09": [15, 20], "S13": [11], "S15": [15]})
    crazy_humans.clues = [MonstersClues.people_kidnapped_weirdly, MonstersClues.weird_electronics_behavior,
                          MonstersClues.flashing_lights, MonstersClues.people_seeing_things_or_figures,
                          MonstersClues.people_dead_weirdly, MonstersClues.weird_things_behavior, MonstersClues.claws,
                          MonstersClues.body_torn_apart, MonstersClues.weird_noises, MonstersClues.no_cold_spots,
                          MonstersClues.can_appear_out_of_thin_air, MonstersClues.slender_like_creature,
                          MonstersClues.can_vanish, MonstersClues.no_flashing_lights, MonstersClues.ghost_like_creature,
                          MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                          MonstersClues.missing_or_dead_people_regularly_in_different_areas, MonstersClues.no_sulfur,
                          MonstersClues.victims_hear_voices, MonstersClues.no_hex_bags]
    crazy_humans.kill_methods = [MonstersKillMethods.like_any_human]

    spring_heeled_jacks = Monster("Sprint Heeled Jacks", description="Not seen. Only mentioned in S01E15")
    spring_heeled_jacks.clues = [MonstersClues.people_kidnapped_weirdly]

    phantom_gassers = Monster("Phantom gassers", description="Not seen. Only mentioned in S01E15")
    phantom_gassers.clues = [MonstersClues.people_kidnapped_weirdly]

    daeva = Monster("Daeva", description="Zoroastrian demon - demon of darkness", episodes={"S01": [16]})
    daeva.clues = [MonstersClues.victims_hear_voices, MonstersClues.seen_as_a_shadow, MonstersClues.animal_like_attack,
                   MonstersClues.emf, MonstersClues.missing_heart, MonstersClues.body_torn_apart, MonstersClues.claws,
                   MonstersClues.left_zoroastrian_symbol_made_with_blood, MonstersClues.high_strength,
                   MonstersClues.invisible_entity]
    daeva.kill_methods = [MonstersKillMethods.very_bright_light]
    daeva.disable_methods = [MonstersDisableMethods.very_bright_light]

    tulpa = Monster("Tulpa", description="A Tibetan thought-form. To summon one there needs to be a tibetan spirit "
                                         "sigil drawn, but they draw a lot of psychic energy.", episodes={"S01": [17]})
    tulpa.clues = [MonstersClues.ghost_like_creature, MonstersClues.high_strength,
                   MonstersClues.keeps_changing_appearances, MonstersClues.salt_does_not_affect_it]
    tulpa.kill_methods = [MonstersKillMethods.make_a_story_that_it_will_unite_with_and_weaken]
    tulpa.disable_methods = [MonstersDisableMethods.destroy_the_place_that_the_tulpa_resides]

    shtriga = Monster("Shtriga", description="Witch-like entity from Albanian folklore. Feeds on life energy, "
                                             "but particularly on children (also siblings)", episodes={"S01": [18]})
    shtriga.clues = [MonstersClues.people_or_children_severely_sick, MonstersClues.no_emf, MonstersClues.moves_fast,
                     MonstersClues.nothing_on_ultraviolet, MonstersClues.leaves_burned_marks,
                     MonstersClues.feeding_on_life_essence, MonstersClues.seen_as_human_when_not_feeding,
                     MonstersClues.dead_people_or_children_regularly_in_different_places, MonstersClues.high_strength,
                     MonstersClues.weird_electronics_behavior]
    shtriga.kill_methods = [MonstersKillMethods.consecrated_wrought_iron_when_it_eats]

    death_omen = Monster("Death omen", description="A spirit or a vision, that appears, when somebody will die soon.",
                         episodes={"S01": [19], "S02": [7], "S03": [6], "S04": [15], "S05": [9], "S07": [7, 19],
                                   "S12": [3]})
    death_omen.clues = [MonstersClues.invisible_entity, MonstersClues.people_dead_weirdly,
                        MonstersClues.people_seeing_things_or_figures, MonstersClues.flashing_lights,
                        MonstersClues.weird_electronics_behavior]
    death_omen.disable_methods = [MonstersDisableMethods.bring_the_spirit_what_it_wants]

    vampire = Monster("Vampire", description="They were once people. They need fresh human blood to survive. "
                                             "A coss will not repel them, sunlight will not kill them. Neither will a "
                                             "stake to the heart. Vampires nest in groups 8 to 10. Smaller packs are "
                                             "sent out to hunt for food. Kidnapped people are taken to nests and then "
                                             "bleeding them for days or weeks. Sometimes nests keep humans alive for "
                                             "years as blood slaves. One can become a vampire, when drinking vampire "
                                             "blood. Upon changing, all senses sharpen.",
                      episodes={"S01": [20], "S02": [3], "S03": [7], "S05": [3], "S06": [5, 7, 10, 19, 20], "S07": [22],
                                "S08": [1, 2, 5, 7, 9, 10, 18, 19], "S09": [2, 16, 19, 20], "S10": [8, 19, 23],
                                "S11": [12], "S12": [1, 9, 14], "S13": [11, 21], "S14": [1, 2, 3, 9, 10],
                                "S15": [4, 10, 14, 20]})
    vampire.clues = [MonstersClues.ripped_throat, MonstersClues.no_blood_in_the_body, MonstersClues.needle_like_teeth,
                     MonstersClues.moving_in_groups_usually, MonstersClues.invulnerable, MonstersClues.high_strength,
                     MonstersClues.bright_eyes, MonstersClues.great_sense_of_smell, MonstersClues.white_skin,
                     MonstersClues.cattle_deaths, MonstersClues.feeds_on_blood, MonstersClues.people_dead_weirdly,
                     MonstersClues.bite_marks_on_peoples_necks, MonstersClues.no_sulfur, MonstersClues.no_emf,
                     MonstersClues.missing_or_dead_people_regularly_in_the_same_area, MonstersClues.moves_fast,
                     MonstersClues.weird_noises, MonstersClues.only_bones_left, MonstersClues.animal_like_attack,
                     MonstersClues.no_weird_noises, MonstersClues.no_hex_bags, MonstersClues.craving_for_blood]
    vampire.kill_methods = [MonstersKillMethods.decapitation, MonstersKillMethods.angel_blade, MonstersKillMethods.avd,
                            MonstersKillMethods.colt_of_colt_with_magic_bullets, MonstersKillMethods.will_of_an_angel,
                            MonstersKillMethods.roman_corn_syrup, MonstersKillMethods.will_of_a_nephilim,
                            MonstersKillMethods.will_of_an_archangel, MonstersKillMethods.bad_place_spear]
    vampire.disable_methods = [MonstersDisableMethods.dead_mans_blood]
    vampire.cure_methods = [MonstersCureMethods.cocktail_made_of_blood_of_the_vampire_that_bit_the_victim]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 2 ----------------------------------------------------

    rakshasa = Monster("Rakshasa", description="Race of ancient Hindu creatures. They appear in human form and feed on "
                                               "human flesh. Can make themselves invisible and cannot enter a home "
                                               "without being invited. They live in squalor and sleep on a bed of "
                                               "dead insects.", episodes={"S02": [2]})
    rakshasa.clues = [MonstersClues.seen_as_a_clown, MonstersClues.people_dead_weirdly, MonstersClues.invulnerable,
                      MonstersClues.people_seeing_things_or_figures, MonstersClues.can_become_invisible,
                      MonstersClues.dead_people_or_children_regularly_in_different_places,
                      MonstersClues.cannot_enter_a_home_without_invitation]
    rakshasa.kill_methods = [MonstersKillMethods.dagger_made_of_pure_brass]

    resurrected_person = Monster("Resurrected person",
                                 description="Brought back from the dead by ancient Greek necromancy ritual. Has to "
                                             "eat people to stay 'alive'", episodes={"S02": [4], "S14": [6]})
    resurrected_person.clues = [MonstersClues.invulnerable, MonstersClues.missing_body, MonstersClues.ripped_throat,
                                MonstersClues.weird_plant_deaths_or_behavior, MonstersClues.people_dead_weirdly,
                                MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
    resurrected_person.disable_methods = [MonstersDisableMethods.silver_or_silver_bullets]
    resurrected_person.kill_methods = [MonstersKillMethods.nail_it_back_to_the_grave]

    hell_hound = Monster("Hell Hound", description="Creation of God, but they were too vicious, so God kept them "
                                                   "short. Now they hunt people that sold their souls. According the "
                                                   "the Demon Tablet - dire creatures may be seen only by the damned "
                                                   "or through an object scorched with holy fire (burning holy oil). "
                                                   "Almost all Hell Hounds were killed by Angels, but Lucyfer rescued "
                                                   "pregnant Ramsey, that is loyal only to him. Hell Hound can be "
                                                   "controlled by a special whistle (showed in S12E21).",
                         episodes={"S02": [8], "S03": [16], "S05": [10, 20], "S06": [4, 10, 14], "S08": [14],
                                   "S09": [21], "S11": [15], "S12": [15, 21], "S15": [13]})
    hell_hound.clues = [MonstersClues.victims_hear_dogs_barking_and_growling, MonstersClues.invisible_dogs,
                        MonstersClues.victims_see_black_dogs, MonstersClues.people_seeing_strange_things,
                        MonstersClues.victims_got_better_at_something_up_to_ten_years_earlier,
                        MonstersClues.people_dead_weirdly, MonstersClues.animal_like_attack, MonstersClues.black_blood,
                        MonstersClues.animal_like_noises]
    hell_hound.disable_methods = [MonstersDisableMethods.goofer_dust, MonstersDisableMethods.devils_shoestring,
                                  MonstersDisableMethods.demon_must_call_it_off,
                                  MonstersDisableMethods.salt_or_salted_bullets]
    hell_hound.kill_methods = [MonstersKillMethods.demon_killing_knife, MonstersKillMethods.angel_sword,
                               MonstersKillMethods.colt_of_colt_with_magic_bullets, MonstersKillMethods.angel_blade]

    crossroads_demon = Monster("Crossroads demon", description="One can make a deal with that demon. Can give "
                                                               "anything, but will collect ones soul after 10 years. "
                                                               "One can summon it by placing a box with: graveyard "
                                                               "dirt, black cat cone, ones photo in the center of "
                                                               "a crossroad.",
                               episodes={"S02": [8, 22], "S03": [5, 15], "S04": [9], "S05": [10], "S06": [4],
                                         "S07": [8], "S08": [19], "S09": [2, 16], "S10": [1, 3, 10, 14], "S11": [15],
                                         "S12": [6], "S13": [8], "S15": [15]})
    crossroads_demon.clues = [MonstersClues.victims_got_better_at_something_up_to_ten_years_earlier,
                              MonstersClues.red_eyes, MonstersClues.summoned_by_placing_box_in_the_crossroads,
                              MonstersClues.travels_as_black_fog, MonstersClues.pact_sealed_with_a_kiss,
                              MonstersClues.people_dead_weirdly, MonstersClues.telekinesis, MonstersClues.high_strength,
                              MonstersClues.flashing_lights]
    crossroads_demon.disable_methods = [MonstersDisableMethods.devils_trap, MonstersDisableMethods.holy_water,
                                        MonstersDisableMethods.fry_its_remains]
    crossroads_demon.kill_methods = [MonstersKillMethods.colt_of_colt_with_magic_bullets,
                                     MonstersKillMethods.demon_killing_knife, MonstersKillMethods.burn_the_remains,
                                     MonstersKillMethods.angel_blade]

    demonic_virus = Monster("Demonic virus", description="Probably caused Roanoke colony disappearance. Croatoan might "
                                                         "be a name of the demon. Names also include Dever and "
                                                         "Reshef - demon of plague and pestilence.",
                            episodes={"S02": [9]})
    demonic_virus.clues = [MonstersClues.people_acting_weirdly, MonstersClues.sulfur_in_the_blood,
                           MonstersClues.elevated_lymphocyte_percentage, MonstersClues.high_strength,
                           MonstersClues.infected_with_blood_to_blood_contact]
    demonic_virus.kill_methods = [MonstersKillMethods.like_any_human]
    demonic_virus.disable_methods = [MonstersDisableMethods.wait_until_its_over]

    angel_like_spirit = Monster("Angel-like spirit", description="Spirit of a person that died tragically (like "
                                                                 "vengeful spirit), but instead of evil, "
                                                                 "that spirit becomes better-ish.",
                                episodes={"S02": [13]})
    angel_like_spirit.clues = [MonstersClues.people_seeing_things_or_figures, MonstersClues.weird_electronics_behavior,
                               MonstersClues.flashing_lights, MonstersClues.people_hear_voices, MonstersClues.no_emf,
                               MonstersClues.weird_things_behavior, MonstersClues.small_earth_quake,
                               MonstersClues.people_seeing_figure_of_light, MonstersClues.people_feel_spiritual_ecstasy,
                               MonstersClues.knows_past, MonstersClues.can_read_peoples_minds, MonstersClues.no_sulfur]
    angel_like_spirit.disable_methods = [MonstersDisableMethods.give_it_last_rites]

    trickster = Monster("Trickster (Loki, Anansi)", description="Demigod (Loki in Scandinavia, Anansi in West Africa). "
                                                                "Can create chaos and mischief as easy as breathing. "
                                                                "Not seen, only appeared to be one, but it was "
                                                                "Archangel Gabriel. A few thousand epochs ago, Gabriel "
                                                                "was out for a hike in the Fjords, came across Loki "
                                                                "bound in a cave with snake dripping venom into his "
                                                                "eye. He freed him. Killed by Gabriel in S13E20.",
                        episodes={"S13": [20]})
    trickster.clues = [MonstersClues.people_seeing_things_or_figures, MonstersClues.can_create_things_out_of_thin_air,
                       MonstersClues.people_dead_weirdly, MonstersClues.no_emf, MonstersClues.people_seeing_aliens,
                       MonstersClues.strange_different_things_happening, MonstersClues.things_disappearing,
                       MonstersClues.weird_noises, MonstersClues.immortal, MonstersClues.people_seeing_strange_things,
                       MonstersClues.can_make_themselves_appear_as_they_like, MonstersClues.mimics_human_voice,
                       MonstersClues.loves_sugar, MonstersClues.telekinesis, MonstersClues.sweets_wrappers,
                       MonstersClues.can_vanish, MonstersClues.high_strength, MonstersClues.astral_projection]
    trickster.kill_methods = [MonstersKillMethods.gabriel_sword]

    archangel_gabriel = Monster("Archangel - Gabriel", description="Archangel, that enjoys tricking people and killing "
                                                                   "them afterwards. Supposedly killed by Lucyfer in "
                                                                   "S05E19. Back in S13E13. Killed by Archangel "
                                                                   "Michael from Apocalypse World in S13E22.",
                                episodes={"S02": [15], "S03": [11], "S05": [8, 19], "S13": [13, 17, 18, 20, 21, 22]})
    archangel_gabriel.clues = [MonstersClues.people_seeing_things_or_figures, MonstersClues.people_seeing_aliens,
                               MonstersClues.telekinesis, MonstersClues.no_emf, MonstersClues.things_disappearing,
                               MonstersClues.weird_noises, MonstersClues.loves_sugar, MonstersClues.immortal,
                               MonstersClues.strange_different_things_happening, MonstersClues.can_vanish,
                               MonstersClues.can_create_things_out_of_thin_air, MonstersClues.can_reverse_time,
                               MonstersClues.people_dead_weirdly, MonstersClues.people_seeing_strange_things,
                               MonstersClues.can_put_people_into_alternate_timelines, MonstersClues.sweets_wrappers,
                               MonstersClues.mimics_human_voice, MonstersClues.high_strength, MonstersClues.has_wings,
                               MonstersClues.can_teleport_people, MonstersClues.can_make_themselves_appear_as_they_like,
                               MonstersClues.can_put_somebody_in_a_time_loop, MonstersClues.bright_light,
                               MonstersClues.bright_eyes, MonstersClues.can_kill_princes_of_hell_with_a_thought,
                               MonstersClues.astral_projection]
    archangel_gabriel.disable_methods = [MonstersDisableMethods.holy_oil]
    archangel_gabriel.kill_methods = [MonstersKillMethods.archangel_blade]

    phantom_hitchhiker = Monster("Phantom hitchhiker", description="Not seen. Only mentioned in S01E16")
    phantom_hitchhiker.clues = [MonstersClues.missing_or_dead_people_regularly_in_the_same_area]

    werewolf = Monster("Werewolf", description="Human by day, animal killing machine by moonlight. Curse spreads "
                                               "through bites. Killing a werewolf, that bit a person does not revert "
                                               "the curse. Werewolves that are turned up to 4 generations from pure "
                                               "blood are less feral and can transform before, during and after the "
                                               "lunar cycle. Pure bloods don't blackout during the transformation and "
                                               "can control themselves. Some have been able to subsist off of "
                                               "animal hearts. Also mentioned in S01E16. Werewolfs can be enhanced by "
                                               "Archangel blood (from S14E02) to be immune to silver. Only "
                                               "decapitation is effective on them then.",
                       episodes={"S02": [17], "S08": [4], "S09": [12, 20], "S10": [4], "S11": [17], "S12": [6, 16],
                                 "S13": [10, 11, 23], "S14": [2, 9, 10], "S15": [5, 8, 10]})
    werewolf.clues = [MonstersClues.body_torn_apart, MonstersClues.animal_like_attack, MonstersClues.missing_heart,
                      MonstersClues.murders_during_full_moon_week, MonstersClues.claws, MonstersClues.attacks_at_night,
                      MonstersClues.animal_like_noises, MonstersClues.amnesia_blackout, MonstersClues.high_strength,
                      MonstersClues.people_dead_weirdly, MonstersClues.increased_regeneration, MonstersClues.moves_fast,
                      MonstersClues.bite_marks, MonstersClues.missing_organs, MonstersClues.animals_dead_weirdly,
                      MonstersClues.missing_or_dead_people_regularly_in_the_same_area, MonstersClues.needle_like_teeth,
                      MonstersClues.yellow_eyes, MonstersClues.large_mouth_full_of_teeth, MonstersClues.ripped_throat]
    werewolf.kill_methods = [MonstersKillMethods.silver_bullet_into_the_heart, MonstersKillMethods.silver_blade,
                             MonstersKillMethods.silver_nitrate_injection, MonstersKillMethods.angel_blade,
                             MonstersKillMethods.decapitation, MonstersKillMethods.will_of_a_nephilim]
    werewolf.disable_methods = [MonstersDisableMethods.silver_or_silver_bullets]
    werewolf.cure_methods = [MonstersCureMethods.plasma_therapy_with_the_blood_of_the_werewolf_that_bit_the_victim]

    jinn = Monster("Jinn", description="Mythical creatures, that feed on people. They have godlike power and can "
                                       "shape reality as they like. Usually reside in ruins - the bigger, the better. "
                                       "They poison people, who see nightmares or paradise of theirs. The poison is "
                                       "transferred by touch. It can be cured. Not all Jinn look different than "
                                       "humans, some look just like regular people. There is an offshoot of jinn, "
                                       "that liquefies the organs of the victims. It can be killed like a regular "
                                       "jinn. A jinn can be upgraded with Archangel Blood. After the upgrade, it reads "
                                       "minds, sees nightmares after just one touch and can bring those nightmares "
                                       "into the world, that turn to dust, when killed. After the upgrade bullets are "
                                       "less affective.",
                   episodes={"S02": [20], "S06": [1, 10], "S08": [20], "S09": [20], "S14": [5, 10], "S15": [6, 10]})
    jinn.clues = [MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                  MonstersClues.blue_eyes, MonstersClues.can_put_a_person_in_wonderland, MonstersClues.feeds_on_blood,
                  MonstersClues.blue_fire_on_its_arms, MonstersClues.poisoned_people, MonstersClues.people_dead_weirdly,
                  MonstersClues.seen_as_human_when_not_feeding, MonstersClues.people_seeing_strange_things,
                  MonstersClues.liquefied_organs, MonstersClues.no_black_goo, MonstersClues.can_appear_out_of_thin_air,
                  MonstersClues.leaves_blue_handprint, MonstersClues.no_burn_marks, MonstersClues.deep_voice,
                  MonstersClues.being_at_two_places_at_once, MonstersClues.people_seeing_things_or_figures,
                  MonstersClues.no_blood_in_the_body]
    jinn.disable_methods = [MonstersDisableMethods.gun_shot]
    jinn.kill_methods = [MonstersKillMethods.silver_knife_dipped_in_lambs_blood, MonstersKillMethods.will_of_a_nephilim,
                         MonstersKillMethods.angel_blade]

    acheri = Monster("Acheri", description="Demon, that disguises itself as a little girl.", episodes={"S02": [21]})
    acheri.clues = [MonstersClues.seen_as_a_little_girl, MonstersClues.claws, MonstersClues.animal_like_attack]
    acheri.disable_methods = [MonstersDisableMethods.iron_or_iron_bullets]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 3 ----------------------------------------------------

    seven_deadly_sins = Monster("Seven deadly sins", description="In 1589 Binsfeld's classification of demons, he IDd "
                                                                 "all of them not just as human vices but "
                                                                 "as actual devils.", episodes={"S03": [1]})
    seven_deadly_sins.clues = [MonstersClues.black_eyes, MonstersClues.mind_control, MonstersClues.no_emf,
                               MonstersClues.burned_by_holy_water, MonstersClues.travels_as_black_fog,
                               MonstersClues.people_acting_weirdly, MonstersClues.people_dead_weirdly,
                               MonstersClues.weird_electronics_behavior, MonstersClues.can_read_peoples_minds,
                               MonstersClues.no_sulfur, MonstersClues.high_strength]
    seven_deadly_sins.kill_methods = [MonstersKillMethods.demon_killing_knife]
    seven_deadly_sins.disable_methods = [MonstersDisableMethods.holy_water, MonstersDisableMethods.devils_trap,
                                         MonstersDisableMethods.exorcism]

    changeling = Monster("Changeling", description="Evil monster babies/children. They can perfectly mimic children. "
                                                   "According to lore, they climb the window and kidnap the kid. "
                                                   "Feeding on moms' synovial fluid. They can feed on a victim for "
                                                   "months. Kidnapped kids are hidden usually underground. There can "
                                                   "be a mother changeling. Burning her burns also kid changelings.",
                         episodes={"S03": [2]})
    changeling.clues = [MonstersClues.weird_things_behavior, MonstersClues.babies_or_children_acting_weirdly,
                        MonstersClues.missing_or_dead_people_regularly_in_the_same_area, MonstersClues.feeding_at_night,
                        MonstersClues.bite_marks_on_peoples_necks, MonstersClues.people_dead_weirdly,
                        MonstersClues.may_leave_claw_marks,
                        MonstersClues.real_appearance_can_be_seen_in_a_reflection_or_camera]
    changeling.kill_methods = [MonstersKillMethods.burn_it]

    krampus = Monster("Krampus", description="Evil brother of Santa. Comes in many names - Belsnickel, Black Peter. "
                                             "Lore says, that Santa's brother went rogue and now he punishes the "
                                             "wicked around Christmas time. Not seen, only mentioned in S03E08")
    krampus.clues = [MonstersClues.weird_noises, MonstersClues.people_dead_weirdly,
                     MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                     MonstersClues.missing_or_dead_people_around_christmas, MonstersClues.seen_as_a_santa_like_figure]

    holdenacar = Monster("Holdenacar", description="God of the winter solstice. Attracted to meadowsweet, which is one "
                                                   "of the most powerful plants in pagan lore. Killed in S03E08.",
                         episodes={"S03": [8]})
    holdenacar.clues = [MonstersClues.missing_or_dead_people_regularly_in_different_areas, MonstersClues.weird_noises,
                        MonstersClues.people_dead_weirdly, MonstersClues.missing_or_dead_people_around_christmas,
                        MonstersClues.high_strength, MonstersClues.seen_as_a_santa_like_figure,
                        MonstersClues.victims_have_meadowsweet_somewhere, MonstersClues.weird_weather]
    holdenacar.kill_methods = [MonstersKillMethods.evergreen_pin]

    witch = Monster("Witch", description="A woman/man, that deals with different kinds of magic (like black, "
                                         "old world, etc.). Witch has magic powers, can bring demons, be immortal, "
                                         "teleport etc. Some witches have companions (called familiars) in the form of "
                                         "a pet. Witches can perform astral projections. One of the more powerful "
                                         "witches is Rowena introduced in S10E03. According to her, grand coven there "
                                         "are three recognized kinds of witch in the world. Most common are the "
                                         "borrowers - those who harness the power of a demon in order to practice the "
                                         "art. Second one (and rarest) are the naturals - the ones born with a gift. "
                                         "The last group are the students - those with no natural ability who, with "
                                         "enough practice and training and a grand coven-approved mentor to show them "
                                         "the path, can eke out a modicum of witchly power. Rowena is a natural and is "
                                         "also a mother of Crowley. Rowena was supposedly killed by Lucifer in S11E10. "
                                         "Back in S11E18. It is revealed, that she was prepared for her death - when a "
                                         "spell sensed her death, it revived her. Rowena was killed in S12E23 by "
                                         "Lucyfer. Back in S13E12. Sam kills Rowena in order to close the rip, that "
                                         "GOD opened.",
                    episodes={"S03": [9], "S04": [7, 12], "S05": [7, 12], "S07": [5], "S08": [7, 15],
                              "S10": [3, 7, 9, 10, 14, 16, 17, 18, 19, 21, 22, 23], "S11": [3, 9, 10, 13, 18, 22, 23],
                              "S12": [2, 3, 6, 8, 11, 13, 20], "S13": [7, 12, 19, 21, 22], "S14": [3, 6, 7, 14, 18],
                              "S15": [2, 3, 6, 8]})
    witch.clues = [MonstersClues.people_dead_weirdly, MonstersClues.hex_bag_hidden_somewhere, MonstersClues.immortal,
                   MonstersClues.coin_hidden_somewhere, MonstersClues.weird_electronics_behavior,
                   MonstersClues.telekinesis, MonstersClues.can_vanish, MonstersClues.weird_plant_deaths_or_behavior,
                   MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                   MonstersClues.people_aging_rapidly, MonstersClues.people_getting_younger, MonstersClues.invulnerable,
                   MonstersClues.people_with_souls_switched, MonstersClues.black_goo, MonstersClues.flashing_lights,
                   MonstersClues.card_found_on_a_victim, MonstersClues.missing_heart, MonstersClues.high_strength,
                   MonstersClues.people_acting_weirdly, MonstersClues.boiled_brain, MonstersClues.red_faces_of_victims,
                   MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_different_areas,
                   MonstersClues.strange_different_things_happening, MonstersClues.can_read_peoples_minds,
                   MonstersClues.weird_fire_spontaneous_combustion, MonstersClues.purple_eyes,
                   MonstersClues.killed_reapers]
    witch.disable_methods = [MonstersDisableMethods.stop_it_from_speaking, MonstersDisableMethods.iron_chains,
                             MonstersDisableMethods.witch_catcher]
    witch.kill_methods = [MonstersKillMethods.like_any_human, MonstersKillMethods.death_transfer_spell,
                          MonstersKillMethods.witch_killing_brew, MonstersKillMethods.will_of_an_archangel,
                          MonstersKillMethods.witch_killing_bullets, MonstersKillMethods.break_the_neck]

    demon_astaroth = Monster("Demon Astaroth", description="Collects human souls by changing them into witches. "
                                                           "Killed in S03R09.", episodes={"S03": [9]})
    demon_astaroth.clues = [MonstersClues.black_eyes, MonstersClues.telekinesis, MonstersClues.high_strength,
                            MonstersClues.can_stop_bullets]
    demon_astaroth.kill_methods = [MonstersKillMethods.demon_killing_knife]

    first_demon = Monster("First Demon - Lilith", description="First demon created by Lucifer out of a human soul by "
                                                              "twisting it. Killed in S04E22 by Sam with powers. "
                                                              "Brought back by GOD in S15E05, when Sam and Dean face "
                                                              "her. Snapped by Archangel Michael in S15E08.",
                          episodes={"S03": [12, 16], "S04": [18, 22], "S15": [5, 8]})
    first_demon.clues = [MonstersClues.white_eyes, MonstersClues.yellow_blast, MonstersClues.telekinesis,
                         MonstersClues.unable_to_hurt_people_with_abilities_with_its_yellow_blast,
                         MonstersClues.travels_as_black_fog, MonstersClues.can_hurt_people_with_a_thought,
                         MonstersClues.can_appear_out_of_thin_air, MonstersClues.can_vanish]
    first_demon.kill_methods = [MonstersKillMethods.will_of_a_person_with_abilities,
                                MonstersKillMethods.will_of_an_archangel]

    death_echo = Monster("Death echo", description="Echos are trapped in a loop. They keep replaying how they "
                                                   "died over and over again usually at the place of death.",
                         episodes={"S03": [13]})
    death_echo.clues = [MonstersClues.ghost_like_creature, MonstersClues.can_vanish, MonstersClues.emf,
                        MonstersClues.weird_electronics_behavior]
    death_echo.disable_methods = [MonstersDisableMethods.shock_it_out_of_its_loop]

    crocotta = Monster("Crocotta", description="Soul scavenger. Mimics loved ones. Whispers 'Come to me', then lures "
                                               "victims into the dark and swallows their souls. Usually live in filth.",
                       episodes={"S03": [14]})
    crocotta.clues = [MonstersClues.people_dead_weirdly, MonstersClues.weird_electronics_behavior,
                      MonstersClues.contact_from_dead_people, MonstersClues.victims_hear_voices,
                      MonstersClues.needle_like_teeth, MonstersClues.can_control_electronics]
    crocotta.kill_methods = [MonstersKillMethods.sharp_object_into_the_spine]

    eternal_living_person = Monster("Eternal living person", description="Person, that can live forever in theory by "
                                                                         "replacing faulty organs.",
                                    episodes={"S03": [15]})
    eternal_living_person.clues = [MonstersClues.missing_organs, MonstersClues.people_dead_weirdly,
                                   MonstersClues.invulnerable]
    eternal_living_person.disable_methods = [MonstersDisableMethods.chloroform, MonstersDisableMethods.bury_it_alive]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 4 ----------------------------------------------------

    angel = Monster("Angel", description="Angel of God (Castiel, Uriel, Hester, Inias, Samandriel, Ion, Nathaniel, "
                                         "Naomi). They can bring people back from the dead. Cannot track people, that "
                                         "use powerful spells to hide themselves. All angels have graces - energy "
                                         "source for their power. When some of the grace is removed (either by eating "
                                         "by another angel or by storing in a container) after some time it is "
                                         "recharged. But only to a point, the whole grace cannot regenerate. All "
                                         "angels instinctively know the names of past, present and future prophets. "
                                         "When they disobey (fall), as a punishment they can become human. When dying, "
                                         "a bright light is produced and they leave wing marks. Also the organs of the "
                                         "vessel, they are possessing are vapourised. To possess somebody, they need a "
                                         "consent. When an angel is tortured, the pain causes a ripple effect and "
                                         "strange things happen nearby. When an angel looses it's Grace - it becomes "
                                         "human. An Angel without a Grace can intake another Angel's/Fallen Angel's "
                                         "Grace. When an Angel leaves a vessel - it leaves a part of himself (a part "
                                         "of his Grace) in it - like a fingerprint. An Angel can be tracked using a "
                                         "part of the Grace, that it left in his vessel. All Angels can unify in order "
                                         "to produce a single angelic blow of power. When that happens, a fallout is "
                                         "produced and the closer you get to the ground zero, the worse it becomes. "
                                         "According to Castiel, the last time it happened, Lot's wife was turned to "
                                         "salt. The fallout does not affect Angels. An Angel can be possessed by an "
                                         "Archangel. Castiel broke the fourth wall in S06E20. Castiel supposedly died "
                                         "in S07E01, back in S07E17. Castiel is killed by Lucyfer in S12E23 with an "
                                         "Angel Blade and appears again in S13E03 in Empty. Back to Earth in S13E04. "
                                         "It is not possible for an Angel to heal an Archangel.",
                    episodes={"S04": [1, 2, 3, 7, 9, 10, 15, 16, 18, 20, 21, 22],
                              "S05": [1, 2, 3, 4, 5, 6, 8, 10, 12, 13, 14, 15, 16, 17, 18, 21, 22],
                              "S06": [3, 6, 7, 10, 12, 15, 17, 18, 19, 20, 21, 22], "S07": [1, 17, 20, 21, 23],
                              "S08": [2, 7, 8, 10, 17, 19, 21, 22, 23], "S09": [9, 10, 11, 14, 18, 21, 22, 23],
                              "S10": [1, 2, 3, 7, 9, 10, 14, 17, 18, 20, 21, 22, 23],
                              "S11": [1, 2, 3, 6, 10, 14, 18, 22, 23],
                              "S12": [1, 2, 3, 7, 8, 9, 10, 12, 13, 15, 19, 23],
                              "S13": [1, 2, 3, 4, 5, 6, 7, 9, 12, 13, 14, 16, 18, 19, 21, 22, 23],
                              "S14": [1, 2, 3, 7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19, 20],
                              "S15": [1, 2, 3, 6, 7, 8, 9, 11, 12, 13, 15, 17, 18]})
    angel.clues = [MonstersClues.can_bring_back_dead_people, MonstersClues.in_true_form_burns_eyes_of_people,
                   MonstersClues.place_where_person_was_resurrected_looks_like_after_explosion, MonstersClues.has_wings,
                   MonstersClues.leaves_burned_marks, MonstersClues.can_tell_if_somebody_was_recently_healed,
                   MonstersClues.can_repair_human_body, MonstersClues.telekinesis, MonstersClues.invulnerable,
                   MonstersClues.can_put_a_person_to_sleep, MonstersClues.demon_killing_knife_is_ineffective,
                   MonstersClues.true_voice_can_hurt_people, MonstersClues.can_vanish, MonstersClues.high_strength,
                   MonstersClues.immune_to_salt_rounds, MonstersClues.immune_to_devils_trap, MonstersClues.bright_light,
                   MonstersClues.can_contact_a_person_in_a_dream, MonstersClues.can_send_people_to_the_past,
                   MonstersClues.can_appear_out_of_thin_air, MonstersClues.can_see_real_appearance_of_entities,
                   MonstersClues.can_exorcise_certain_demons_with_hand_on_forehead, MonstersClues.mimics_human_voice,
                   MonstersClues.can_control_electronics, MonstersClues.triangle_wound, MonstersClues.amnesia_blackout,
                   MonstersClues.can_teleport_people, MonstersClues.can_read_peoples_minds, MonstersClues.burned_eyes,
                   MonstersClues.can_become_invisible, MonstersClues.can_control_demons, MonstersClues.liquefied_organs,
                   MonstersClues.can_erase_and_bring_back_memories, MonstersClues.can_transfer_mental_diseases,
                   MonstersClues.can_go_and_put_into_a_persons_mind, MonstersClues.strange_different_things_happening,
                   MonstersClues.bright_eyes, MonstersClues.vapourised_organs, MonstersClues.travels_as_white_fog,
                   MonstersClues.blue_eyes, MonstersClues.falling_meteor, MonstersClues.weird_electronics_behavior,
                   MonstersClues.can_kill_humans_with_hand_on_forehead]
    angel.disable_methods = [MonstersDisableMethods.symbol_made_with_blood_against_angels,
                             MonstersDisableMethods.exorcism_for_angels, MonstersDisableMethods.holy_oil,
                             MonstersDisableMethods.enochian_spell, MonstersDisableMethods.rowenas_immobilization_spell,
                             MonstersDisableMethods.presence_of_the_mother, MonstersDisableMethods.grace_removal,
                             MonstersDisableMethods.attack_dog_spell, MonstersDisableMethods.angel_blade,
                             MonstersDisableMethods.angel_knuckle_duster, MonstersDisableMethods.enochian_handcuffs,
                             MonstersDisableMethods.lance_of_archangel_michael, MonstersDisableMethods.gorgon_venom]
    angel.kill_methods = [MonstersKillMethods.angel_blade, MonstersKillMethods.holy_oil,
                          MonstersKillMethods.leviathan_black_goo, MonstersKillMethods.will_of_an_archangel,
                          MonstersKillMethods.will_of_the_darkness, MonstersKillMethods.lance_of_archangel_michael,
                          MonstersKillMethods.will_of_prince_of_hell, MonstersKillMethods.will_of_a_nephilim]

    rougarou = Monster("Rougarou", description="Once a human. Now - rotten teeth, wormy skin. When going through "
                                               "metamorphosis, their hunger increases. At first for everything, but "
                                               "after a while - for human flesh. Hunger grows, until it is "
                                               "irresistible. After the first bite of the human flesh, they transform "
                                               "completely and fast. They feed once, they're a monster forever. "
                                               "This may be a genetic condition.",
                       episodes={"S04": [4], "S06": [10], "S08": [2], "S12": [13], "S13": [11], "S14": [10]})
    rougarou.clues = [MonstersClues.enormous_appetite, MonstersClues.body_metamorphosis, MonstersClues.high_strength,
                      MonstersClues.bloodshot_eyes, MonstersClues.wormy_skin, MonstersClues.no_bone_marrow_in_bones,
                      MonstersClues.drained_organs, MonstersClues.people_dead_weirdly, MonstersClues.bite_marks]
    rougarou.kill_methods = [MonstersKillMethods.burn_it, MonstersKillMethods.demon_killing_knife,
                             MonstersKillMethods.man_of_letters_rougarou_gun, MonstersKillMethods.will_of_a_nephilim]

    samhain = Monster("Samhain", description="A demon that is the origin of Halloween. Celts believed, that the 31st "
                                             "of October is the day, when the veil is the thinnest between the living "
                                             "and dead. And this is also Samhain's night. Masks were put on to hide "
                                             "from him, sweets left on doorsteps to appease him and faces carved into "
                                             "pumpkins to worship him.", episodes={"S04": [7]})
    samhain.clues = [MonstersClues.travels_as_black_fog, MonstersClues.white_eyes, MonstersClues.yellow_blast,
                     MonstersClues.can_bring_back_dead_people, MonstersClues.can_summon_ghosts]
    samhain.disable_methods = [MonstersDisableMethods.extrusion_by_people_with_abilities]

    fallen_angel = Monster("Fallen Angel", description="An angel, that disobeyed the orders or was cursed by "
                                                       "spell banishing Angels to Earth and fell. Like Angels - when "
                                                       "killed, the organs of the vessel are vapourised. "
                                                       "After The Fall in S08E23 we have the following fallen "
                                                       "angels: Hael, Ezekiel, Bartholomew, Malachi, Gadreel "
                                                       "(committed suicide in S0923), Muriel, Azrael, Sophia, Theo, "
                                                       "Thaddeus, Abner, Hannah, Ezra, Esther, Asariel, Purah. Gadreel "
                                                       "was the Angel, that let Lucifer into the Garden of Eden.",
                           episodes={"S04": [9, 10], "S08": [23], "S09": [1, 2, 3, 4, 5, 8, 9, 10, 14, 18, 21, 22, 23],
                                     "S10": [1, 2, 3, 7, 10, 17], "S11": [1, 2, 3, 9, 10, 11, 12, 22]})
    fallen_angel.clues = [MonstersClues.people_hear_voices, MonstersClues.can_see_real_appearance_of_entities,
                          MonstersClues.telekinesis, MonstersClues.people_acting_weirdly, MonstersClues.falling_meteor,
                          MonstersClues.can_hear_angel_radio, MonstersClues.can_erase_and_bring_back_memories,
                          MonstersClues.can_repair_human_body, MonstersClues.can_posses_a_person,
                          MonstersClues.bright_eyes, MonstersClues.can_hear_demon_radio, MonstersClues.bright_light,
                          MonstersClues.burned_eyes, MonstersClues.travels_as_white_fog, MonstersClues.body_torn_apart,
                          MonstersClues.vapourised_organs, MonstersClues.can_bring_back_dead_people,
                          MonstersClues.blue_eyes, MonstersClues.leaves_burned_marks, MonstersClues.triangle_wound,
                          MonstersClues.people_acting_weirdly, MonstersClues.travels_as_white_fog,
                          MonstersClues.can_kill_humans_with_hand_on_forehead, MonstersClues.weird_things_behavior,
                          MonstersClues.can_put_a_person_to_sleep, MonstersClues.weird_electronics_behavior,
                          MonstersClues.flashing_lights, MonstersClues.burned_eyes, MonstersClues.people_dead_weirdly]
    fallen_angel.disable_methods = [MonstersDisableMethods.holy_oil, MonstersDisableMethods.angel_blade,
                                    MonstersDisableMethods.first_blade]
    fallen_angel.kill_methods = [MonstersKillMethods.angel_blade, MonstersKillMethods.first_blade,
                                 MonstersKillMethods.will_of_an_archangel]

    demon_alastair = Monster("Demon Alastair", description="A very powerful demon. Tortures souls in Hell. "
                                                           "Killed in S04E16 by Sam with powers.",
                             episodes={"S04": [9, 10, 15, 16]})
    demon_alastair.clues = [MonstersClues.white_eyes, MonstersClues.demon_killing_knife_is_ineffective,
                            MonstersClues.immune_to_extrusion_by_people_with_abilities,
                            MonstersClues.immune_to_exorcism_of_an_angel]
    demon_alastair.disable_methods = [MonstersDisableMethods.demon_killing_knife, MonstersDisableMethods.holy_water,
                                      MonstersDisableMethods.reconnection_of_angel_with_its_grace,
                                      MonstersDisableMethods.enochian_devils_trap,
                                      MonstersDisableMethods.salt_or_salted_bullets]
    demon_alastair.kill_methods = [MonstersKillMethods.will_of_a_person_with_abilities]

    siren = Monster("Siren", description="Beautiful creatures, that prey on men, entice them with their siren song. "
                                         "For men, they are perfect and they want to do anything for them. Sirens "
                                         "lived on islands in the past. Has a venom in it's mouth. Can be killed with "
                                         "it's own venom or the blood of the victim, that is under the spell.",
                    episodes={"S04": [14]})
    siren.clues = [MonstersClues.people_dead_weirdly, MonstersClues.people_acting_weirdly,
                   MonstersClues.high_oxytocin_levels, MonstersClues.can_read_peoples_minds,
                   MonstersClues.real_appearance_can_be_seen_in_a_reflection_or_camera]
    siren.kill_methods = [MonstersKillMethods.its_own_venom]

    angel_zachariah = Monster("Angel Zachariah", description="High Tier Angel. Died in S05E18. Zachariah from the "
                                                             "alternate timeline appears in S13E14 and is killed in "
                                                             "the same episode by Jack.",
                              episodes={"S04": [17, 18, 22], "S05": [1, 4, 16, 18], "S13": [14], "S14": [13]})
    angel_zachariah.clues = [MonstersClues.can_put_people_into_alternate_timelines, MonstersClues.can_repair_human_body,
                             MonstersClues.can_erase_and_bring_back_memories, MonstersClues.can_appear_out_of_thin_air,
                             MonstersClues.can_vanish, MonstersClues.can_give_people_diseases,
                             MonstersClues.telekinesis]
    angel_zachariah.disable_methods = [MonstersDisableMethods.symbol_made_with_blood_against_angels]
    angel_zachariah.kill_methods = [MonstersKillMethods.angel_blade]

    prophet = Monster("Prophet of the Lord", description="A person that is gifted with the knowledge of the future. "
                                                         "Only one prophet can exist at a time. There are multiple "
                                                         "people in the world, that can become one if needed. Prophets "
                                                         "throughout the series: Chuck Shurley, Kevin Tran (Killed by "
                                                         "Gadreel in S09E09). Chuck came back in S10E05. Next Prophet, "
                                                         "that Winchesters encounter in S11E21 is professor Donatello "
                                                         "Redfield.",
                      episodes={"S04": [18, 22], "S05": [1, 9, 22], "S07": [21, 22, 23],
                                "S08": [1, 2, 7, 10, 14, 19, 21, 23], "S09": [2, 6, 9], "S10": [5], "S11": [21, 22],
                                "S13": [2, 7, 13, 14, 20], "S14": [12, 15, 17], "S15": [8]})
    prophet.clues = [MonstersClues.can_see_future, MonstersClues.protected_by_an_archangel, MonstersClues.visions,
                     MonstersClues.can_repair_broken_word_of_god, MonstersClues.can_read_word_of_god,
                     MonstersClues.weird_weather, MonstersClues.missing_or_dead_people_regularly_in_different_areas,
                     MonstersClues.marks_on_victims_bodies, MonstersClues.people_dead_weirdly,
                     MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
    prophet.kill_methods = [MonstersKillMethods.will_of_an_angel, MonstersKillMethods.like_any_human]

    archangel = Monster("Archangel", description="They are heaven's most terrifying weapon. "
                                                 "They are fierce and absolute.", episodes={"S04": [22]})
    archangel.clues = [MonstersClues.small_earth_quake, MonstersClues.bright_light]

    archangel_raphael = Monster("Archangel Raphael", description="One of the Archangels of God. Wanted to bring the "
                                                                 "Apocalypse. Killed by Castiel in S06E22.",
                                episodes={"S04": [18], "S05": [3], "S06": [3, 15, 20, 22]})
    archangel_raphael.clues = [MonstersClues.small_earth_quake, MonstersClues.bright_light, MonstersClues.invulnerable,
                               MonstersClues.can_vanish, MonstersClues.can_hurt_people_with_a_thought,
                               MonstersClues.telekinesis]
    archangel_raphael.disable_methods = [MonstersDisableMethods.holy_oil]
    archangel_raphael.kill_methods = [MonstersKillMethods.archangel_blade,
                                      MonstersKillMethods.will_of_an_angel_on_soul_juice]

    ghoul = Monster("Ghoul", description="Ghoul is a creature, that feeds on dead people. It can take the form of a "
                                         "person that it ate with all memories and thoughts.",
                    episodes={"S04": [19], "S06": [10], "S13": [6]})
    ghoul.clues = [MonstersClues.empty_graves, MonstersClues.body_torn_apart, MonstersClues.missing_body,
                   MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                   MonstersClues.holy_water_does_not_affect_it, MonstersClues.silver_does_not_affect_it,
                   MonstersClues.moves_fast, MonstersClues.bite_marks, MonstersClues.people_dead_weirdly,
                   MonstersClues.high_strength]
    ghoul.kill_methods = [MonstersKillMethods.decapitation, MonstersKillMethods.head_shot]

    archangel_lucyfer = Monster("Archangel - Lucyfer", description="Archangel, that disobeyed God when he requested to "
                                                                   "bow before the men. To upset God he twisted one of "
                                                                   "the people into Lilith. Lucyfer is released from "
                                                                   "his Cage in S11 and is send back not to his cage "
                                                                   "but to cage, where Crowley resides in S12E08. It "
                                                                   "is revealed, that the Cage is not the place where "
                                                                   "Lucyfer is in S12E12. Lucyfer is stuck in "
                                                                   "Alternate timeline in S12E23, back in S13E07. "
                                                                   "Trapped in Apocalypse World in S13E22, but back in "
                                                                   "S13E23. Can consume Nephilim Grace and be more "
                                                                   "powerful. With that power he can kill Archangels "
                                                                   "with hand on forehead. Killed by Dean in S13E23. "
                                                                   "Seen again in Empty in S14E07. Lucyfer is brought "
                                                                   "back by GOD in S15E19 and is killed by Archangel "
                                                                   "Michael in the same episode.",
                                episodes={"S04": [22], "S05": [1, 3, 4, 10, 19, 22], "S07": [1, 2, 15, 17],
                                          "S11": [9, 10, 11, 14, 15, 18, 21, 22],
                                          "S12": [2, 3, 7, 8, 12, 13, 15, 17, 19, 21, 23],
                                          "S13": [1, 2, 7, 12, 13, 18, 21, 22, 23], "S14": [7, 17], "S15": [19]})
    archangel_lucyfer.clues = [MonstersClues.weird_things_behavior, MonstersClues.true_voice_can_hurt_people,
                               MonstersClues.bright_light, MonstersClues.weird_weather, MonstersClues.visions,
                               MonstersClues.people_seeing_strange_things, MonstersClues.biblical_like_events,
                               MonstersClues.people_hear_voices, MonstersClues.can_read_peoples_minds,
                               MonstersClues.can_make_themselves_appear_as_they_like, MonstersClues.cold_spots,
                               MonstersClues.can_give_hallucinations, MonstersClues.can_vanish, MonstersClues.red_eyes,
                               MonstersClues.can_appear_out_of_thin_air, MonstersClues.can_contact_a_person_in_a_dream,
                               MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                               MonstersClues.immune_to_colt_of_colt, MonstersClues.temperature_fluctuations,
                               MonstersClues.flashing_lights, MonstersClues.telekinesis, MonstersClues.double_tongue,
                               MonstersClues.weird_fire_spontaneous_combustion, MonstersClues.revelation_omens,
                               MonstersClues.can_go_and_put_into_a_persons_mind, MonstersClues.can_posses_an_angel,
                               MonstersClues.high_strength, MonstersClues.invulnerable, MonstersClues.can_time_travel,
                               MonstersClues.can_send_people_to_the_past, MonstersClues.people_dead_weirdly,
                               MonstersClues.travels_as_white_fog, MonstersClues.weird_electronics_behavior,
                               MonstersClues.can_repair_human_body, MonstersClues.has_wings, MonstersClues.burned_eyes,
                               MonstersClues.bible_burns_it, MonstersClues.burned_people, MonstersClues.cut_throat,
                               MonstersClues.angel_blade_is_ineffective, MonstersClues.can_eat_angelic_grace,
                               MonstersClues.can_teleport_angels, MonstersClues.can_kill_humans_with_a_thought,
                               MonstersClues.can_bring_back_dead_people, MonstersClues.small_earth_quake,

                               MonstersClues.people_burned_on_the_ceiling,
                               MonstersClues.in_true_form_burns_eyes_of_people]
    archangel_lucyfer.disable_methods = [MonstersDisableMethods.cage_of_lucyfer_in_hell,
                                         MonstersDisableMethods.colt_of_colt_with_magic_bullets,
                                         MonstersDisableMethods.symbol_made_with_blood_against_angels,
                                         MonstersDisableMethods.hand_of_god, MonstersDisableMethods.holy_oil,
                                         MonstersDisableMethods.angel_knuckle_duster]
    archangel_lucyfer.kill_methods = [MonstersKillMethods.archangel_blade, MonstersKillMethods.the_darkness]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 5 ----------------------------------------------------

    archangel_michael = Monster("Archangel - Michael", description="He commands the heavenly host. He was the one, who "
                                                                   "brought down Lucifer to Hell. He did it with his "
                                                                   "sword (Sword of Archangel Michael). Can kill other "
                                                                   "angels with a touch. Another Michael exists in "
                                                                   "alternate timeline. Alternate Timeline Michael is "
                                                                   "killed by Jack in S14E14. Michael is killed in "
                                                                   "S15E19 by GOD.",
                                episodes={"S05": [4, 13, 18, 22], "S13": [2, 7, 14, 22, 23], "S14": [1, 2, 3, 9, 10, 14],
                                          "S15": [8, 19]})
    archangel_michael.clues = [MonstersClues.can_put_a_person_to_sleep, MonstersClues.can_erase_and_bring_back_memories,
                               MonstersClues.can_send_people_back_to_their_time, MonstersClues.can_repair_human_body,
                               MonstersClues.can_kill_angels_with_a_touch, MonstersClues.travels_as_white_fog,
                               MonstersClues.can_go_and_put_into_a_persons_mind, MonstersClues.flashing_lights,
                               MonstersClues.small_earth_quake, MonstersClues.can_sense_number_of_angels_in_the_world,
                               MonstersClues.telekinesis, MonstersClues.burned_eyes, MonstersClues.people_dead_weirdly,
                               MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                               MonstersClues.has_wings, MonstersClues.can_see_real_appearance_of_entities,
                               MonstersClues.falling_meteor, MonstersClues.bright_eyes, MonstersClues.can_vanish,
                               MonstersClues.can_appear_out_of_thin_air, MonstersClues.can_open_rift_to_purgatory,
                               MonstersClues.can_kill_demons_with_power_of_will]
    archangel_michael.disable_methods = [MonstersDisableMethods.holy_oil, MonstersDisableMethods.bad_place_spear,
                                         MonstersDisableMethods.cage_of_lucyfer_in_hell,
                                         MonstersDisableMethods.enochian_handcuffs,
                                         MonstersDisableMethods.sword_of_michael_mind,

                                         MonstersDisableMethods.symbol_made_with_blood_against_angels]
    archangel_michael.kill_methods = [MonstersKillMethods.archangel_blade, MonstersKillMethods.will_of_a_nephilim,
                                      MonstersKillMethods.will_of_god]

    god = Monster("THE GOD", description="The light, the beginning of everything. Brother of the Darkness. A being "
                                         "with almost unlimited power. Only mentioned for now. According to Death - he "
                                         "will die too some day by Death's hand (S05E21). At the end of the S05E22 "
                                         "Chuck disappears, hinting he is THE God. His voice can be heard "
                                         "in S07E01 talking to Castiel. In S11E20 it is revealed, that Chuck Shurley "
                                         "is GOD. According to GOD, he is being, Amara is nothingness. HE created "
                                         "life, because he was lonely. Whenever he created a new world, Amara would "
                                         "destroy it. GOD is heavily weakened by the Darkness in S11E22. In S15E19 GOD "
                                         "becomes human - looses his power to Jack.",
                  episodes={"S11": [4, 20, 21, 22, 23], "S14": [20], "S15": [2, 4, 8, 9, 12, 17, 19]})
    god.clues = [MonstersClues.can_bring_back_dead_angels, MonstersClues.can_teleport_people, MonstersClues.can_vanish,
                 MonstersClues.shining_of_magic_amulet, MonstersClues.visions, MonstersClues.can_appear_out_of_thin_air,
                 MonstersClues.can_bring_back_angelic_grace, MonstersClues.knows_past, MonstersClues.can_kill_nephilim,
                 MonstersClues.can_make_themselves_appear_as_they_like, MonstersClues.weird_electronics_behavior,
                 MonstersClues.weird_things_behavior, MonstersClues.things_disappearing, MonstersClues.telekinesis,
                 MonstersClues.travels_as_white_fog, MonstersClues.can_repair_an_archangel, MonstersClues.burned_eyes,
                 MonstersClues.can_teleport_angels, MonstersClues.can_control_electronics, MonstersClues.invulnerable,
                 MonstersClues.can_give_others_knowledge, MonstersClues.people_cured_miraculously,
                 MonstersClues.people_dead_weirdly, MonstersClues.can_posses_a_person, MonstersClues.high_strength,
                 MonstersClues.lack_of_body_control, MonstersClues.can_hurt_people_with_a_thought]
    god.disable_methods = [MonstersDisableMethods.darkness_powers, MonstersDisableMethods.god_gun,
                           MonstersDisableMethods.power_of_nephilim_on_juice]
    god.kill_methods = [MonstersKillMethods.the_darkness]

    horseman_war = Monster("Horseman War", description="One of the four horseman. Can give people hallucinations with "
                                                       "his ring. The ring is a source of his power.",
                           episodes={"S05": [2]})
    horseman_war.clues = [MonstersClues.people_dead_weirdly, MonstersClues.people_acting_weirdly,
                          MonstersClues.black_eyes, MonstersClues.salt_does_not_affect_it,
                          MonstersClues.people_seeing_strange_things, MonstersClues.immune_to_exorcism,
                          MonstersClues.can_take_form_of_other_people, MonstersClues.can_read_peoples_minds,
                          MonstersClues.can_give_hallucinations]
    horseman_war.disable_methods = [MonstersDisableMethods.demon_killing_knife]

    pagan_god_leshii = Monster("Pagan god Leshi", description="Guardian of the forest in Balkan legends. He is "
                                                              "a mischievous god and can take infinite forms. Can only "
                                                              "be pleased with the blood of his worshippers. He would "
                                                              "drain them, then stuff their stomachs with seeds. "
                                                              "Killed in S05E05 by Sam.",
                               episodes={"S05": [5]})
    pagan_god_leshii.clues = [MonstersClues.weird_electronics_behavior, MonstersClues.weird_things_behavior,
                              MonstersClues.cold_spots, MonstersClues.can_make_themselves_appear_as_they_like,
                              MonstersClues.people_seeing_things_or_figures, MonstersClues.people_dead_weirdly,
                              MonstersClues.seeds_in_victims_stomachs, MonstersClues.can_read_peoples_minds]
    pagan_god_leshii.kill_methods = [MonstersKillMethods.chop_a_head_off_with_an_iron_axe]

    antichrist = Monster("Antichrist", description="Also known as Cambion or Katako. Half-demon, half-human, "
                                                   "but far more powerful than any of them. Can make real, "
                                                   "whatever comes to his mind.",
                         episodes={"S05": [6]})
    antichrist.clues = [MonstersClues.claws, MonstersClues.animal_like_attack, MonstersClues.no_cold_spots,
                        MonstersClues.people_dead_weirdly, MonstersClues.strange_different_things_happening,
                        MonstersClues.no_sulfur, MonstersClues.can_exorcise_demons_with_a_thought,
                        MonstersClues.telekinesis, MonstersClues.can_vanish]

    demon_crowley = Monster("Demon - Crowley", description="Crossroads demon in S05. King of Hell in S06. According to "
                                                           "a crossroads demon, he's real name is Fergus Rodric "
                                                           "MacLeod. He was born in Canisbay, Scotland 1661. "
                                                           "Supposedly died in S06E10, but in S06E19 it is revealed he "
                                                           "was working with Castiel. Crowley sacrifices himself to "
                                                           "close the portal in S12E23.",
                            episodes={"S05": [10, 20, 21], "S06": [4, 7, 8, 10, 19, 20, 21, 22],
                                      "S07": [1, 6, 8, 22, 23], "S08": [1, 2, 7, 10, 17, 19, 21, 22, 23],
                                      "S09": [2, 4, 6, 10, 11, 16, 17, 21, 23],
                                      "S10": [1, 2, 3, 7, 9, 10, 14, 16, 17, 21, 22, 23],
                                      "S11": [1, 2, 3, 6, 9, 10, 14, 15, 18, 22, 23],
                                      "S12": [1, 2, 3, 7, 8, 9, 12, 13, 15, 17, 21, 23]})
    demon_crowley.clues = [MonstersClues.can_vanish, MonstersClues.pact_sealed_with_a_kiss, MonstersClues.telekinesis,
                           MonstersClues.summoned_by_placing_box_in_the_crossroads, MonstersClues.small_earth_quake,
                           MonstersClues.victims_got_better_at_something_up_to_ten_years_earlier,
                           MonstersClues.can_appear_out_of_thin_air, MonstersClues.can_control_electronics,
                           MonstersClues.weird_fire_spontaneous_combustion, MonstersClues.can_become_invisible,
                           MonstersClues.can_bring_back_dead_people, MonstersClues.can_give_people_diseases,
                           MonstersClues.cannot_be_exorcised_by_an_angel_with_hand_on_forehead_when_protected_by_an_archangel,
                           MonstersClues.can_create_fire_large_temperatures, MonstersClues.travels_as_red_fog,
                           MonstersClues.red_eyes, MonstersClues.can_posses_a_person_possessed_by_an_angel,
                           MonstersClues.can_give_hallucinations, MonstersClues.burned_by_holy_water,
                           MonstersClues.can_give_others_knowledge, MonstersClues.can_posses_an_archangel,
                           MonstersClues.can_teleport_people, MonstersClues.can_posses_an_animal]
    demon_crowley.disable_methods = [MonstersDisableMethods.devils_trap, MonstersDisableMethods.will_of_an_archangel,
                                     MonstersDisableMethods.demonic_handcuffs, MonstersDisableMethods.darkness_powers,
                                     MonstersDisableMethods.rowenas_immobilization_spell,
                                     MonstersDisableMethods.holy_water, MonstersDisableMethods.angel_blade,
                                     MonstersDisableMethods.demon_killing_knife]
    demon_crowley.kill_methods = [MonstersKillMethods.angel_blade]

    reaper_death = Monster("Reaper - Death", description="One of the Horseman, the pale rider. Angel of Death. "
                                                         "Can be brought to the Earth at midnight through a place of "
                                                         "awful carnage. Summoned in S05E10 and his actions seen "
                                                         "in S05E15. According to Reaper Billie, this reality has a "
                                                         "rule, that states, if a Reaper Death dies, next reaper to "
                                                         "die, takes his place.",
                           episodes={"S05": [21], "S06": [11], "S07": [1], "S09": [1], "S10": [23]})
    reaper_death.clues = [MonstersClues.number_of_reapers_appearing, MonstersClues.can_bring_back_dead_people,
                          MonstersClues.can_kill_people_with_a_thought, MonstersClues.people_dead_weirdly,
                          MonstersClues.can_appear_out_of_thin_air, MonstersClues.can_put_a_soul_back_to_a_body,
                          MonstersClues.can_go_to_lucifers_cage_and_back_with_ease]
    reaper_death.kill_methods = [MonstersKillMethods.scythe_of_death]

    wraith = Monster("Wraith", description="Creatures, that crack the head and feed on brain juice. Can poison people "
                                           "and drive them crazy. If the spike of a Wraith is broken, it regenerates.",
                     episodes={"S05": [11], "S09": [20], "S13": [3], "S14": [19], "S15": [10]})
    wraith.clues = [MonstersClues.people_dead_weirdly, MonstersClues.no_black_fog, MonstersClues.no_cold_spots,
                    MonstersClues.bite_marks_on_peoples_necks, MonstersClues.people_seeing_strange_things,
                    MonstersClues.victims_brain_devoid_of_water, MonstersClues.silver_burns_its_skin,
                    MonstersClues.can_take_form_of_other_people, MonstersClues.people_seeing_things_or_figures,
                    MonstersClues.people_hear_voices, MonstersClues.long_spike_from_the_arm, MonstersClues.black_blood,
                    MonstersClues.real_appearance_can_be_seen_in_a_reflection_or_camera, MonstersClues.no_sulfur,
                    MonstersClues.high_strength, MonstersClues.people_loosing_their_minds]
    wraith.disable_methods = [MonstersDisableMethods.silver_or_silver_bullets]
    wraith.kill_methods = [MonstersKillMethods.silver_blade]

    cupid = Monster("Cupid", description="A lower tier of an angel - cherub, third class angel. "
                                         "Binds people that are supposed to be with each other. Cupids have angelic "
                                         "grace.", episodes={"S05": [14], "S08": [23], "S10": [18], "S13": [13]})
    cupid.clues = [MonstersClues.people_dead_weirdly, MonstersClues.people_acting_weirdly, MonstersClues.no_emf,
                   MonstersClues.no_sulfur, MonstersClues.marks_on_victims_hearts, MonstersClues.invisible_entity,
                   MonstersClues.can_vanish, MonstersClues.invulnerable, MonstersClues.naked_man]
    cupid.kill_methods = [MonstersKillMethods.angel_blade]

    horseman_famine = Monster("Horseman Famine", description="Makes people starve for something they lack or they want "
                                                             "(sex, attention, food, drugs, love, etc.). Can feed on "
                                                             "souls of his victims or souls of demons. When he eats "
                                                             "souls of demons, he can be killed by a person "
                                                             "with abilities. Killed by Sam in S05E14.",
                              episodes={"S05": [14]})
    horseman_famine.clues = [MonstersClues.people_dead_weirdly, MonstersClues.people_acting_weirdly,
                             MonstersClues.telekinesis, MonstersClues.can_exorcise_demons_with_a_thought,
                             MonstersClues.victims_starve_for_something, MonstersClues.can_read_peoples_minds,
                             MonstersClues.immune_to_extrusion_by_people_with_abilities]
    horseman_famine.kill_methods = [MonstersKillMethods.will_of_a_person_with_abilities]

    zombie = Monster("Zombie", description="A person brought back from the dead by Horseman Death. At first a normal "
                                           "person, after a while turns into human flesh-loving monster.",
                     episodes={"S05": [15]})
    zombie.clues = [MonstersClues.silver_does_not_affect_it, MonstersClues.holy_water_does_not_affect_it,
                    MonstersClues.salt_does_not_affect_it, MonstersClues.missing_body,
                    MonstersClues.feeds_on_human_flesh]
    zombie.kill_methods = [MonstersKillMethods.head_shot]

    angel_joshua = Monster("Angel Joshua", description="Angel, that guards the Heavens garden and the one, "
                                                       "that God talks to. He is killed in S12E19 by Dagon.",
                           episodes={"S05": [16], "S12": [19]})
    angel_joshua.clues = [MonstersClues.can_read_peoples_minds, MonstersClues.can_bring_back_dead_people]
    angel_joshua.kill_methods = [MonstersKillMethods.will_of_prince_of_hell]

    false_prophet = Monster("False Prophet", description="False Prophet rises, when Lucifer walks the Earth. Book of "
                                                         "Revelations calls her 'The Whore of Babylon'. Her goal is to "
                                                         "drag as many souls to Hell as possible. Can only be killed "
                                                         "by a true servant of heaven (like a devoted priest).",
                            episodes={"S05": [17]})
    false_prophet.clues = [MonstersClues.can_read_peoples_minds, MonstersClues.can_take_form_of_other_people,
                           MonstersClues.can_see_future, MonstersClues.telekinesis, MonstersClues.can_control_demons,
                           MonstersClues.visions, MonstersClues.real_appearance_can_be_seen_in_a_reflection_or_camera]
    false_prophet.kill_methods = [MonstersKillMethods.stake_made_from_cypress_tree_in_babylon]

    god_mercury = Monster("God Mercury", description="Roman god of messengers. Died in S05E19.", episodes={"S05": [19]})
    god_mercury.clues = [MonstersClues.moves_fast, MonstersClues.people_dead_weirdly, MonstersClues.immortal,
                         MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                         MonstersClues.can_appear_out_of_thin_air]
    god_mercury.kill_methods = [MonstersKillMethods.will_of_an_archangel]

    ganesh = Monster("Ganesh", description="Hindu Elephant god of success and wisdom. Died in S05E19.",
                     episodes={"S05": [19]})
    ganesh.clues = [MonstersClues.can_appear_as_an_elephant, MonstersClues.people_dead_weirdly, MonstersClues.immortal,
                    MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                    MonstersClues.weird_things_behavior, MonstersClues.people_seeing_strange_things]
    ganesh.kill_methods = [MonstersKillMethods.will_of_an_archangel]

    odin = Monster("Odin", description="Norse god of wisdom, poetry and death. Died in S05E19.", episodes={"S05": [19]})
    odin.clues = [MonstersClues.people_dead_weirdly, MonstersClues.immortal, MonstersClues.weird_things_behavior,
                  MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
    odin.kill_methods = [MonstersKillMethods.will_of_an_archangel]

    kali = Monster("Kali", description="Hindu goddess of death, time and doomsday.", episodes={"S05": [19]})
    kali.clues = [MonstersClues.people_dead_weirdly, MonstersClues.immortal, MonstersClues.telekinesis,
                  MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                  MonstersClues.weird_things_behavior, MonstersClues.seen_as_fire]

    baron_samedi = Monster("Baron Samedi", description="One of the Iwa of Haitian Voodoo. He is the Iwa of the dead. "
                                                       "The master of magic. Died in S05E19.", episodes={"S05": [19]})
    baron_samedi.kill_methods = [MonstersKillMethods.will_of_an_archangel]

    baldur = Monster("Baldur", description="Norse god of good, beauty and wisdom. Died in S05E19.",
                     episodes={"S05": [19]})
    baldur.clues = [MonstersClues.people_dead_weirdly, MonstersClues.immortal, MonstersClues.weird_things_behavior,
                    MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
    baldur.kill_methods = [MonstersKillMethods.stabbing_the_heart]

    zao_shen = Monster("Zao Shen", description="Chinese god of the kitchen. Died in S05E19.", episodes={"S05": [19]})
    zao_shen.clues = [MonstersClues.people_dead_weirdly, MonstersClues.immortal, MonstersClues.weird_things_behavior,
                      MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
    zao_shen.kill_methods = [MonstersKillMethods.stake_made_from_unknown_wood]

    isis = Monster("Isis", description="Egyptian goddess of healing and magic. Died in S05E19.", episodes={"S05": [19]})
    isis.clues = [MonstersClues.people_dead_weirdly, MonstersClues.immortal, MonstersClues.weird_things_behavior,
                  MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
    isis.kill_methods = [MonstersKillMethods.will_of_an_archangel]

    horseman_pestilence = Monster("Horseman Pestilence",
                                  description="One of the horseman, that brings disease and pests.",
                                  episodes={"S05": [19, 21]})
    horseman_pestilence.clues = [MonstersClues.general_sickness, MonstersClues.increased_pest_activity,
                                 MonstersClues.weird_electronics_behavior]

    soulless_person = Monster("Soulless person", description="A person without a soul - only the 'meatsuit'. There is "
                                                             "a way of removing the soul from the body and create "
                                                             "demons out of it (as stated in S09E17). Released soul of "
                                                             "a person will find a way back to a body.",
                              episodes={"S05": [21], "S06": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 22], "S09": [17],
                                        "S11": [2, 5, 6]})
    soulless_person.clues = [MonstersClues.people_acting_weirdly, MonstersClues.lack_of_empathy, MonstersClues.suicides,
                             MonstersClues.no_sulfur, MonstersClues.sociopath_like_behavior, MonstersClues.bright_light,
                             MonstersClues.does_not_sleep, MonstersClues.no_emf, MonstersClues.people_dead_weirdly,
                             MonstersClues.people_seeing_things_or_figures, MonstersClues.holy_water_does_not_affect_it]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 6 ----------------------------------------------------

    alpha_shapeshifter = Monster("Alpha Shapeshifter", description="First of it's kind. Does not shed it's skin to "
                                                                   "change into other people. There is a connection "
                                                                   "between it and it's babies. Even an elephant "
                                                                   "tranquilizes does not affect it long enough. "
                                                                   "Killed in S06E10.",
                                 episodes={"S06": [2, 10]})
    alpha_shapeshifter.clues = [MonstersClues.people_dead_weirdly, MonstersClues.no_sulfur, MonstersClues.moves_fast,
                                MonstersClues.missing_babies, MonstersClues.no_emf, MonstersClues.high_strength,
                                MonstersClues.silver_does_not_affect_it,
                                MonstersClues.can_make_themselves_appear_as_they_like,
                                MonstersClues.missing_or_dead_people_regularly_in_the_same_area]
    alpha_shapeshifter.disable_methods = [MonstersDisableMethods.iridium_or_iridium_blade]
    alpha_shapeshifter.kill_methods = [MonstersKillMethods.iridium_blade_decapitation]

    angel_balthazar = Monster("Angel Balthazar", description="Angel, that stole a lot of angel weapons after the "
                                                             "Apocalypse was canceled. Killed by Castiel in S06E22.",
                              episodes={"S06": [3, 11, 15, 17, 21, 22]})
    angel_balthazar.clues = [MonstersClues.can_vanish, MonstersClues.can_appear_out_of_thin_air,
                             MonstersClues.marks_on_victims_souls, MonstersClues.can_change_the_past]
    angel_balthazar.disable_methods = [MonstersDisableMethods.holy_oil]

    lamia = Monster("Lamia", description="Juices hearts, chugs the blood. These monsters usually appear in Greece.",
                    episodes={"S06": [4]})
    lamia.clues = [MonstersClues.no_emf, MonstersClues.missing_heart, MonstersClues.claws, MonstersClues.no_sulfur,
                   MonstersClues.no_hex_bags]
    lamia.kill_methods = [MonstersKillMethods.silver_knife_blessed_by_a_priest,
                          MonstersKillMethods.mix_of_salt_and_rosemary_thrown_it_and_burned]

    okami = Monster("Okami", description="Monster with fangs like a vampire, but larger and not retractable. "
                                         "Usually appear in Japan.",
                    episodes={"S06": [4]})
    okami.clues = [MonstersClues.people_dead_weirdly, MonstersClues.feeds_on_women_during_their_sleep,
                   MonstersClues.needle_like_teeth, MonstersClues.high_strength]
    okami.kill_methods = [MonstersKillMethods.stab_it_seven_times_with_bamboo_dagger_blessed_by_shinto_priest,
                          MonstersKillMethods.blend_it]

    vampire_alpha = Monster("Vampire Alpha", description="First Vampire. All Vampires are descendants of the Alpha. "
                                                         "Has control over other vampires. He is a son of Eve. Killed "
                                                         "in S12E14 by Sam.",
                            episodes={"S06": [5, 7], "S07": [22], "S12": [14]})
    vampire_alpha.clues = [MonstersClues.can_give_hallucinations, MonstersClues.mind_control, MonstersClues.moves_fast,
                           MonstersClues.great_sense_of_smell, MonstersClues.can_appear_out_of_thin_air,
                           MonstersClues.can_put_a_person_to_sleep, MonstersClues.invulnerable,
                           MonstersClues.needle_like_teeth]
    vampire_alpha.kill_methods = [MonstersKillMethods.colt_of_colt_with_magic_bullets]

    veritas = Monster("Veritas", description="Goddess of Truth. Can be summoned with a cat skull, grains of paradise "
                                             "seed and devil's shoestring. Loves cats, dogs hate her. Can make people "
                                             "tell the truth. Died in S06E06.",
                      episodes={"S06": [6]})
    veritas.clues = [MonstersClues.missing_body, MonstersClues.suicides, MonstersClues.no_emf, MonstersClues.no_sulfur,
                     MonstersClues.no_hex_bags, MonstersClues.blue_eyes, MonstersClues.telekinesis,
                     MonstersClues.high_strength, MonstersClues.people_acting_weirdly]
    veritas.kill_methods = [MonstersKillMethods.silver_knife_dipped_in_dogs_blood]

    fairy = Monster("Fairy", description="Little people with or without wings. Can be mistaken with UFO encounters. "
                                         "They like in another reality - Avalon. Only people, that were in their land "
                                         "and came back can see them. Fairies can be summoned and put back into their "
                                         "land by a spell. They abduct only first sons. There are different kings of "
                                         "fairies. Dark fairies burn, when touched with silver. No matter how "
                                         "powerful, the fairy must stop and count each grain, when salt or sugar is "
                                         "spilled in front of them. If you want to win a fairy's favor, leave a bowl "
                                         "of fresh cream. A fairy can be made to do things with a spell. To release "
                                         "the Fairy one has to destroy the book of magic, that has the power over "
                                         "the fairy.", episodes={"S06": [9], "S08": [11]})
    fairy.clues = [MonstersClues.strange_different_things_happening, MonstersClues.bright_light,
                   MonstersClues.people_seeing_strange_things, MonstersClues.flashing_lights, MonstersClues.no_sulfur,
                   MonstersClues.missing_or_dead_people_regularly_in_the_same_area, MonstersClues.has_wings,
                   MonstersClues.small_people, MonstersClues.high_strength, MonstersClues.invisible_entity,
                   MonstersClues.can_vanish, MonstersClues.can_appear_out_of_thin_air, MonstersClues.no_emf,
                   MonstersClues.can_sense_peoples_souls, MonstersClues.people_dead_weirdly,
                   MonstersClues.tree_tatoo, MonstersClues.animal_like_noises, MonstersClues.no_hex_bags]
    fairy.disable_method = [MonstersDisableMethods.iron_or_iron_bullets, MonstersClues.silver_burns_its_skin,
                            MonstersDisableMethods.spilled_sugar_or_salt]
    fairy.kill_methods = [MonstersKillMethods.microwave_it, MonstersKillMethods.silver_blade]

    dragon = Monster("Dragon", description="Flying creatures form the legends. They like virgins and gold. "
                                           "Live in caves or underground, dark, wet places. They disappeared "
                                           "almost 700 years ago (from 2010).", episodes={"S06": [12]})
    dragon.clues = [MonstersClues.people_seeing_strange_things, MonstersClues.people_dead_weirdly, MonstersClues.claws,
                    MonstersClues.missing_attacked_virgin_women, MonstersClues.has_wings, MonstersClues.likes_gold,
                    MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                    MonstersClues.weird_fire_spontaneous_combustion, MonstersClues.can_create_fire_large_temperatures,
                    MonstersClues.high_strength]
    dragon.disable_methods = [MonstersDisableMethods.blade_forged_with_dragons_blood]
    dragon.kill_methods = [MonstersKillMethods.blade_forged_with_dragons_blood]

    ellie_monster_from_purgatory = Monster("Ellie - Monster from Purgatory",
                                           description="Monster released from Purgatory during H.P. Lovecraft's 1937 "
                                                       "night, that he and his worshipers opened the door to "
                                                       "Purgatory. Possessed a body of a woman Ellie. Died in S06E22.",
                                           episodes={"S06": [12, 21, 22]})
    ellie_monster_from_purgatory.clues = [MonstersClues.weird_things_behavior, MonstersClues.immortal,
                                          MonstersClues.people_dead_weirdly]
    ellie_monster_from_purgatory.kill_methods = [MonstersKillMethods.draining_blood]

    mother_of_all = Monster("Mother of all", description="Mother of all monsters. Was in a Purgatory, until released "
                                                         "in S06E12. Calls herself Eve. She was walking the face of "
                                                         "the Earth 10 000 years ago. Every monster can be traced back "
                                                         "to her. Can talk to every monster, that is alive. "
                                                         "Killed in S06E19.",
                            episodes={"S06": [12, 16, 19]})
    mother_of_all.clues = [MonstersClues.people_acting_weirdly, MonstersClues.weird_electronics_behavior,
                           MonstersClues.mind_control, MonstersClues.people_dead_weirdly, MonstersClues.telekinesis,
                           MonstersClues.people_hear_voices, MonstersClues.can_make_themselves_appear_as_they_like,
                           MonstersClues.can_turn_people_into_monsters, MonstersClues.can_appear_out_of_thin_air,
                           MonstersClues.real_appearance_can_be_seen_in_a_reflection_or_camera, MonstersClues.can_vanish]
    mother_of_all.disable_methods = [MonstersDisableMethods.ashes_of_a_phoenix]
    mother_of_all.kill_methods = [MonstersKillMethods.ashes_of_a_phoenix]

    arachne = Monster("Arachne", description="No one has seen it outside of Crete for 2000 years. "
                                             "When in mating time it has a type, that it likes.",
                      episodes={"S06": [13], "S13": [11]})
    arachne.clues = [MonstersClues.missing_or_dead_people_regularly_in_the_same_area, MonstersClues.left_cobweb,
                     MonstersClues.high_strength, MonstersClues.multiple_pupils, MonstersClues.fire_does_not_affect_it,
                     MonstersClues.head_shot_does_not_affect_it]
    arachne.kill_methods = [MonstersKillMethods.decapitation]

    possessing_worm = Monster("Possessing worm", description="Worm, that can possess a person and control their mind. "
                                                             "It is spread by the Mother of All.",
                              episodes={"S06": [16]})
    possessing_worm.clues = [MonstersClues.amnesia_blackout, MonstersClues.people_acting_weirdly,
                             MonstersClues.black_blood, MonstersClues.mind_control, MonstersClues.worm,
                             MonstersClues.people_dead_weirdly, MonstersClues.invulnerable, MonstersClues.high_strength]
    possessing_worm.disable_methods = [MonstersDisableMethods.electricity]
    possessing_worm.kill_methods = [MonstersKillMethods.electricity]

    fate = Monster("Fate", description="Sisters Fates (Atropos, Clotho and Lachesis) from Greek Mythology. "
                                       "They are responsible for the way you die.", episodes={"S06": [17]})
    fate.clues = [MonstersClues.weird_things_behavior, MonstersClues.people_dead_weirdly, MonstersClues.no_emf,
                  MonstersClues.bad_luck, MonstersClues.left_gold_thread, MonstersClues.can_stop_time]

    phoenix = Monster("Phoenix", description="A creature, that can burn people with it's touch. Dies in a fire.",
                      episodes={"S06": [18]})
    phoenix.clues = [MonstersClues.weird_fire_spontaneous_combustion, MonstersClues.empty_graves,
                     MonstersClues.burned_people, MonstersClues.invulnerable]
    phoenix.disable_methods = [MonstersDisableMethods.iron_or_iron_bullets]
    phoenix.kill_methods = [MonstersKillMethods.colt_of_colt_with_magic_bullets]

    jefferson_starship = Monster("Jefferson Starship", description="A monster, that is a combination of a Vampire and "
                                                                   "a Wraith created by Eve. Dean named it in S06E19 "
                                                                   "and all of them died in the same episode.",
                                 episodes={"S06": [19]})
    jefferson_starship.clues = [MonstersClues.needle_like_teeth, MonstersClues.moving_in_groups_usually,
                                MonstersClues.bright_eyes, MonstersClues.long_spike_from_the_arm,
                                MonstersClues.feeds_on_blood]
    jefferson_starship.kill_methods = [MonstersKillMethods.decapitation, MonstersKillMethods.will_of_an_angel]

    angel_on_soul_juice = Monster("Angel on soul juice", description="Angel, that has taken millions of souls (in "
                                                                     "Castiel case these were Purgatory Souls). "
                                                                     "Possesses GOD-like powers. Castiel made himself "
                                                                     "a new GOD in S06E22. His body will deteriorate "
                                                                     "from the amount of power he holds in himself. "
                                                                     "After letting all creatures out, angel returns "
                                                                     "to his strength.",
                                  episodes={"S06": [22], "S07": [1]})
    angel_on_soul_juice.clues = [MonstersClues.can_appear_out_of_thin_air, MonstersClues.people_dead_weirdly,
                                 MonstersClues.can_kill_archangels_with_finger_snap, MonstersClues.telekinesis,
                                 MonstersClues.angel_blade_is_ineffective, MonstersClues.weird_weather,
                                 MonstersClues.can_hurt_people_with_a_thought, MonstersClues.can_vanish,
                                 MonstersClues.burned_marks_on_its_skin, MonstersClues.weird_electronics_behavior,
                                 MonstersClues.missing_or_dead_people_regularly_in_different_areas,
                                 MonstersClues.sigils_against_angels_are_ineffective,
                                 MonstersClues.can_remove_death_binding_spell]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 7 ----------------------------------------------------

    leviathan = Monster("Leviathan", description="Long before GOD created Angel and man, he made the first beasts - "
                                                 "the Leviathans. GOD was concerned, that they would devour all "
                                                 "creation, so he locked them away in Purgatory. Leviathan description "
                                                 "by Franck Devereaux in S07E20, minute 13. "
                                                 "Kill method revealed in S07E20 in the Word of GOD.",
                        episodes={"S07": [1, 2, 3, 5, 6, 9, 10, 16, 20, 21, 22, 23], "S08": [5, 7], "S10": [19],
                                  "S15": [9]})
    leviathan.clues = [MonstersClues.high_strength, MonstersClues.can_posses_an_angel, MonstersClues.black_veins,
                       MonstersClues.black_blood, MonstersClues.moves_in_water, MonstersClues.people_dead_weirdly,
                       MonstersClues.animal_like_attack, MonstersClues.being_at_two_places_at_once,
                       MonstersClues.can_read_peoples_minds, MonstersClues.can_take_form_of_other_people,
                       MonstersClues.silver_does_not_affect_it, MonstersClues.large_mouth_full_of_teeth,
                       MonstersClues.invulnerable, MonstersClues.double_tongue, MonstersClues.salt_does_not_affect_it,
                       MonstersClues.holy_water_does_not_affect_it, MonstersClues.great_sense_of_smell,
                       MonstersClues.can_make_themselves_appear_as_they_like]
    leviathan.disable_methods = [MonstersDisableMethods.paralyze_spell, MonstersDisableMethods.decapitation,
                                 MonstersDisableMethods.sodium_borate_burns_it, MonstersDisableMethods.head_shot]
    leviathan.kill_methods = [MonstersKillMethods.bone_of_a_righteous_mortal_washed_in_three_bloods_of_the_fallen]

    kitsune = Monster("Kitsune", description="Tey look human, until they sprout out claws and stab you behind "
                                             "your ear to get to your brain - according to young Sam. "
                                             "They need a steady diet of human pituitary gland.", episodes={"S07": [3]})
    kitsune.clues = [MonstersClues.bite_marks_on_peoples_necks, MonstersClues.claws, MonstersClues.cat_eyes,
                     MonstersClues.missing_part_of_the_brain, MonstersClues.people_dead_weirdly, MonstersClues.red_eyes,
                     MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_different_areas]
    kitsune.kill_methods = [MonstersKillMethods.stabbing_the_heart]

    osiris = Monster("Osiris", description="Egyptian God of death and the great judge of the dead. If he gets hold of "
                                           "you, he's judge, jury and executioner. He can see directly into the human "
                                           "heart. He weights the guilt and if there is more than feather's worth - "
                                           "punishes. Leaves egyptian hieroglyphs. Stab with a Ram's horn puts him "
                                           "away for centuries. Put back to the Dead in S07E04.",
                     episodes={"S07": [4]})
    osiris.clues = [MonstersClues.cold_spots, MonstersClues.people_dead_weirdly, MonstersClues.animal_like_attack,
                    MonstersClues.seen_as_car_or_truck, MonstersClues.emf, MonstersClues.left_egyptian_symbols,
                    MonstersClues.can_summon_ghosts, MonstersClues.can_control_ghosts,
                    MonstersClues.can_hurt_people_with_a_thought]
    osiris.disable_methods = [MonstersDisableMethods.stab_with_rams_horn]

    black_goo_monster = Monster("Black Goo Monster", description="A monster with overgrown adrenal glands, that "
                                                                 "increases it's strength drastically. A person can "
                                                                 "become one by eating grey goo. It was developed by "
                                                                 "one of the Leviathans. It works on human DNA from "
                                                                 "the first dose, slowing the metabolism, causing "
                                                                 "weight gain and dampening their emotional range.",
                                episodes={"S07": [9]})
    black_goo_monster.clues = [MonstersClues.body_torn_apart, MonstersClues.grey_goo, MonstersClues.moves_fast,
                               MonstersClues.animal_like_attack, MonstersClues.people_acting_weirdly,
                               MonstersClues.human_like_creature, MonstersClues.people_dead_weirdly,
                               MonstersClues.no_missing_heart, MonstersClues.high_strength,
                               MonstersClues.missing_or_dead_people_regularly_in_the_same_area,
                               MonstersClues.enormous_appetite]
    black_goo_monster.disable_methods = [MonstersDisableMethods.gun_shot]
    black_goo_monster.kill_methods = [MonstersKillMethods.gun_shots]

    vetala = Monster("Vetala", description="Similar to vampires, they feed on blood, but have cat eyes. They're "
                                           "maladjusted loner types and feed slow on people. They have a venom, that "
                                           "they inject into victims. They hunt in pairs (almost always). You have to "
                                           "twist a blade, when stabbed into the heart.",
                     episodes={"S07": [11], "S09": [20]})
    vetala.clues = [MonstersClues.cat_eyes, MonstersClues.blue_eyes, MonstersClues.needle_like_teeth,
                    MonstersClues.no_blood_in_the_body, MonstersClues.animal_like_attack, MonstersClues.high_strength,
                    MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                    MonstersClues.ear_ringing, MonstersClues.people_dead_weirdly, MonstersClues.no_hex_bags,
                    MonstersClues.bite_marks_on_peoples_necks]
    vetala.disable_methods = [MonstersDisableMethods.hit_it_hard_in_the_head]
    vetala.kill_methods = [MonstersKillMethods.silver_blade]

    chronos = Monster("Chronos", description="God of time. Can be summoned in order to compel him to tell "
                                             "your future with a spell. Killed in S07E12.", episodes={"S07": [12]})
    chronos.clues = [MonstersClues.red_light, MonstersClues.people_dead_weirdly, MonstersClues.mummified_body,
                     MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                     MonstersClues.seen_as_a_person_in_a_suit, MonstersClues.weird_electronics_behavior,
                     MonstersClues.immortal, MonstersClues.can_time_travel, MonstersClues.high_strength,
                     MonstersClues.invulnerable]
    chronos.kill_methods = [MonstersKillMethods.olive_pin_dipped_in_blood]

    amazons = Monster("Amazons", description="A tribe of women created by Harmonia and Ares. In their culture, there "
                                             "was no use for men, except procreation. After impregnation, the child, "
                                             "that is a fully grown person after a few days, kills the male, first "
                                             "cutting off certain body parts.", episodes={"S07": [13]})
    amazons.clues = [MonstersClues.people_aging_rapidly, MonstersClues.left_greek_symbol_on_chest,
                     MonstersClues.high_strength, MonstersClues.people_dead_weirdly, MonstersClues.yellow_eyes,
                     MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_different_areas,
                     MonstersClues.snake_eyes]
    amazons.kill_methods = [MonstersKillMethods.gun_shots]

    shojo = Monster("Shojo", description="Japanese alcohol spirit. It roams where there's lots of alcohol. Lore says, "
                                         "that if you were drunk enough, you could see in skulking around breweries "
                                         "in Japan. One can harness the will of a Shojo with the right spell box.",
                    episodes={"S07": [18]})
    shojo.clues = [MonstersClues.weird_noises, MonstersClues.people_dead_weirdly, MonstersClues.invisible_entity,
                   MonstersClues.emf, MonstersClues.body_torn_apart, MonstersClues.people_seeing_things_or_figures,
                   MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                   MonstersClues.ghost_like_creature, MonstersClues.seen_by_drunk_people, MonstersClues.telekinesis,
                   MonstersClues.high_strength]
    shojo.kill_methods = [MonstersKillMethods.samurai_sword_consecrated_with_shinto_blessing]

    ghost_bobby = Monster("Ghost Bobby", description="Ghost of Bobby Singer. Bobby died in S07E10. Bobby turns "
                                                     "Vengeful in S07E23. His flask is burned in the same episode. "
                                                     "Bobby is now in his own personal Heaven.",
                          episodes={"S07": [17, 18, 19, 20, 21, 22, 23], "S10": [17]})
    ghost_bobby.clues = [MonstersClues.weird_things_behavior, MonstersClues.telekinesis, MonstersClues.emf,
                         MonstersClues.can_absorb_other_ghost_energy, MonstersClues.can_appear_out_of_thin_air,
                         MonstersClues.can_vanish, MonstersClues.invisible_entity, MonstersClues.ghost_like_creature,
                         MonstersClues.high_strength, MonstersClues.cold_spots, MonstersClues.can_posses_a_person]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 8 ----------------------------------------------------

    plutus = Monster("Plutus", description="God of greed. Killed in S08E02.", episodes={"S08": [2]})
    plutus.clues = [MonstersClues.can_read_peoples_minds, MonstersClues.can_appear_out_of_thin_air,
                    MonstersClues.can_vanish]
    plutus.kill_methods = [MonstersKillMethods.mjolnir]

    mr_vili = Monster("Mr. Vili", description="Pagan norse god.", episodes={"S08": [2]})
    mr_vili.clues = [MonstersClues.people_dead_weirdly]
    mr_vili.kill_methods = [MonstersKillMethods.mjolnir]

    cacao = Monster("Cacao", description="Mayan god of maize and crop. One can arrange a bargain with it to get "
                                         "immortality ad be successful in sports as long as he does the ritual for "
                                         "Cacao - ripping and eating other peoples hearts twice a year. A person can "
                                         "be killed by stabbing their heart.", episodes={"S08": [3]})
    cacao.clues = [MonstersClues.red_eyes, MonstersClues.missing_heart, MonstersClues.people_dead_weirdly,
                   MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                   MonstersClues.high_strength]

    spectre = Monster("Spectre", description="Ghost-like creature. Spectre is an avenging ghost. It possesses a person "
                                             "and finds out whatever betrayals this person feels and forces one to act "
                                             "on them. The defining characteristic is black-green ectoplasm. "
                                             "Rises shortly after someone desecrated a nearby grave. "
                                             "Spectre is attached to remains or an object.", episodes={"S08": [5]})
    spectre.clues = [MonstersClues.green_ectoplasm, MonstersClues.amnesia_blackout, MonstersClues.empty_graves,
                     MonstersClues.weird_electronics_behavior, MonstersClues.people_acting_weirdly,
                     MonstersClues.people_dead_weirdly, MonstersClues.high_strength]
    spectre.kill_methods = [MonstersKillMethods.destroy_the_object_that_the_ghost_is_bound_to]

    psychokinetic_person = Monster("Psychokinetic person", description="An average psychokinetic can move things with "
                                                                       "his mind, but a powerful psychokinetic can "
                                                                       "reshape reality.", episodes={"S08": [8]})
    psychokinetic_person.clues = [MonstersClues.people_dead_weirdly, MonstersClues.no_hex_bags, MonstersClues.no_emf,
                                  MonstersClues.strange_different_things_happening]
    psychokinetic_person.disable_methods = [MonstersDisableMethods.angel_procedure, MonstersClues.telekinesis]

    knight_of_hell = Monster("Knight of Hell", description="Handpicked by Lucifer himself. They are of the first "
                                                           "fallen firstborn demons, thus very pure and strong. "
                                                           "Archangels killed almost all of them. "
                                                           "One of the survivors is Abaddon. Abaddon is killed in "
                                                           "S09E21 by Dean.",
                             episodes={"S08": [12, 22, 23], "S09": [2, 6, 10, 11, 17, 21]})
    knight_of_hell.clues = [MonstersClues.people_dead_weirdly, MonstersClues.bloodshot_eyes, MonstersClues.black_eyes,
                            MonstersClues.immune_to_exorcism, MonstersClues.can_read_peoples_minds,
                            MonstersClues.demon_killing_knife_is_ineffective, MonstersClues.telekinesis,
                            MonstersClues.can_posses_a_person, MonstersClues.weird_electronics_behavior,
                            MonstersClues.travels_as_black_fog, MonstersClues.high_strength, MonstersClues.can_vanish,
                            MonstersClues.can_exorcise_certain_demons_with_hand_on_forehead, MonstersClues.immortal,
                            MonstersClues.immune_to_exorcism]
    knight_of_hell.disable_methods = [MonstersDisableMethods.demon_killing_knife, MonstersDisableMethods.devils_trap,
                                      MonstersDisableMethods.holy_oil, MonstersDisableMethods.holy_water]
    knight_of_hell.kill_methods = [MonstersKillMethods.first_blade]

    thule = Monster("Thule", description="Members of The Thule Society. Used blood magic to make themselves almost "
                                         "undead. To kill it you have to break it's neck or shoot it in the head and "
                                         "burn the body within 12h.", episodes={"S08": [13], "S11": [14], "S12": [5]})
    thule.clues = [MonstersClues.weird_fire_spontaneous_combustion, MonstersClues.people_dead_weirdly,
                   MonstersClues.immortal, MonstersClues.invulnerable, MonstersClues.burned_people,
                   MonstersClues.no_sulfur, MonstersClues.no_emf]
    thule.kill_methods = [MonstersKillMethods.break_the_neck, MonstersKillMethods.head_shot,
                          MonstersKillMethods.burn_it]

    golem = Monster("Golem", description="Shaped from clay and brought to life by rabbis to protect Jewish people. "
                                         "A golem can be commanded with instructions, that are in a kind of golem "
                                         "manual. One of the instructions said in Hebrew is 'Clay of Adam surrender "
                                         "your bond unto me!'", episodes={"S08": [13]})
    golem.clues = [MonstersClues.invulnerable, MonstersClues.high_strength, MonstersClues.giant_man]

    familiar = Monster("Familiar", description="A companion to some witches. They split their time between human and "
                                               "animal form. They can communicate with their masters telepathically.",
                       episodes={"S08": [15]})
    familiar.clues = [MonstersClues.can_change_into_a_dog, MonstersClues.can_change_into_an_animal,
                      MonstersClues.can_read_peoples_minds]

    prometheus = Monster("Prometheus", description="A Greek proto-god. These gods ruled Greece before Zeus and other "
                                                   "Olympian gods overthrew them. He stole fire for people form Mount "
                                                   "Olympus. In return, Zeus decided to strap him to the mountain and "
                                                   "make him relive death every day. Killed in S08E16.",
                         episodes={"S08": [16]})
    prometheus.clues = [MonstersClues.increased_regeneration, MonstersClues.holy_water_does_not_affect_it,
                        MonstersClues.amnesia_blackout, MonstersClues.silver_does_not_affect_it, MonstersClues.immortal,
                        MonstersClues.comes_back_from_the_dead]
    prometheus.kill_methods = [MonstersKillMethods.the_arrow_of_artemis]

    artemis = Monster("Artemis", description="Zeus' daughter. Has great fighting skills. Has daggers, that can kill "
                                             "immortals. She fell for Prometheus.", episodes={"S08": [16]})
    artemis.clues = [MonstersClues.telekinesis, MonstersClues.can_vanish]

    zeus = Monster("Zeus", description="Olympian god of lightning. Zeus can be summoned by a spell. Spell ingredients: "
                                       "frozen energy from the hand of Zeus (fulgurite) and the bone of a worshipper. "
                                       "Killed in S08E16.", episodes={"S08": [16]})
    zeus.clues = [MonstersClues.lightnings, MonstersClues.can_hurt_people_with_a_thought]
    zeus.kill_methods = [MonstersKillMethods.stake_made_from_a_tree_struck_by_lightning,
                         MonstersKillMethods.the_arrow_of_artemis]

    angel_metatron = Monster("Angel Metatron", description="Scribe of GOD. One of the angels. Metatron broke the "
                                                           "fourth wall in S09E18. His grace was removed in S10E17. "
                                                           "He was killed in S11E21 by Amara.",
                             episodes={"S08": [21, 22, 23], "S09": [9, 10, 18, 22, 23], "S10": [2, 10, 17, 18],
                                       "S11": [6, 20, 21]})
    angel_metatron.clues = [MonstersClues.immortal, MonstersClues.can_vanish, MonstersClues.can_give_hallucinations,
                            MonstersClues.can_erase_anti_angel_marks, MonstersClues.can_appear_out_of_thin_air,
                            MonstersClues.can_repair_human_body, MonstersClues.can_put_down_holy_fire,
                            MonstersClues.telekinesis, MonstersClues.can_teleport_people, MonstersClues.high_strength,
                            MonstersClues.can_give_others_knowledge]
    angel_metatron.disable_methods = [MonstersDisableMethods.grace_removal]

    nephilim = Monster("Nephilim", description="Child of human and Angel/Archangel. Human with an angelic grace. When "
                                               "a Nephilim is conceived, there is a massive surge in celestial energy. "
                                               "Depending on the type of celestial being (Angel/Archangel), the surge "
                                               "differs in power. If Nephilim comes from Lucyfer and the mother "
                                               "touches the Bible - it burns. Nephilim don't need 9 months to fully "
                                               "grow (only about 5). Nephilim does not allow its mother to die and can "
                                               "boost angelic powers. Power of a Nephilim can tear spacetime and open "
                                               "a portal to an alternate timeline. In S12E23 Jack (the son of Lucyfer) "
                                               "is born. Dies in S14E08. Nephilim born from an Archangel is unaffected "
                                               "by Angel blade. A Nephilim becomes more powerful, than the angel, that "
                                               "sired him. Nephilim with the power level of Jack can talk to beings in "
                                               "Empty. A Nephilim can have part of his Grace removed by cutting his "
                                               "throat and allowing the Grace to escape. After that it can take from "
                                               "a month to a century for the Grace to regenerate.",
                       episodes={"S08": [22], "S12": [23], "S13": [1, 2, 3, 4, 6, 9, 14, 20, 21, 22, 23],
                                 "S14": [1, 2, 3, 6, 7, 8, 9, 10, 14, 15, 16, 17, 18, 19, 20],
                                 "S15": [9, 11, 12, 13, 14, 15, 17, 18, 19]})
    nephilim.clues = [MonstersClues.can_see_real_appearance_of_entities, MonstersClues.high_strength,
                      MonstersClues.bright_eyes, MonstersClues.bible_burns_it, MonstersClues.weird_weather,
                      MonstersClues.biblical_like_events, MonstersClues.flashing_lights, MonstersClues.grows_fast,
                      MonstersClues.leaves_burned_marks, MonstersClues.yellow_eyes, MonstersClues.telekinesis,
                      MonstersClues.can_control_electronics, MonstersClues.immune_to_angel_sigils,
                      MonstersClues.angel_blade_is_ineffective, MonstersClues.can_erase_anti_angel_marks,
                      MonstersClues.can_vanish, MonstersClues.invulnerable, MonstersClues.can_hear_angel_radio,
                      MonstersClues.can_put_a_person_to_sleep, MonstersClues.can_go_and_put_into_a_persons_mind,
                      MonstersClues.can_read_peoples_minds, MonstersClues.can_kill_angels_with_power_of_will,
                      MonstersClues.can_travel_to_alternate_timelines, MonstersClues.has_wings,
                      MonstersClues.can_hear_prayers, MonstersClues.can_make_an_archangel_tell_the_truth,
                      MonstersClues.can_kill_archangels_with_finger_snap, MonstersClues.can_repair_human_body,
                      MonstersClues.can_hurt_people_with_a_thought, MonstersClues.can_kill_people_with_a_thought,
                      MonstersClues.can_teleport_people, MonstersClues.can_turn_people_into_pillar_of_salt,
                      MonstersClues.can_make_angels_out_of_people, MonstersClues.ma_lak_box_does_not_trap_it,
                      MonstersClues.can_make_people_tell_the_truth]
    nephilim.kill_methods = [MonstersKillMethods.angel_blade, MonstersKillMethods.archangel_blade,
                             MonstersKillMethods.will_of_god]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 9 ----------------------------------------------------

    wicked_witch = Monster("Wicked Witch", description="Wicked witch from Oz. She can control other people by placing "
                                                       "a hand on their forehead. Then a person's eyes turn intense "
                                                       "green color for a moment and they talk in very monstrous "
                                                       "voice. Her eyes can turn green occasionally too. She can kill "
                                                       "another person with green lightning. One encountered in "
                                                       "1935/1936 in Man of Letters compound in Lebanon, Kansas. "
                                                       "Killed in S09E04.",
                           episodes={"S09": [4]})
    wicked_witch.clues = [MonstersClues.grey_goo, MonstersClues.holy_water_does_not_affect_it, MonstersClues.green_eyes,
                          MonstersClues.burning_does_not_affect_it, MonstersClues.decapitation_does_not_affect_it,
                          MonstersClues.invulnerable, MonstersClues.travels_as_black_green_fog,
                          MonstersClues.green_blood, MonstersClues.high_strength,
                          MonstersClues.can_appear_out_of_thin_air, MonstersClues.seen_as_an_old_lady]
    wicked_witch.disable_methods = [MonstersDisableMethods.devils_trap,
                                    MonstersDisableMethods.bullets_with_poppy_extract]
    wicked_witch.kill_methods = [MonstersKillMethods.magic_red_high_heels]

    rit_zien_angel = Monster("Rit Zien Angel", description="A special class of an angel. Rit Zien in Enochian stands "
                                                           "for 'Hands pf Mercy'. They function like medics. They "
                                                           "healed those, who could be healed, but for the mortally "
                                                           "wounded, their job was to destroy them. Their special "
                                                           "ability is to completely vapourise an entity quickly and "
                                                           "totally. They home in on pain. One encountered Rit Zien "
                                                           "Angel is Ephraim (killed in S09E05)", episodes={"S09": [6]})
    rit_zien_angel.clues = [MonstersClues.purple_pink_light, MonstersClues.people_dead_weirdly, MonstersClues.no_emf,
                            MonstersClues.missing_or_dead_people_regularly_in_the_same_area, MonstersClues.no_sulfur,
                            MonstersClues.no_hex_bags, MonstersClues.vapourised_body, MonstersClues.not_burned_people,
                            MonstersClues.can_appear_out_of_thin_air, MonstersClues.telekinesis,
                            MonstersClues.bright_light]
    rit_zien_angel.disable_methods = [MonstersDisableMethods.symbol_made_with_blood_against_angels]
    rit_zien_angel.kill_methods = [MonstersKillMethods.angel_blade]

    vesta = Monster("Vesta", description="Roman goddess of the hearth. In ancient Rome, six virgins were dedicated "
                                         "to here every year. Their main duty was to tend Vesta's hearth. As long as "
                                         "Vesta's fire was kept lit, Rome received a good harvest. The virgins had to "
                                         "stay celibate for 30 years. If they broke their vows, they were buried "
                                         "alive. Vesta was often enveloped in a blue halo of light, which she could "
                                         "control at will to disorient, to maim or to kill.", episodes={"S09": [8]})
    vesta.clues = [MonstersClues.high_strength, MonstersClues.can_create_fire_large_temperatures,
                   MonstersClues.missing_or_dead_people_regularly_in_the_same_area, MonstersClues.bright_light,
                   MonstersClues.no_white_bright_light, MonstersClues.missing_attacked_broken_virgin_women_or_man,
                   MonstersClues.can_teleport_people, MonstersClues.can_put_a_person_to_sleep]
    vesta.kill_methods = [MonstersKillMethods.stake_made_from_oak_stained_in_virgin_blood]

    cain = Monster("Cain", description="The Father of Murder (according to Crowley from S09E11). After Cain killed "
                                       "Abel he became the deadliest demon on Earth. Killed thousands. He was the "
                                       "first Knight of Hell and trained the rest of the Knights. He has influence on "
                                       "demons. According to Cain, he killed Abel because he made a deal with Lucyfer. "
                                       "Cain's soul in Hell for Abel's soul in Heaven, but Cain was supposed to be the "
                                       "one that kills Abel. He is Adam and Eve's firstborn. Killed in S10E14.",
                   episodes={"S09": [11], "S10": [14]})
    cain.clues = [MonstersClues.invulnerable, MonstersClues.red_light, MonstersClues.immortal, MonstersClues.can_vanish,
                  MonstersClues.can_appear_out_of_thin_air, MonstersClues.can_take_voice_of_a_demon,
                  MonstersClues.can_exorcise_certain_demons_with_hand_on_forehead, MonstersClues.can_teleport_people,
                  MonstersClues.demon_killing_knife_is_ineffective, MonstersClues.weird_electronics_behavior,
                  MonstersClues.flashing_lights, MonstersClues.telekinesis, MonstersClues.no_emf]
    cain.kill_methods = [MonstersKillMethods.first_blade]

    pishtaco = Monster("Pishtaco", description="'Peruvian fat sucker' according to Maritza in S09E13. A monster, that "
                                               "feeds on human fat. They are like parasites. Known Pishtaco are "
                                               "Maritza and Alonso (dead) - siblings).", episodes={"S09": [13]})
    pishtaco.clues = [MonstersClues.people_dead_weirdly, MonstersClues.no_fat_in_the_body, MonstersClues.damaged_organs,
                      MonstersClues.suction_marks, MonstersClues.suction_tongue, MonstersClues.white_eyes,
                      MonstersClues.bite_marks_on_peoples_necks]
    pishtaco.kill_methods = [MonstersKillMethods.cut_its_tongue_out]

    ghost_kevin = Monster("Ghost Kevin", description="Ghost of prophet Kevin Tran. Kevin was killed in S09E09. Kevin "
                                                     "is stuck on Earth even though his body was cremated by Dean. "
                                                     "According to Kevin, every person, that died after the Angels "
                                                     "fell cannot go to Heaven. It is revealed by GOD, that he was in "
                                                     "the Veil the whole time. GOD supposedly moved him to Heaven in "
                                                     "S11E21, but as in S15E02 it is revealed, that he was send to "
                                                     "Hell by GOD.",
                          episodes={"S09": [14], "S11": [21], "S15": [2]})
    ghost_kevin.clues = [MonstersClues.weird_things_behavior, MonstersClues.emf, MonstersClues.ghost_like_creature,
                         MonstersClues.weird_electronics_behavior, MonstersClues.can_appear_out_of_thin_air,
                         MonstersClues.can_vanish, MonstersClues.invisible_entity]

    person_with_mark_of_cain = Monster("Person with Mark of Cain",
                                       description="A person, that was cursed with a Mark of Cain and became a demon. "
                                                   "The Demon part of that person can be cured by Father Thompson's "
                                                   "ritual of curing a Demon.",
                                       episodes={"S09": [23], "S10": [1, 2, 3]})
    person_with_mark_of_cain.clues = [MonstersClues.people_acting_weirdly, MonstersClues.increased_regeneration,
                                      MonstersClues.black_eyes, MonstersClues.high_strength, MonstersClues.deep_voice,
                                      MonstersClues.less_affected_by_telekinesis_of_knight_of_hell,
                                      MonstersClues.comes_back_from_the_dead]
    person_with_mark_of_cain.disable_methods = [MonstersDisableMethods.holy_water,
                                                MonstersDisableMethods.demonic_handcuffs]
    person_with_mark_of_cain.cure_methods = [MonstersCureMethods.demon_curing_ritual]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 10 ---------------------------------------------------

    calliope = Monster("Calliope", description="The Goddess of epic poetry (she is a muse). She is associated with "
                                               "Borage (Starflower). She manifests creatures from the stories she has "
                                               "tuned into. She uses these manifestations to inspire the author and "
                                               "protect them until their vision is realized. After that she eats the "
                                               "author. She is killed by Sam in S10E05.", episodes={"S10": [5]})
    calliope.clues = [MonstersClues.missing_or_dead_people_regularly_in_the_same_area, MonstersClues.telekinesis,
                      MonstersClues.seen_as_a_scarecrow, MonstersClues.left_star_flower_after_kidnapping,
                      MonstersClues.can_teleport_people]
    calliope.kill_methods = [MonstersKillMethods.blessed_wooden_stake]

    soul_doppelganger = Monster("Soul Doppelgänger",
                                description="Two people, that are created out of a good and dark part of the original "
                                            "person's soul. Can be created by Inner key of Ozz. Good and Bad versions "
                                            "of a person are connected physically - if one gets hurt, the other one "
                                            "gets hurt.", episodes={"S10": [11]})
    soul_doppelganger.clues = [MonstersClues.being_at_two_places_at_once, MonstersClues.people_acting_weirdly,
                               MonstersClues.no_sulfur, MonstersClues.no_weird_noises]
    soul_doppelganger.disable_methods = [MonstersDisableMethods.use_inner_key_of_ozz_on_them]
    soul_doppelganger.kill_methods = [MonstersKillMethods.like_any_human, MonstersKillMethods.kill_the_other_version]

    wizard_of_ozz = Monster("Wizard of Ozz", description="A dark version of one of the Man of Letters members - Clive "
                                                         "Dillon. He was kidnapped by coven of witches in Ozz and they "
                                                         "used the inner key on him. The dark version killed all the "
                                                         "witches and went into a tantrum and became the wizard of "
                                                         "Ozz. Killed in S10E11.", episodes={"S10": [11]})
    wizard_of_ozz.clues = [MonstersClues.telekinesis, MonstersClues.magic_abilities]
    wizard_of_ozz.kill_methods = [MonstersKillMethods.kill_the_other_version]

    witch_katja = Monster("Witch Katja", description="Witch from Hanzel & Gretel story. Hanzel became her accomplice "
                                                     "and ate Gretel's heart. She belonged to the same coven as Rowena "
                                                     "and knows her. Killed by Dean in S10E12.", episodes={"S10": [12]})
    witch_katja.clues = [MonstersClues.bright_light, MonstersClues.can_appear_out_of_thin_air, MonstersClues.no_sulfur,
                         MonstersClues.people_seeing_things_or_figures, MonstersClues.people_seeing_strange_things,
                         MonstersClues.strange_different_things_happening, MonstersClues.can_teleport_people,
                         MonstersClues.flower_smell, MonstersClues.left_clothes, MonstersClues.can_make_people_younger,
                         MonstersClues.magic_abilities, MonstersClues.no_cold_spots, MonstersClues.sweets_given_to_eat,
                         MonstersClues.can_make_people_immortal, MonstersClues.seen_as_an_old_lady,
                         MonstersClues.telekinesis]
    witch_katja.kill_methods = [MonstersKillMethods.burn_it]

    khan_worm = Monster("Khan worm", description="Similar to Possessing worm. Transmits via mouth to mouth worm "
                                                 "transmission. Dehydration causes it to come out of its host.",
                        episodes={"S10": [15]})
    khan_worm.clues = [MonstersClues.drained_organs, MonstersClues.no_bone_marrow_in_bones, MonstersClues.no_bite_marks,
                       MonstersClues.people_dead_weirdly, MonstersClues.no_sulfur, MonstersClues.enormous_thirst,
                       MonstersClues.dry_skin, MonstersClues.people_acting_weirdly, MonstersClues.craving_for_blood,
                       MonstersClues.no_cattle_deaths, MonstersClues.no_weird_weather, MonstersClues.worm,
                       MonstersClues.electricity_does_not_affect_it, MonstersClues.high_strength]
    khan_worm.disable_methods = [MonstersDisableMethods.extreme_dehydration]
    khan_worm.kill_methods = [MonstersKillMethods.stamp_on_it]

    styne_family_member = Monster("Styne Family member", description="Member of the Styne (Frankenstein) family - to "
                                                                     "learn more, check The Styne Family in "
                                                                     "Organizations.",
                                  episodes={"S10": [18, 21, 22]})
    styne_family_member.clues = [MonstersClues.people_dead_weirdly, MonstersClues.invulnerable,
                                 MonstersClues.high_strength, MonstersClues.eagle_tatoo]
    styne_family_member.kill_methods = [MonstersKillMethods.head_shot, MonstersKillMethods.gun_shots]

    watcher_angel = Monster("Watcher Angel - Grigori", description="Some lore says, that it feeds on people, some, "
                                                                   "that it helps them. It feeds on a person by "
                                                                   "cutting them and inhaling parts of their souls. "
                                                                   "Once there were hundreds of them. One squad was "
                                                                   "send a long time ago to Earth and went rogue. It "
                                                                   "was believed to be executed, but one of them "
                                                                   "remained - Tamiel (killed in S10E20 by Claire - "
                                                                   "Jimmy Novac's daughter).", episodes={"S10": [20],
                                                                                                         "S15": [11]})
    watcher_angel.clues = [MonstersClues.can_put_a_person_to_sleep, MonstersClues.can_put_a_person_in_wonderland,
                           MonstersClues.can_repair_human_body, MonstersClues.triangle_wound_with_burns,
                           MonstersClues.invulnerable]
    watcher_angel.kill_methods = [MonstersKillMethods.angel_sword, MonstersKillMethods.angel_blade]

    darkness = Monster("Darkness", description="Before there was light, before there was GOD and the archangels, there "
                                               "wasn't nothing. There was the Darkness - horribly destructive, amoral "
                                               "force, that was beaten back by GOD and his archangels in a terrible "
                                               "war. GOD locked the Darkness away where it could do no harm. The Mark "
                                               "of Cain serves as both lock and key for the Darkness. It is released "
                                               "in S10E23 after the Mark was removed from Dean's arm. Sister of God. "
                                               "He was the light, she is the dark. According to Metatron (S11E06) in "
                                               "order for GOD to be able to make Creation, he had to betray her. "
                                               "A being with almost unlimited power. After she was released, the Mark "
                                               "of Cain becomes one with her. She is connected to the person, "
                                               "that had the Mark. In order to grow, she needs to consume Souls (from "
                                               "humans) or Soul energy (like Demons, Angels). She can be knocked out "
                                               "by all of the Angels single blow for a while. If that happens, a lot "
                                               "of darkness is released to the neighbourhood. When she wakes up, she "
                                               "can take in the darkness back, but is hurt by the blow.",
                       episodes={"S10": [23], "S11": [1, 2, 3, 5, 6, 9, 10, 18, 21, 22, 23], "S15": [2, 15, 17]})
    darkness.clues = [MonstersClues.enormous_black_fog, MonstersClues.can_teleport_people, MonstersClues.can_vanish,
                      MonstersClues.seen_as_a_woman, MonstersClues.people_dead_weirdly, MonstersClues.black_veins,
                      MonstersClues.leaves_zombie_like_people_with_black_veins_around_neck, MonstersClues.telekinesis,
                      MonstersClues.weird_weather, MonstersClues.leaves_soulless_people_behind, MonstersClues.visions,
                      MonstersClues.people_feel_spiritual_ecstasy, MonstersClues.grows_fast, MonstersClues.eats_souls,
                      MonstersClues.can_give_hallucinations, MonstersClues.burned_people, MonstersClues.invulnerable,
                      MonstersClues.weird_things_behavior, MonstersClues.can_kill_angels_with_power_of_will,
                      MonstersClues.can_teleport_angels, MonstersClues.can_teleport_archangels, MonstersClues.red_sun,
                      MonstersClues.electrical_storms, MonstersClues.can_shake_heaven, MonstersClues.small_earth_quake,
                      MonstersClues.hand_of_god_does_not_affect_it, MonstersClues.can_remove_protection_sigils,
                      MonstersClues.can_exorcise_archangels, MonstersClues.can_bring_back_dead_people,
                      MonstersClues.travels_as_black_fog, MonstersClues.burned_eyes, MonstersClues.can_repair_god]
    darkness.disable_methods = [MonstersDisableMethods.all_of_angels_single_blow,
                                MonstersDisableMethods.a_few_witches_power, MonstersDisableMethods.lucifers_spear]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 11 ---------------------------------------------------

    rabid = Monster("Rabid", description="Created by The Darkness. The disease can be passed by bleeding on another "
                                         "person. After some time (it is different for every person, it can be "
                                         "4 hours, it can be a day) a person becomes one of them. After a while, "
                                         "a Rabid dies.", episodes={"S11": [1, 2, 20, 21]})
    rabid.clues = [MonstersClues.black_veins, MonstersClues.people_acting_weirdly, MonstersClues.aggression,
                   MonstersClues.intelligent, MonstersClues.infected_with_blood_to_blood_contact,
                   MonstersClues.people_loosing_their_minds, MonstersClues.white_fog]
    rabid.disable_methods = [MonstersDisableMethods.electricity]
    rabid.kill_methods = [MonstersKillMethods.stabbing_the_heart, MonstersKillMethods.shooting_the_heart,
                          MonstersKillMethods.wait_for_it_to_die]
    rabid.cure_methods = [MonstersCureMethods.burning_holy_oil]

    whisper = Monster("Whisper", description="A mix of a Werewolf and a Vampire (Were-pire as called by Dean in "
                                             "S11E04). They were once believed to be in the bloodline of werewolves, "
                                             "but in fact, they are more similar to demons. Their names comes from the "
                                             "fact, that their attacks are very stealthy. Some of them were hunted in "
                                             "the Salem. Feeds only during the solar eclipse. Not seen, only mentioned "
                                             "in S11E04.")
    whisper.clues = [MonstersClues.missing_heart, MonstersClues.body_torn_apart, MonstersClues.no_blood_in_the_body,
                     MonstersClues.animal_like_attack, MonstersClues.feeding_during_solar_eclipse,
                     MonstersClues.needle_like_teeth]
    whisper.kill_methods = [MonstersKillMethods.silver_blade, MonstersKillMethods.decapitation]

    nachzehrer = Monster("Nachzehrer", description="A mix of a Ghul and a Vampire (aka Ghulpire/Were-pire - nickname "
                                                   "by Dean from S11E04). Some feed on the flesh of the dead, some "
                                                   "feed on the blood and hearts of the living. They run in small "
                                                   "packs, but usually keep an extremely low profile. According to "
                                                   "lore, if you kill the pack's Alpha Nachzehrer, the rest is "
                                                   "reverted back to the human form. A human can become a Nachzehrer "
                                                   "after a bite.", episodes={"S11": [4]})
    nachzehrer.clues = [MonstersClues.bright_eyes, MonstersClues.weird_animal_behavior, MonstersClues.skin_left_behind,
                        MonstersClues.ozone_smell, MonstersClues.missing_heart, MonstersClues.animal_like_attack,
                        MonstersClues.no_blood_in_the_body, MonstersClues.body_torn_apart, MonstersClues.high_strength,
                        MonstersClues.silver_does_not_affect_it, MonstersClues.decapitation_does_not_affect_it,
                        MonstersClues.invulnerable]
    nachzehrer.disable_methods = [MonstersDisableMethods.silver_or_silver_bullets, MonstersDisableMethods.decapitation]
    nachzehrer.kill_methods = [MonstersKillMethods.copper_coin_placed_under_the_tongue]

    zanna = Monster("Zanna", description="Invisible entities that help children when they are young. In Romanian lore "
                                         "they guide and protect lost children. Zanna intentionally appear as figments "
                                         "of the child's imagination, allowing the child to move on with confidence "
                                         "once guidance is no longer necessary. Zanna can see another Zanna, but "
                                         "people see Zanna only, when it allows them to see. Zanna can grant other "
                                         "people the ability to see everything, that Zanna see. Zanna share a "
                                         "telepathic link. Zanna can be seen after a proper spell is used.",
                    episodes={"S11": [8]})
    zanna.clues = [MonstersClues.babies_or_children_acting_weirdly, MonstersClues.children_seeing_things_or_figures,
                   MonstersClues.invisible_entity, MonstersClues.kids_imaginary_friend, MonstersClues.glittery_blood,
                   MonstersClues.knife_mark, MonstersClues.can_appear_out_of_thin_air, MonstersClues.can_vanish]
    zanna.kill_methods = [MonstersKillMethods.zanna_killing_knife]

    banshee = Monster("Banshee", description="There are two types of Banshees. Good ones are connected to Fairy lore. "
                                             "They cry out as a warning to a victim's impending death. The other ones "
                                             "are malevolent and feed on vulnerable. They use their piercing scream to "
                                             "drive their prey crazy, forcing their victims to crack out their heads, "
                                             "so that they could feed on them. They hunt the same place, until it is "
                                             "picked clean and only hunt at night. "
                                             "They is usually seen as a floating lady with long, flowing hair, "
                                             "blood-red robes and sunken eyes. The only people, that can hear Banshee "
                                             "are the victims. Victims lack their frontal lobes.",
                      episodes={"S11": [11]})
    banshee.clues = [MonstersClues.feeding_at_night, MonstersClues.flashing_lights, MonstersClues.feeding_on_vulnerable,
                     MonstersClues.emf, MonstersClues.ghost_like_creature, MonstersClues.missing_part_of_the_brain,
                     MonstersClues.people_dead_weirdly, MonstersClues.telekinesis, MonstersClues.victims_hear_screams,
                     MonstersClues.seen_as_a_floating_woman, MonstersClues.black_eyes, MonstersClues.immortal,
                     MonstersClues.long_tongue, MonstersClues.can_vanish, MonstersClues.can_appear_out_of_thin_air,
                     MonstersClues.bright_eyes]
    banshee.disable_methods = [MonstersDisableMethods.celtic_imprisonment_sigil,
                               MonstersDisableMethods.gold_or_golden_blade]
    banshee.kill_methods = [MonstersKillMethods.gold_blade]

    quareen = Monster("Quareen", description="Slave creature with corporeal form. When Kiss of Death curse is layed on "
                                             "a person, Quareen seduces this person as a form of deepest, darkest "
                                             "desire, then kills. The person that possesses a Quareens heart, "
                                             "commands it.", episodes={"S11": [13]})
    quareen.clues = [MonstersClues.people_dead_weirdly, MonstersClues.missing_heart, MonstersClues.animal_like_attack,
                     MonstersClues.high_strength, MonstersClues.being_at_two_places_at_once, MonstersClues.bright_eyes,
                     MonstersClues.keeps_changing_appearances]
    quareen.kill_methods = [MonstersKillMethods.stabbing_the_heart]

    baku = Monster("Baku", description="Japanese monster, that Bobby and Rufus hunted together in Alaska. Not seen, "
                                       "only mentioned in S11E16.")
    baku.clues = [MonstersClues.emf, MonstersClues.weird_noises, MonstersClues.ghost_like_creature,
                  MonstersClues.cold_spots, MonstersClues.flashing_lights, MonstersClues.leaves_burned_marks]

    soul_eater = Monster("Soul Eater", description="Undead ghost-like creature that feeds on souls and existing "
                                                   "between worlds. Soul eater moves into a house and makes a nest, "
                                                   "which exists outside time and space. The nest feels like a house "
                                                   "that a soul eater is in. They aren't really here or there, but can "
                                                   "muster enough strength to bring their victims' souls out of this "
                                                   "world and into their nest. As soon as the victims are in the nest, "
                                                   "they're outside of our space and time. The nest messes with "
                                                   "victims' heads. Shows them things they love, parts of their soul, "
                                                   "in distress. It keeps souls vulnerable. In order to kill the Soul "
                                                   "Eater a proper sigil has to be drawn inside the house and in the "
                                                   "nest. A soul eater can possess a body of a person, that is already "
                                                   "in the nest.", episodes={"S11": [16]})
    soul_eater.clues = [MonstersClues.emf, MonstersClues.victims_in_coma_fading_and_dying, MonstersClues.weird_noises,
                        MonstersClues.ghost_like_creature, MonstersClues.cold_spots, MonstersClues.leaves_burned_marks,
                        MonstersClues.feeling_of_something_bad, MonstersClues.weird_electronics_behavior,
                        MonstersClues.children_seeing_things_or_figures, MonstersClues.salt_does_not_affect_it,
                        MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                        MonstersClues.burning_remains_does_not_affect_it, MonstersClues.victims_dream_about_their_house,
                        MonstersClues.white_eyes, MonstersClues.people_acting_weirdly, MonstersClues.flashing_lights,
                        MonstersClues.can_posses_a_person]
    soul_eater.disable_methods = [MonstersDisableMethods.celtic_sigil_to_trap_monsters]
    soul_eater.kill_methods = [MonstersKillMethods.celtic_sigil]

    bisaan = Monster("Bisaan", description="Cicada-like spirits. Every 27 years they come out and have orgies. They "
                                           "make a specific buzzing/chittering sound when they start to emerge. They "
                                           "are rare in North America. They probably originated in Malaysia's forests. "
                                           "They can't multiply on their own due to a lack of junk, so they 'posses' "
                                           "people to do it. The sound they make is a mating call.",
                     episodes={"S11": [19]})
    bisaan.clues = [MonstersClues.junkless_creature, MonstersClues.mutant_pale_creature, MonstersClues.green_eyes,
                    MonstersClues.weird_noises, MonstersClues.missing_or_dead_people_regularly_in_the_same_area,
                    MonstersClues.needle_like_teeth, MonstersClues.people_seeing_things_or_figures,
                    MonstersClues.people_seeing_strange_things]
    bisaan.kill_methods = [MonstersKillMethods.decapitation]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 12 ---------------------------------------------------

    myling = Monster("Myling", description="Scandinavian vengeful child ghost. They try to lure adults and kill them "
                                           "with their cry. Not seen, only mentioned and suspected in S12E03.")
    myling.clues = [MonstersClues.victims_hear_children_cry, MonstersClues.people_dead_weirdly, MonstersClues.emf,
                    MonstersClues.weird_things_behavior, MonstersClues.leaves_frozen_marks, MonstersClues.frozen_heart,
                    MonstersClues.flashing_lights, MonstersClues.cold_spots]
    myling.disable_methods = [MonstersDisableMethods.iron_or_iron_bullets]
    myling.kill_methods = [MonstersKillMethods.burn_salted_corpse,
                           MonstersKillMethods.destroy_the_object_that_the_ghost_is_bound_to]

    hitler = Monster("Hitler", description="THE Hitler. Resurrected by Nauhaus in S12E05. Killed by Dean in S12E05.",
                     episodes={"S12": [5]})
    hitler.kill_methods = [MonstersKillMethods.head_shot, MonstersKillMethods.burn_it]

    satyr = Monster("Satyr", description="Half man half goat creature from greek mythology. They lead people to the "
                                         "woods to massive orgies. When orgy is over satyr feeds on the victim. Not "
                                         "seen, only mentioned in S12E18.")
    satyr.clues = [MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                   MonstersClues.goat_man]

    moloch = Monster("Moloch", description="God of sacrifice. WHen fed once a year with fresh human blood grants a "
                                           "great wealth. Killed by Sam in S12E18.", episodes={"S12": [18]})
    moloch.clues = [MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                    MonstersClues.goat_man, MonstersClues.high_strength]
    moloch.kill_methods = [MonstersKillMethods.colt_of_colt_with_magic_bullets]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 13 ---------------------------------------------------

    shedim = Monster("Shedim", description="According to Asmodeus Hell's most savage. Things so dark and base, GOD "
                                           "himself would not allow them into the light. Asmodeus believed, that he "
                                           "could train them. Lucyfer feared them, so he forbade it and locked them up "
                                           "again.", episodes={"S13": [2]})
    shedim.clues = [MonstersClues.snake_skin]

    revenant = Monster("Revenant", description="Not seen, only mentioned in S13E04.")
    revenant.clues = [MonstersClues.people_dead_weirdly, MonstersClues.comes_back_from_the_dead, MonstersClues.no_emf,
                      MonstersClues.missing_body]

    empty = Monster("Empty", description="A cosmic being (and a place) that angels and demons go to when they die. "
                                         "THE God has no power there. The Empty cannot go to Earth on its own. It has "
                                         "to be summoned.", episodes={"S13": [4], "S14": [8, 20], "S15": [13, 17, 18]})
    empty.clues = [MonstersClues.can_make_themselves_appear_as_they_like, MonstersClues.can_read_peoples_minds,
                   MonstersClues.telekinesis, MonstersClues.high_strength, MonstersClues.can_posses_an_angel,
                   MonstersClues.black_goo, MonstersClues.can_kill_reapers_with_finger_snap]
    empty.disable_methods = [MonstersDisableMethods.nephilim_bomb]

    dream_walker = Monster("Dream walker", description="A person, that can travel to different worlds with his/her "
                                                       "mind in a dream or by special trans. Kaia is killed in S13E10 "
                                                       "in the Bad Place alternate timeline.",
                           episodes={"S13": [9, 10]})
    dream_walker.clue = [MonstersClues.can_travel_to_alternate_timelines_with_their_mind]

    bad_place_humanoid_monster = Monster("Bad Place humanoid monster",
                                         description="A humanoid creature, that came from the Bad Place (the place,"
                                                     " where Kaia went, when she slept).", episodes={"S13": [9, 10],
                                                                                                     "S15": [12]})
    bad_place_humanoid_monster.clues = [MonstersClues.grey_goo, MonstersClues.claws, MonstersClues.human_like_creature]

    gog_and_magog = Monster("Gog and Magog", description="Ancient warriors, who enslaved half the Fertile Crescent "
                                                         "until some priests cast a spell to bind them away in 'a "
                                                         "place without a place and a time without a time'). They can "
                                                         "only be killed a a weapon touched by GOD. They are brothers. "
                                                         "Their weapons were made by Gods. They are primitive beasts "
                                                         "made of rock and sand. Killed in S13E14 by Dean.",
                            episodes={"S13": [14]})
    gog_and_magog.kill_methods = [MonstersKillMethods.angel_blade, MonstersKillMethods.weapon_touched_by_god]

    yokoth = Monster("Yokoth", description="Star of Madness, Ravager of Galaxies, Mother of Faceless Hordes. God from "
                                           "another dimension summoned by Men of Letters on 1925. It has a mate - "
                                           "Glythur, that she wants to mate with in order to spread. It can't die.",
                     episodes={"S13": [17]})
    yokoth.clues = [MonstersClues.human_like_creature, MonstersClues.purple_eyes, MonstersClues.feeds_on_human_flesh,
                    MonstersClues.people_dead_weirdly, MonstersClues.tentacles, MonstersClues.invulnerable]
    yokoth.disable_methods = [MonstersDisableMethods.special_chains]

    fenrir = Monster("Fenrir", description="One of the sons of Loki. Norse Demigod. Represents a tiger. Killed by "
                                           "Gabriel in S13E20.", episodes={"S13": [20]})
    fenrir.clues = [MonstersClues.claws, MonstersClues.large_mouth_full_of_teeth, MonstersClues.immortal,
                    MonstersClues.astral_projection]
    fenrir.kill_methods = [MonstersKillMethods.gabriel_sword]

    narfi = Monster("Narfi", description="One of the sons of Loki. Norse Demigod. Represents a skul. Killed by Gabriel "
                                         "in S13E20.", episodes={"S13": [20]})
    narfi.clues = [MonstersClues.immortal, MonstersClues.astral_projection]
    narfi.kill_methods = [MonstersKillMethods.gabriel_sword]

    sleipnir = Monster("Sleipnir", description="One of the sons of Loki. Norse Demigod. Represents a horse. Killed by "
                                               "Gabriel in S13E20.", episodes={"S13": [20]})
    sleipnir.clues = [MonstersClues.immortal, MonstersClues.astral_projection]
    sleipnir.kill_methods = [MonstersKillMethods.gabriel_sword]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 14 ---------------------------------------------------

    musca = Monster("Musca", description="A hybrid between a man and a fly. A lot of stories about them exist, but no "
                                         "one has ever seen one in real life. Every few hundred years there's a "
                                         "'bad egg'. When a male fails to find a mate, he abandons his community and "
                                         "starts using people's bodies to nest, biding them together with a viscous "
                                         "goo.", episodes={"S14": [6]})
    musca.clues = [MonstersClues.people_dead_weirdly, MonstersClues.bite_marks, MonstersClues.green_ectoplasm,
                   MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                   MonstersClues.lots_of_flies, MonstersClues.fly_man, MonstersClues.human_like_creature]
    musca.kill_methods = [MonstersKillMethods.brass_nail_dipped_in_sugar_water, MonstersKillMethods.head_shot]

    anubis = Monster("Anubis", description="Guardian of the Dead. Ancient Egyptians believed, that when you die, "
                                           "Anubis would weigh your heart on his scale against justice's feather. His "
                                           "father is Osiris. Anubis works with Heaven. WHen GOD left, Heaven needed "
                                           "a new judge and Anubis was the choice. Can be summoned with a proper spell.",
                     episodes={"S14": [8]})
    anubis.clues = [MonstersClues.human_like_creature, MonstersClues.can_appear_out_of_thin_air,
                    MonstersClues.can_vanish]
    anubis.disable_methods = [MonstersDisableMethods.palm_oil]

    gorgon = Monster("Gorgon", description="An Ancient, cursed being, with an affinity for snakes and a hunger for "
                                           "human flesh. Every few months the Gorgon goes on a spree and gorges itself "
                                           "like a snake. SOme lore says, that Gorgon can tell people's fates and, by "
                                           "consuming human eyes, they may \"glimpse the future\". Cannot see the "
                                           "future of Angels and Nephilims. Killed by Jack in S14E14.",
                     episodes={"S14": [14]})
    gorgon.clues = [MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_different_areas,
                    MonstersClues.people_dead_weirdly, MonstersClues.missing_eyes, MonstersClues.can_see_future,
                    MonstersClues.missing_organs, MonstersClues.snake_skin, MonstersClues.snake_eyes,
                    MonstersClues.paralysis]
    gorgon.kill_methods = [MonstersKillMethods.silver_blade_decapitation]

    kohonta = Monster("Kohonta", description="A monster from Native American legend, that roams the woods \"driven to "
                                             "consume sweet mortal flesh\". They get so starving, they spit up stomach "
                                             "acid. Kohonta means Whistler. They are not born, they are made by a "
                                             "curse.", episodes={"S14": [16]})
    kohonta.clues = [MonstersClues.ripped_throat, MonstersClues.bite_marks, MonstersClues.whistle_noises,
                     MonstersClues.feeds_on_human_flesh, MonstersClues.human_like_creature, MonstersClues.moves_fast,
                     MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
    kohonta.kill_methods = [MonstersKillMethods.silver_blade_through_the_heart]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    # ---------------------------------------------------- SEASON 15 ---------------------------------------------------

    marid = Monster("Marid", description="As song as this monster is fed with blood, it gives one money, health and "
                                         "everything one dreamed of.", episodes={"S15": [7]})
    marid.clues = [MonstersClues.feeds_on_blood, MonstersClues.human_like_creature, MonstersClues.no_blood_in_the_body,
                   MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                   MonstersClues.needle_like_teeth]
    marid.kill_methods = [MonstersKillMethods.decapitation]

    atrox_fortuna = Monster("Atrox Fortuna", description="Roman goddess of luck. She run a bar for people to exchange "
                                                         "luck, but she also took a part of it herself. She has a son "
                                                         "Pax.", episodes={"S15": [11]})
    atrox_fortuna.clues = [MonstersClues.people_dead_weirdly, MonstersClues.bad_luck,
                           MonstersClues.can_make_themselves_appear_as_they_like]

    wood_nymph = Monster("Wood Nymph", description="Wood Nymphs, though naturally docile, react violently when home or "
                                                   "family are threatened. One encountered is Mrs. Butters.",
                         episodes={"S15": [14]})
    wood_nymph.clues = [MonstersClues.magic_abilities, MonstersClues.high_strength, MonstersClues.human_like_creature,
                        MonstersClues.can_sense_peoples_souls, MonstersClues.telekinesis, MonstersClues.green_eyes,
                        MonstersClues.can_repair_human_body, MonstersClues.can_appear_out_of_thin_air,
                        MonstersClues.can_vanish]

    baba_yaga = Monster("Baba Yaga", description="A witch, who feeds on children's fear using hallucinations. She "
                                                 "wears a red ring, that is a source of her power (which is her "
                                                 "heart). If it's broken, witch is disabled.", episodes={"S15": [16]})
    baba_yaga.clues = [MonstersClues.people_seeing_things_or_figures, MonstersClues.weird_electronics_behavior,
                       MonstersClues.people_dead_weirdly, MonstersClues.ghost_like_creature, MonstersClues.invulnerable,
                       MonstersClues.weird_things_behavior, MonstersClues.immortal,
                       MonstersClues.missing_or_dead_children_regularly_in_different_places,
                       MonstersClues.can_make_themselves_appear_as_they_like]
    baba_yaga.disable_methods = [MonstersDisableMethods.separate_the_ring_from_the_body]
    baba_yaga.kill_methods = [MonstersKillMethods.destroy_the_ring]

    # ------------------------------------------------ ALL EPISODES DONE -----------------------------------------------

    def __init__(self):
        self.monsters = [monster for monster in self.__class__.__dict__.values() if isinstance(monster, Monster)]
        self.clues = [clue for key, clue in list(MonstersClues.__dict__.items()) if not key.startswith("__")]
        self.kill_methods = [k_method for key, k_method in list(MonstersKillMethods.__dict__.items())
                             if not key.startswith("__")]
        self.disable_methods = [d_method for key, d_method in list(MonstersDisableMethods.__dict__.items())
                                if not key.startswith("__")]
        self.cure_methods = [cure for key, cure in list(MonstersCureMethods.__dict__.items())
                             if not key.startswith("__")]

    def print_all_sorted_clues(self):
        print(Colors.BOLD + Colors.YELLOW + "\nBase of all clues:" + Colors.ENDC)
        sorted_clues = sorted(self.clues)
        for clue_number, clue in enumerate(sorted_clues, 1):
            print(" »%5d  " % clue_number + clue)

    def print_all_clues(self):
        print(Colors.BOLD + Colors.YELLOW + "\nBase of all clues:" + Colors.ENDC)
        for clue_number, clue in enumerate(sorted(self.clues, key=lambda clue: clue.lower()), 1):
            print(" »%5d  " % clue_number + clue)

    def choose_clues(self) -> List[str]:
        clues = input(Colors.UNDERLINE + "\nChoose clues:" + Colors.ENDC + " ")
        clues = re.sub('[a-zA-Z,&^%$#@?|/:;"_=]', ' ', clues)
        chosen_clues = [sorted(self.clues, key=lambda clue: clue.lower())[int(clue) - 1] for clue in clues.split()
                        if (clue.isdigit() and int(clue) <= len(self.clues))]
        return chosen_clues

    def print_all_matches(self, selected_clues: List[str]):
        print(Colors.YELLOW + "\nSelected clues:" + Colors.ENDC)
        for clue in sorted(selected_clues):
            print(" *  " + clue)
        monster_clues_dict = {}
        for monster_number, monster in enumerate(self.monsters):
            if monster.clues is not None \
                    and (clues_intersection := len(set(monster.clues).intersection(set(selected_clues)))):
                monster_clues_dict[monster_number] = clues_intersection
        sorted_monster_clues_dict = {m: c for m, c in sorted(monster_clues_dict.items(), key=lambda item: item[1],
                                                             reverse=True)}
        print(f"\n{len(sorted_monster_clues_dict)} MATCHING MONSTERS FOUND: \n")
        for monster_number, number_of_matching_clues in sorted_monster_clues_dict.items():
            print(Colors.BOLD + Colors.BLUE + f"{number_of_matching_clues}/{len(selected_clues)} Matches:"
                  + Colors.ENDC, end=" ")
            self.monsters[monster_number].print_all()
            print("")

    def print_all_monsters(self):
        for monster in sorted(self.monsters, key=lambda monster: monster.name):
            monster.print_all()

    def print_monsters_names(self):
        sorted_monsters = sorted([monster.name for monster in self.monsters])
        print(Colors.RED + Colors.BOLD + "All monsters:" + Colors.ENDC)
        for monster in sorted_monsters:
            print(" »  " + monster)

    def print_monster_data_by_name(self, name: str):
        list_of_similarities = {}
        for monster in self.monsters:
            if monster.name.lower() == name.lower():
                monster.print_all()
                break
            list_of_similarities[monster] = difflib.SequenceMatcher(None, monster.name.lower(), name.lower()).ratio()*100
        else:
            print(Colors.RED + Colors.BOLD + f"No monster with name '{name}' found." + Colors.ENDC)
            closest_monster = [monster for monster, ratio in list_of_similarities.items()
                               if ratio == max(list(list_of_similarities.values()))][0]
            print(Colors.BLUE + f"Monster with highest name similarity of {list_of_similarities[closest_monster]:.2f}% is:" + Colors.ENDC)
            closest_monster.print_all()
