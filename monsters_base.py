import re
from typing import List

from monster import Monster
from monsters_data import MonstersClues, MonstersKillMethods, MonstersDisableMethods, MonstersCureMethods
from colors import Colors


class MonsterBase:
    def __init__(self):
        self.clues = [clue for key, clue in list(MonstersClues.__dict__.items()) if not key.startswith("__")]
        self.kill_methods = [k_method for key, k_method in list(MonstersKillMethods.__dict__.items())
                             if not key.startswith("__")]
        self.disable_methods = [d_method for key, d_method in list(MonstersDisableMethods.__dict__.items())
                                if not key.startswith("__")]
        self.cure_methods = [cure for key, cure in list(MonstersCureMethods.__dict__.items())
                             if not key.startswith("__")]

        # -------------------------------------------------- SEASON 1 --------------------------------------------------

        self.prince_of_hell = Monster("Prince of Hell (Azazel - the yellow eyed demon that made people with abilities, "
                                      "Ramiel, Asmodeus, Dagon)",
                                      description="The oldest of old demons. One generation after Lilith. "
                                                  "They were turned by Lucyfer himself before the Atlantis drown. "
                                                  "They were trained to be demonic generals in the war against heaven.",
                                      episodes={"S01": [1, 21, 22], "S02": [1, 21, 22], "S04": [3, 22], "S06": [1]})
        # TODO: Check in which episodes does Azazel appear and check in which he dies (probably in S02E22)
        self.prince_of_hell.clues = [MonstersClues.people_burned_on_the_ceiling, MonstersClues.telekinesis,
                                     MonstersClues.weird_things_behavior, MonstersClues.yellow_eyes,
                                     MonstersClues.children_of_victims_that_died_on_the_ceiling_have_abilities,
                                     MonstersClues.mothers_burned_when_children_are_6_months_old,
                                     MonstersClues.weird_weather, MonstersClues.cattle_deaths,
                                     MonstersClues.temperature_fluctuations, MonstersClues.electrical_storms,
                                     MonstersClues.holy_water_does_not_affect_it, MonstersClues.travels_as_black_fog,
                                     MonstersClues.can_posses_a_reaper, MonstersClues.one_can_make_a_deal_with_it,
                                     MonstersClues.can_show_past_to_people]
        self.prince_of_hell.kill_methods = [MonstersKillMethods.colt_of_colt_with_magic_bullets,

                                            MonstersKillMethods.lance_of_archangel_michael,
                                            MonstersKillMethods.will_of_a_nephilim]

        self.vengeful_spirit = Monster("Vengeful Spirit or Ghost (Bloody Mary, Hook Man)",
                                       description="Appears, when somebody died tragically, committed suicide "
                                                   "or was killed violently. Usually bound to a place or to things. "
                                                   "Ghost can occasionally possess people. "
                                                   "When they do, sometimes they can travel for a while before "
                                                   "coming back to the usual haunting place."
                                                   "Can be summoned by Enochian, necromantic summoning rituals. "
                                                   "Sometimes it's a spirit of a person, that is in the coma. "
                                                   "Ghosts can be forced to rise and keep risen. If it is done with "
                                                   "very powerful spell, then a Mark of Witness remains on them if "
                                                   "they were killed by supernatural. Witnesses can be put to rest "
                                                   "by a special spell (has to be cast over an open fire).",
                                       episodes={"S01": [1, 3, 5, 7, 9, 10, 13, 19], "S02": [6, 11, 16, 18, 19],
                                                 "S03": [5, 6, 13], "S04": [2, 13, 15, 17], "S05": [9, 11],
                                                 "S06": [4, 14]})
        self.vengeful_spirit.clues = [MonstersClues.
                                      missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                                      MonstersClues.people_dead_weirdly, MonstersClues.ghost_like_creature,
                                      MonstersClues.weird_electronics_behavior, MonstersClues.weird_things_behavior,
                                      MonstersClues.local_legend_about_somebody_killed_or_died, MonstersClues.ectoplasm,
                                      MonstersClues.telekinesis, MonstersClues.invisible_entity, MonstersClues.emf,
                                      MonstersClues.missing_body, MonstersClues.high_strength, MonstersClues.cold_spots,
                                      MonstersClues.can_control_water, MonstersClues.people_seeing_things_or_figures,
                                      MonstersClues.summoned_by_saying_bloody_marry_in_front_of_the_mirror,
                                      MonstersClues.objects_seen_in_night_vision, MonstersClues.weird_noises,
                                      MonstersClues.missing_or_dead_people_regularly_in_the_same_area,
                                      MonstersClues.ozone_smell, MonstersClues.seen_as_fire, MonstersClues.no_sulfur,
                                      MonstersClues.people_acting_weirdly, MonstersClues.small_earth_quake,
                                      MonstersClues.seen_as_black_truck, MonstersClues.seen_as_a_little_girl,
                                      MonstersClues.seen_as_a_drown_man, MonstersClues.flashing_lights,
                                      MonstersClues.strange_different_things_happening, MonstersClues.no_missing_heart,
                                      MonstersClues.body_torn_apart, MonstersClues.no_black_fog,
                                      MonstersClues.lack_of_body_control, MonstersClues.scars_on_victims]
        self.vengeful_spirit.disable_methods = [MonstersDisableMethods.bring_the_spirit_to_its_crime_place,
                                                MonstersDisableMethods.bring_the_spirit_what_it_wants,
                                                MonstersDisableMethods.iron_or_iron_bullets,
                                                MonstersDisableMethods.salt_or_salted_bullets,
                                                MonstersDisableMethods.finish_its_unfinished_business]
        self.vengeful_spirit.kill_methods = [MonstersKillMethods.burn_salted_corpse,
                                             MonstersKillMethods.destroy_the_object_that_the_ghost_is_bound_to]

        self.wendigo = Monster("Wendigo", description="Wending in Cree Indian means 'evil, that devours'. "
                                                      "These creatures can live to hundreds of years. "
                                                      "Each Wendigo was once a man. "
                                                      "It's a product of a cannibalism - people in "
                                                      "camps/mineshafts/tribes due to lack of supplies eat others. "
                                                      "Stores other man as a supply for winters as food.",
                               episodes={"S01": [2]})
        self.wendigo.clues = [MonstersClues.missing_or_dead_people_regularly_in_the_same_area,
                              MonstersClues.moves_fast, MonstersClues.strange_roar, MonstersClues.attacks_at_night,
                              MonstersClues.able_to_use_doors, MonstersClues.intelligent, MonstersClues.claws,
                              MonstersClues.animal_like_attack, MonstersClues.silent_area, MonstersClues.high_strength,
                              MonstersClues.mimics_human_voice]
        self.wendigo.disable_methods = [MonstersDisableMethods.symbols_of_anasazi]
        self.wendigo.kill_methods = [MonstersKillMethods.burn_it]

        self.skinwalker = Monster("Skinwalker", description="Can change into an animal anytime. Can infect "
                                                            "other people with a single bite. Basically a werewolf "
                                                            "cousin. Mentioned in S01E02.",
                                  episodes={"S06": [8]})
        self.skinwalker.clues = [MonstersClues.claws, MonstersClues.moves_fast, MonstersClues.people_dead_weirdly,
                                 MonstersClues.animal_like_attack, MonstersClues.missing_heart,
                                 MonstersClues.body_torn_apart, MonstersClues.murders_not_during_full_moon_week,
                                 MonstersClues.can_change_into_a_dog, MonstersClues.great_sense_of_smell]
        self.skinwalker.disable_methods = [MonstersDisableMethods.silver_or_silver_bullets]
        self.skinwalker.kill_methods = [MonstersKillMethods.silver_bullet_into_the_heart]

        self.black_dog = Monster("Black Dog", description="Not seen. Only mentioned in S01E02 and S02E08")
        self.black_dog.clues = [MonstersClues.claws, MonstersClues.moves_fast, MonstersClues.victims_see_black_dogs]

        self.water_wraith = Monster("Water Wraith", description="Not seen. Only mentioned in S01E03")
        self.water_wraith.clues = [MonstersClues.can_control_water]

        self.demon = Monster("Demon", description="In every religion there is information about demonic possessions. "
                                                  "Demons are man that were stuck in hell for a long time.",
                             episodes={"S01": [4, 21, 22], "S02": [1, 14], "S03": [1, 2, 4, 12, 15, 16],
                                       "S04": [1, 4, 9, 10, 20, 21, 22], "S05": [1, 6, 10, 12, 14, 17, 20, 21, 22],
                                       "S06": [7, 10, 18, 20]})
        self.demon.clues = [MonstersClues.black_eyes, MonstersClues.travels_as_black_fog, MonstersClues.emf,
                            MonstersClues.weird_electronics_behavior, MonstersClues.high_strength, MonstersClues.sulfur,
                            MonstersClues.burned_by_holy_water, MonstersClues.reacts_to_gods_name_in_latin,
                            MonstersClues.people_dead_weirdly, MonstersClues.with_a_binding_link_exorcism_does_not_work,
                            MonstersClues.people_acting_weirdly, MonstersClues.can_appear_out_of_thin_air,
                            MonstersClues.amnesia_blackout, MonstersClues.telekinesis, MonstersClues.can_vanish,
                            MonstersClues.lack_of_body_control, MonstersClues.can_hurt_people_with_a_thought,

                            MonstersClues.black_blood]
        self.demon.kill_methods = [MonstersKillMethods.demon_killing_knife, MonstersKillMethods.angel_exorcism,
                                   MonstersKillMethods.colt_of_colt_with_magic_bullets,

                                   MonstersKillMethods.angel_blade, MonstersKillMethods.will_of_an_archangel,
                                   MonstersKillMethods.lance_of_archangel_michael]
        self.demon.disable_methods = [MonstersDisableMethods.holy_water, MonstersDisableMethods.holy_wood,
                                      MonstersDisableMethods.exorcism, MonstersDisableMethods.devils_trap,
                                      MonstersDisableMethods.witch_spell_to_get_a_demon_out_of_the_body,
                                      MonstersDisableMethods.salt_or_salted_bullets,
                                      MonstersDisableMethods.extrusion_by_people_with_abilities,
                                      MonstersDisableMethods.demon_killing_knife]

        self.shapeshifter = Monster("Shapeshifter", description="These creatures can transform themselves into "
                                                                "other man or animals. Can mate with humans to produce "
                                                                "Shapeshifter offspring.",
                                    episodes={"S01": [6], "S02": [12], "S04": [5], "S05": [2]})
        self.shapeshifter.clues = [MonstersClues.can_take_form_of_other_people, MonstersClues.skin_left_behind,
                                   MonstersClues.being_at_two_places_at_once, MonstersClues.bright_eyes,
                                   MonstersClues.weird_animal_behavior, MonstersClues.can_copy_memories_of_other_people,
                                   MonstersClues.people_dead_weirdly, MonstersClues.strange_different_things_happening,
                                   MonstersClues.can_make_themselves_appear_as_they_like, MonstersClues.no_emf,
                                   MonstersClues.no_sulfur, MonstersClues.silver_burns_its_skin,
                                   MonstersClues.missing_or_dead_people_regularly_in_the_same_area]
        self.shapeshifter.kill_methods = [MonstersKillMethods.silver_bullet_into_the_heart,
                                          MonstersKillMethods.silver_blade]

        self.psychic = Monster("Psychic", description="A person, that can read minds, knows past, "
                                                      "present and future of people or in general. "
                                                      "Senses energies and spirits also.",
                               episodes={"S01": [9]})
        self.psychic.clues = [MonstersClues.psychic_abilities,

                              MonstersClues.people_dead_weirdly]
        self.psychic.kill_methods = [MonstersKillMethods.like_any_human]

        self.poltergeist = Monster("Poltergeist", episodes={"S01": [9]})
        self.poltergeist.clues = [MonstersClues.weird_noises, MonstersClues.flashing_lights, MonstersClues.telekinesis,
                                  MonstersClues.weird_things_behavior]
        self.poltergeist.kill_methods = [MonstersKillMethods.angelica_root_mixture]

        self.norwegian_god_vanir = Monster("Norwegian god - Vanir",
                                           description="Norwegian God of the harvest, protection and prosperity. "
                                                       "Once a year it requires a sacrifice of a man and a woman "
                                                       "in order to maintain prosperity. "
                                                       "Sacrifice takes place in April.",
                                           episodes={"S01": [11]})
        self.norwegian_god_vanir.clues = [MonstersClues.missing_or_dead_people_regularly_in_the_same_area,
                                          MonstersClues.emf, MonstersClues.seen_as_a_scarecrow,
                                          MonstersClues.weird_noises]
        self.norwegian_god_vanir.disable_methods = [MonstersDisableMethods.bring_it_what_it_wants]
        self.norwegian_god_vanir.kill_methods = [MonstersKillMethods.burn_the_sacred_tree]

        self.rawhead = Monster("Rawhead", episodes={"S01": [12]})
        self.rawhead.kill_methods = [MonstersKillMethods.apply_large_voltage]

        self.reaper = Monster("Reaper", description="Can give and take life. Can also transfer illnesses of people. "
                                                    "When gone, people are not dying. "
                                                    "When a reaper dies, there are electrical storms.",
                              episodes={"S01": [12], "S02": [1], "S04": [15], "S05": [10, 21], "S06": [11]})
        self.reaper.clues = [MonstersClues.people_dead_weirdly, MonstersClues.people_cured_miraculously,
                             MonstersClues.weird_things_behavior, MonstersClues.people_seeing_things_or_figures,
                             MonstersClues.seen_as_a_person_in_a_suit, MonstersClues.ghost_like_creature,
                             MonstersClues.visible_by_other_ghosts_and_people_close_to_death_only,
                             MonstersClues.can_make_themselves_appear_as_they_like, MonstersClues.people_not_dying,
                             MonstersClues.strange_different_things_happening, MonstersClues.invisible_entity,
                             MonstersClues.electrical_storms]
        self.reaper.disable_methods = [MonstersDisableMethods.reaper_imprison_sigil]
        self.reaper.kill_methods = [MonstersKillMethods.reaper_blade_combined_with_a_spell]

        self.people_with_abilities = Monster("People with abilities",
                                             description="People, that were infants, when prince of hell killed their "
                                                         "mother on the ceiling. Can get stronger, "
                                                         "when consuming demon blood. After using the blood for a long "
                                                         "time, a person becomes addicted to it like to a drug. "
                                                         "With enough power, that person's eyes become black "
                                                         "as for a demon.",
                                             episodes={"S01": [14], "S02": [5, 10], "S03": [16],
                                                       "S04": [1, 4, 7, 9, 15, 16, 18, 20, 21, 22], "S05": [14, 22]})
        self.people_with_abilities.clues = [MonstersClues.people_dead_weirdly, MonstersClues.weird_things_behavior,
                                            MonstersClues.telekinesis, MonstersClues.mind_control,
                                            MonstersClues.able_to_electrocute, MonstersClues.can_see_future,
                                            MonstersClues.people_seeing_things_or_figures,
                                            MonstersClues.their_mother_was_burned_on_the_ceiling_when_they_were_infants,
                                            MonstersClues.as_babies_fed_with_demon_blood,
                                            MonstersClues.immune_to_liliths_yellow_blast,
                                            MonstersClues.can_control_demons, MonstersClues.black_eyes,
                                            MonstersClues.can_send_demons_back_to_hell_with_power_of_will,
                                            MonstersClues.can_kill_demons_with_power_of_will]
        self.people_with_abilities.kill_methods = [MonstersKillMethods.like_any_human]

        self.crazy_humans = Monster("Crazy humans", description="Ordinary humans, that are mad or crazy. "
                                                                "Sometimes can be mistaken for ghosts or vampires.",
                                    episodes={"S01": [15], "S04": [11]})
        self.crazy_humans.clues = [MonstersClues.people_kidnapped_weirdly, MonstersClues.weird_electronics_behavior,
                                   MonstersClues.flashing_lights, MonstersClues.people_seeing_things_or_figures,
                                   MonstersClues.people_dead_weirdly, MonstersClues.weird_things_behavior,
                                   MonstersClues.body_torn_apart, MonstersClues.weird_noises]
        self.crazy_humans.kill_methods = [MonstersKillMethods.like_any_human]

        self.spring_heeled_jacks = Monster("Sprint Heeled Jacks", description="Not seen. Only mentioned in S01E15")
        self.spring_heeled_jacks.clues = [MonstersClues.people_kidnapped_weirdly]

        self.phantom_gassers = Monster("Phantom gassers", description="Not seen. Only mentioned in S01E15")
        self.phantom_gassers.clues = [MonstersClues.people_kidnapped_weirdly]

        self.daeva = Monster("Daeva", description="Zoroastrian demon - demon of darkness", episodes={"S01": [16]})
        self.daeva.clues = [MonstersClues.victims_hear_voices, MonstersClues.seen_as_a_shadow,
                            MonstersClues.animal_like_attack, MonstersClues.emf, MonstersClues.missing_heart,
                            MonstersClues.body_torn_apart, MonstersClues.left_zoroastrian_symbol_made_with_blood,
                            MonstersClues.high_strength, MonstersClues.claws, MonstersClues.invisible_entity]
        self.daeva.kill_methods = [MonstersKillMethods.very_bright_light]
        self.daeva.disable_methods = [MonstersDisableMethods.very_bright_light]

        self.tupla = Monster("Tulpa", description="A Tibetan thought-form. "
                                                  "To summon one there needs to be a tibetan spirit sigil drawn.",
                             episodes={"S01": [17]})
        self.tupla.clues = [MonstersClues.ghost_like_creature, MonstersClues.high_strength,
                            MonstersClues.keeps_changing_appearances, MonstersClues.salt_does_not_affect_it]
        self.tupla.kill_methods = [MonstersKillMethods.make_a_story_that_it_will_unite_with_and_weaken]
        self.tupla.disable_methods = [MonstersDisableMethods.destroy_the_place_that_the_tulpa_resides]

        self.shtriga = Monster("Shtriga", description="Witch-like entity from Albanian folklore. Feeds on life energy, "
                                                      "but particularly on children (also siblings)",
                               episodes={"S01": [18]})
        self.shtriga.clues = [MonstersClues.people_or_children_severely_sick, MonstersClues.no_emf,
                              MonstersClues.nothing_on_ultraviolet, MonstersClues.leaves_burned_marks,
                              MonstersClues.feeding_on_life_essence, MonstersClues.seen_as_human_when_not_feeding,
                              MonstersClues.dead_people_or_children_regularly_in_different_places,
                              MonstersClues.high_strength, MonstersClues.moves_fast,
                              MonstersClues.weird_electronics_behavior]
        self.shtriga.kill_methods = [MonstersKillMethods.consecrated_wrought_iron_when_it_eats]

        self.vampire = Monster("Vampire", description="They were once people. They need fresh human blood to survive. "
                                                      "A coss will not repel them, sunlight will not kill them. "
                                                      "Neither will a stake to the heart. "
                                                      "Vampires nest in groups 8 to 10. "
                                                      "Smaller packs are sent out to hunt for food. "
                                                      "Kidnapped people are taken to nests and then "
                                                      "bleeding them for days or weeks. "
                                                      "One can become a vampire, when drinking vampire blood. "
                                                      "Upon changing, all senses sharpen.",
                               episodes={"S01": [20], "S02": [3], "S03": [7], "S05": [3], "S06": [5, 19]})
        self.vampire.clues = [MonstersClues.ripped_throat, MonstersClues.no_blood_in_the_body,
                              MonstersClues.needle_like_teeth, MonstersClues.moving_in_groups_usually,
                              MonstersClues.invulnerable, MonstersClues.high_strength, MonstersClues.bright_eyes,
                              MonstersClues.great_sense_of_smell, MonstersClues.white_skin, MonstersClues.cattle_deaths,
                              MonstersClues.feeds_on_blood, MonstersClues.bite_marks_on_peoples_necks,
                              MonstersClues.craving_for_blood, MonstersClues.people_dead_weirdly,
                              MonstersClues.missing_or_dead_people_regularly_in_the_same_area, MonstersClues.moves_fast]
        self.vampire.kill_methods = [MonstersKillMethods.decapitation, MonstersKillMethods.angel_blade,
                                     MonstersKillMethods.colt_of_colt_with_magic_bullets,
                                     MonstersKillMethods.will_of_an_angel]
        self.vampire.disable_methods = [MonstersDisableMethods.dead_mans_blood]
        self.vampire.cure_methods = [MonstersCureMethods.cocktail_made_of_blood_of_the_vampire_that_bit_the_victim]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # -------------------------------------------------- SEASON 2 --------------------------------------------------

        self.rakshasa = Monster("Rakshasa", description="Race of ancient Hindu creatures. "
                                                        "They appear in human form and feed on human flesh. "
                                                        "Can make themselves invisible and cannot enter a home "
                                                        "without being invited. "
                                                        "They live in squalor and sleep on a bed of dead insects.",
                                episodes={"S02": [2]})
        self.rakshasa.clues = [MonstersClues.seen_as_a_clown, MonstersClues.people_dead_weirdly,
                               MonstersClues.people_seeing_things_or_figures, MonstersClues.invulnerable,
                               MonstersClues.dead_people_or_children_regularly_in_different_places,
                               MonstersClues.can_become_invisible, MonstersClues.cannot_enter_a_home_without_invitation]
        self.rakshasa.kill_methods = [MonstersKillMethods.dagger_made_of_pure_brass]

        self.resurrected_person = Monster("Resurrected person", description="Brought back from the dead by ancient "
                                                                            "Greek necromancy ritual.",
                                          episodes={"S02": [4]})
        self.resurrected_person.clues = [MonstersClues.people_dead_weirdly, MonstersClues.missing_body,
                                         MonstersClues.weird_plant_deaths_or_behavior, MonstersClues.invulnerable]
        self.resurrected_person.kill_methods = [MonstersKillMethods.nail_it_back_to_the_grave]

        self.death_omen = Monster("Death omen", description="A spirit, that appears, when somebody will die soon.",
                                  episodes={"S02": [7]})
        self.death_omen.clues = [MonstersClues.invisible_entity, MonstersClues.people_dead_weirdly,
                                 MonstersClues.people_seeing_things_or_figures, MonstersClues.flashing_lights,
                                 MonstersClues.weird_electronics_behavior]
        self.death_omen.disable_methods = [MonstersDisableMethods.bring_the_spirit_what_it_wants]

        self.hell_hound = Monster("Hell Hound", description="Creation of God, but they were too vicious, "
                                                            "so God kept them short. "
                                                            "Now they hunt people that sold their souls.",
                                  episodes={"S02": [8], "S03": [16], "S05": [10, 20], "S06": [4, 10]})
        self.hell_hound.clues = [MonstersClues.victims_hear_dogs_barking_and_growling, MonstersClues.invisible_dogs,
                                 MonstersClues.victims_see_black_dogs, MonstersClues.people_seeing_strange_things,
                                 MonstersClues.victims_got_better_at_something_up_to_ten_years_earlier,
                                 MonstersClues.people_dead_weirdly, MonstersClues.animal_like_attack,
                                 MonstersClues.black_blood]
        self.hell_hound.disable_methods = [MonstersDisableMethods.goofer_dust, MonstersDisableMethods.devils_shoestring,
                                           MonstersDisableMethods.demon_must_call_it_off,
                                           MonstersDisableMethods.salt_or_salted_bullets]
        self.hell_hound.kill_methods = [MonstersKillMethods.demon_killing_knife, MonstersKillMethods.angel_sword,
                                        MonstersKillMethods.colt_of_colt_with_magic_bullets,
                                        MonstersKillMethods.angel_blade]

        self.crossroads_demon = Monster("Crossroads demon", description="One can make a deal with that demon. "
                                                                        "Can give anything, but will collect ones soul "
                                                                        "after 10 years. One can summon it by placing "
                                                                        "a box with: graveyard dirt, black cat cone, "
                                                                        "ones photo in the center of a crossroad.",
                                        episodes={"S02": [8, 22], "S04": [9], "S05": [10], "S06": [4]})
        self.crossroads_demon.clues = [MonstersClues.victims_got_better_at_something_up_to_ten_years_earlier,
                                       MonstersClues.red_eyes, MonstersClues.summoned_by_placing_box_in_the_crossroads,
                                       MonstersClues.travels_as_black_fog, MonstersClues.pact_sealed_with_a_kiss]
        self.crossroads_demon.disable_methods = [MonstersDisableMethods.devils_trap,
                                                 MonstersDisableMethods.fry_its_remains]
        self.crossroads_demon.kill_methods = [MonstersKillMethods.colt_of_colt_with_magic_bullets,
                                              MonstersKillMethods.demon_killing_knife,
                                              MonstersKillMethods.burn_the_remains]

        self.demonic_virus = Monster("Demonic virus", description="Probably caused Roanoke colony disappearance. "
                                                                  "Croatoan might be a name of the demon. "
                                                                  "Names also include Dever and Reshef - "
                                                                  "demon of plague and pestilence.",
                                     episodes={"S02": [9]})
        self.demonic_virus.clues = [MonstersClues.people_acting_weirdly, MonstersClues.sulfur_in_the_blood,
                                    MonstersClues.elevated_lymphocyte_percentage, MonstersClues.high_strength,
                                    MonstersClues.infected_with_blood_to_blood_contact]
        self.demonic_virus.kill_methods = [MonstersKillMethods.like_any_human]
        self.demonic_virus.disable_methods = [MonstersDisableMethods.wait_until_its_over]

        self.angel_like_spirit = Monster("Angel-like spirit", description="Spirit of a person that died tragically "
                                                                          "(like vengeful spirit), but instead of evil,"
                                                                          " that spirit becomes better-ish.",
                                         episodes={"S02": [13]})
        self.angel_like_spirit.clues = [MonstersClues.flashing_lights, MonstersClues.weird_electronics_behavior,
                                        MonstersClues.people_seeing_things_or_figures, MonstersClues.people_hear_voices,
                                        MonstersClues.weird_things_behavior, MonstersClues.small_earth_quake,
                                        MonstersClues.people_seeing_figure_of_light, MonstersClues.knows_past,
                                        MonstersClues.no_emf, MonstersClues.people_feel_spiritual_ecstasy,
                                        MonstersClues.can_read_peoples_minds, MonstersClues.no_sulfur]
        self.angel_like_spirit.disable_methods = [MonstersDisableMethods.give_it_last_rites]

        self.trickster = Monster("Trickster (Loki, Anansi)", description="Demigod (Loki in Scandinavia, Anansi in "
                                                                         "West Africa). Can create chaos and mischief "
                                                                         "as easy as breathing. Not seen, "
                                                                         "only appeared to be one, but it was "
                                                                         "Archangel Gabriel.")
        self.trickster.clues = [MonstersClues.people_seeing_things_or_figures, MonstersClues.people_dead_weirdly,
                                MonstersClues.no_emf, MonstersClues.weird_noises, MonstersClues.people_seeing_aliens,
                                MonstersClues.strange_different_things_happening, MonstersClues.things_disappearing,
                                MonstersClues.can_create_things_out_of_thin_air, MonstersClues.immortal,
                                MonstersClues.can_make_themselves_appear_as_they_like, MonstersClues.loves_sugar,
                                MonstersClues.telekinesis, MonstersClues.sweets_wrappers, MonstersClues.can_vanish,
                                MonstersClues.people_seeing_strange_things, MonstersClues.mimics_human_voice,
                                MonstersClues.high_strength]
        self.trickster.kill_methods = [MonstersKillMethods.aspen_pin]

        self.archangel_gabriel = Monster("Archangel - Gabriel", description="Archangel, that enjoys tricking people "
                                                                            "and killing them afterwards. "
                                                                            "Died in S05E19.",
                                         episodes={"S02": [15], "S03": [11], "S05": [8, 19]})
        self.archangel_gabriel.clues = [MonstersClues.people_seeing_things_or_figures, MonstersClues.telekinesis,
                                        MonstersClues.no_emf, MonstersClues.weird_noises, MonstersClues.loves_sugar,
                                        MonstersClues.people_seeing_aliens, MonstersClues.things_disappearing,
                                        MonstersClues.strange_different_things_happening, MonstersClues.immortal,
                                        MonstersClues.can_create_things_out_of_thin_air, MonstersClues.can_reverse_time,
                                        MonstersClues.people_dead_weirdly, MonstersClues.people_seeing_strange_things,
                                        MonstersClues.can_put_people_into_alternate_timelines, MonstersClues.can_vanish,
                                        MonstersClues.sweets_wrappers, MonstersClues.mimics_human_voice,
                                        MonstersClues.high_strength, MonstersClues.can_teleport_people,
                                        MonstersClues.can_make_themselves_appear_as_they_like, MonstersClues.has_wings,
                                        MonstersClues.can_put_somebody_in_a_time_loop, MonstersClues.bright_light]
        self.archangel_gabriel.disable_methods = [MonstersDisableMethods.holy_oil]
        self.archangel_gabriel.kill_methods = [MonstersKillMethods.archangel_blade]

        self.phantom_hitchhiker = Monster("Phantom hitchhiker", description="Not seen. Only mentioned in S01E16")
        self.phantom_hitchhiker.clues = [MonstersClues.missing_or_dead_people_regularly_in_the_same_area]

        self.werewolf = Monster("Werewolf", description="Human by day, animal killing machine by moonlight. "
                                                        "Killing a werewolf, that bit a person "
                                                        "does not revert the curse. "
                                                        "Also mentioned in S01E16", episodes={"S02": [17]})
        self.werewolf.clues = [MonstersClues.body_torn_apart, MonstersClues.animal_like_attack,
                               MonstersClues.missing_heart, MonstersClues.murders_during_full_moon_week,
                               MonstersClues.claws, MonstersClues.attacks_at_night, MonstersClues.animal_like_noises,
                               MonstersClues.amnesia_blackout]
        self.werewolf.kill_methods = [MonstersKillMethods.silver_bullet_into_the_heart]
        self.werewolf.cure_methods = \
            [MonstersCureMethods.plasma_therapy_with_the_blood_of_the_werewolf_that_bit_the_victim]

        self.jinn = Monster("Jinn", description="Mythical creatures, that feed on people. They have godlike power "
                                                "and can shaper reality as they like. Usually reside in ruins - "
                                                "the bigger, the better. They poison people, who see nightmares or "
                                                "paradise of theirs. The poison is transferred by touch. "
                                                "It can be cured. Not all Jinn look different than humans, "
                                                "some look just like regular people.",
                            episodes={"S02": [20], "S06": [1]})
        self.jinn.clues = [MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                           MonstersClues.blue_eyes, MonstersClues.can_put_a_person_in_wonderland,
                           MonstersClues.blue_fire_on_its_arms, MonstersClues.feeds_on_blood,
                           MonstersClues.poisoned_people, MonstersClues.people_dead_weirdly,
                           MonstersClues.seen_as_human_when_not_feeding, MonstersClues.people_seeing_strange_things]
        self.jinn.kill_methods = [MonstersKillMethods.silver_knife_dipped_in_lambs_blood]

        self.acheri = Monster("Acheri", description="Demon, that disguises itself as a little girl.",
                              episodes={"S02": [21]})
        self.acheri.clues = [MonstersClues.seen_as_a_little_girl, MonstersClues.claws, MonstersClues.animal_like_attack]
        self.acheri.disable_methods = [MonstersDisableMethods.iron_or_iron_bullets]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # -------------------------------------------------- SEASON 3 --------------------------------------------------

        self.seven_deadly_sins = Monster("Seven deadly sins", description="In 1589 Binsfeld's classification of demons,"
                                                                          " he IDd all of them not just as human vices "
                                                                          "but as actual devils.",
                                         episodes={"S03": [1]})
        self.seven_deadly_sins.clues = [MonstersClues.black_eyes, MonstersClues.mind_control, MonstersClues.no_emf,
                                        MonstersClues.burned_by_holy_water, MonstersClues.travels_as_black_fog,
                                        MonstersClues.people_acting_weirdly, MonstersClues.people_dead_weirdly,
                                        MonstersClues.no_sulfur, MonstersClues.can_read_peoples_minds,
                                        MonstersClues.weird_electronics_behavior, MonstersClues.high_strength]
        self.seven_deadly_sins.kill_methods = [MonstersKillMethods.demon_killing_knife]
        self.seven_deadly_sins.disable_methods = [MonstersDisableMethods.holy_water, MonstersDisableMethods.devils_trap,
                                                  MonstersDisableMethods.exorcism]

        self.changeling = Monster("Changeling", description="Evil monster babies/children. They can perfectly mimic "
                                                            "children. According to lore, they climb the window and "
                                                            "kidnap the kid. Feeding on moms' synovial fluid. "
                                                            "They can feed on a victim for months. "
                                                            "Kidnapped kids are hidden usually underground. "
                                                            "There can be a mother changeling. "
                                                            "Burning her burns also kid changelings.",
                                  episodes={"S03": [2]})
        self.changeling.clues = [MonstersClues.weird_things_behavior, MonstersClues.babies_or_children_acting_weirdly,
                                 MonstersClues.missing_or_dead_people_regularly_in_the_same_area,
                                 MonstersClues.bite_marks_on_peoples_necks, MonstersClues.people_dead_weirdly,
                                 MonstersClues.feeding_at_night, MonstersClues.may_leave_claw_marks,
                                 MonstersClues.real_appearance_can_be_seen_in_a_reflection_or_camera]
        self.changeling.kill_methods = [MonstersKillMethods.burn_it]

        self.krampus = Monster("Krampus", description="Evil brother of Santa. Comes in many names - Belsnickel, "
                                                      "Black Peter. Lore says, that Santa's brother went rogue and now "
                                                      "he punishes the wicked around Christmas time. "
                                                      "Not seen, only mentioned in S03E08")
        self.krampus.clues = [MonstersClues.weird_noises, MonstersClues.people_dead_weirdly,
                              MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                              MonstersClues.missing_or_dead_people_around_christmas,
                              MonstersClues.seen_as_a_santa_like_figure]

        self.holdenacar = Monster("Holdenacar", description="God of the winter solstice. Attracted to meadowsweet, "
                                                            "which is one of the most powerful plants in pagan lore",
                                  episodes={"S03": [8]})
        self.holdenacar.clues = [MonstersClues.missing_or_dead_people_regularly_in_different_areas,
                                 MonstersClues.weird_noises, MonstersClues.people_dead_weirdly,
                                 MonstersClues.missing_or_dead_people_around_christmas, MonstersClues.high_strength,
                                 MonstersClues.seen_as_a_santa_like_figure,
                                 MonstersClues.victims_have_meadowsweet_somewhere, MonstersClues.weird_weather]
        self.holdenacar.kill_methods = [MonstersKillMethods.evergreen_pin]

        self.witch = Monster("Witch", description="A woman/man, that deals with different kinds of magic (like black, "
                                                  "old world, etc.). Witch has magic powers, can bring demons, "
                                                  "be immortal, teleport etc.",
                             episodes={"S03": [9], "S04": [7, 12], "S05": [7, 12]})
        self.witch.clues = [MonstersClues.people_dead_weirdly, MonstersClues.hex_bag_hidden_somewhere,
                            MonstersClues.weird_electronics_behavior, MonstersClues.telekinesis,
                            MonstersClues.can_vanish, MonstersClues.immortal, MonstersClues.invulnerable,
                            MonstersClues.telekinesis, MonstersClues.card_found_on_a_victim,
                            MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                            MonstersClues.people_aging_rapidly, MonstersClues.people_getting_younger,
                            MonstersClues.people_with_souls_switched,

                            MonstersClues.missing_heart]
        self.witch.disableMethod = [MonstersDisableMethods.stop_it_from_speaking,
                                    MonstersDisableMethods.witch_catcher]
        self.witch.kill_methods = [MonstersKillMethods.like_any_human, MonstersKillMethods.death_transfer_spell,
                                   MonstersKillMethods.witch_killing_brew, MonstersKillMethods.cut_throat,
                                   MonstersClues.red_eyes]

        self.demon_astaroth = Monster("Demon Astaroth", description="Collects human souls by changing them into "
                                                                    "witches.",
                                      episodes={"S03": [9]})
        self.demon_astaroth.clues = [MonstersClues.black_eyes, MonstersClues.telekinesis, MonstersClues.high_strength,
                                     MonstersClues.can_stop_bullets]
        self.demon_astaroth.kill_methods = [MonstersKillMethods.demon_killing_knife]

        self.first_demon = Monster("First Demon - Lilith", description="First demon created by Lucifer out of a human "
                                                                       "soul by twisting it.",
                                   episodes={"S03": [12, 16], "S04": [18, 22]})
        self.first_demon.clues = [MonstersClues.white_eyes, MonstersClues.yellow_blast, MonstersClues.telekinesis,
                                  MonstersClues.travels_as_black_fog,
                                  MonstersClues.unable_to_hurt_people_with_abilities_with_its_yellow_blast]
        self.first_demon.kill_methods = [MonstersKillMethods.will_of_a_person_with_abilities]

        self.death_echo = Monster("Death echo", description="Echos are trapped in a loop. They keep replaying how they "
                                                            "died over and over again usually at the place of death.",
                                  episodes={"S03": [13]})
        self.death_echo.clues = [MonstersClues.ghost_like_creature, MonstersClues.can_vanish, MonstersClues.emf,
                                 MonstersClues.weird_electronics_behavior]
        self.death_echo.disable_methods = [MonstersDisableMethods.shock_it_out_of_its_loop]

        self.crocotta = Monster("Crocotta", description="Soul scavenger. Mimics loved ones. Whispers \"Come to me\", "
                                                        "then lures victims into the dark and swallows their souls. "
                                                        "Usually live in filth.",
                                episodes={"S03": [14]})
        self.crocotta.clues = [MonstersClues.people_dead_weirdly, MonstersClues.weird_electronics_behavior,
                               MonstersClues.contact_from_dead_people, MonstersClues.tells_victims_come_to_me,
                               MonstersClues.needle_like_teeth, MonstersClues.can_control_electronics]
        self.crocotta.kill_methods = [MonstersKillMethods.sharp_object_into_the_spine]

        self.eternal_living_person = Monster("Eternal living person", description="Person, that can live forever in "
                                                                                  "theory by replacing faulty organs.",
                                             episodes={"S03": [15]})
        self.eternal_living_person.clues = [MonstersClues.missing_organs, MonstersClues.people_dead_weirdly,
                                            MonstersClues.invulnerable]
        self.eternal_living_person.disable_methods = [MonstersDisableMethods.chloroform,
                                                      MonstersDisableMethods.bury_it_alive]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # -------------------------------------------------- SEASON 4 --------------------------------------------------

        self.angel = Monster("Angel", description="Angel of God (Castiel, Uriel). "
                                                  "They can bring people back from the dead. Cannot track people, "
                                                  "that use powerful spells to hide themselves. "
                                                  "All angels have graces - energy source for their power. "
                                                  "When they disobey (fall), as a punishment they can become human. "
                                                  "When dying, a bright light is produced and they leave wing marks. "
                                                  "To possess somebody, they need a consent. Castiel broke the fourth "
                                                  "wall in S06E20.",
                             episodes={"S04": [1, 2, 7, 9, 10, 15, 16, 18, 20, 21, 22],
                                       "S05": [1, 2, 3, 4, 5, 8, 10, 12, 13, 14, 15, 16, 17, 18, 21, 22],
                                       "S06": [3, 6, 7, 10, 12, 15, 17, 18, 19, 20]})
        self.angel.clues = [MonstersClues.can_bring_back_dead_people, MonstersClues.in_true_form_burns_eyes_of_people,
                            MonstersClues.place_where_person_was_resurrected_looks_like_after_explosion,
                            MonstersClues.leaves_burned_marks, MonstersClues.weird_electronics_behavior,
                            MonstersClues.can_repair_human_body, MonstersClues.telekinesis, MonstersClues.invulnerable,
                            MonstersClues.can_put_a_person_to_sleep, MonstersClues.demon_killing_knife_is_ineffective,
                            MonstersClues.has_wings, MonstersClues.true_voice_can_hurt_people, MonstersClues.can_vanish,
                            MonstersClues.immune_to_salt_rounds, MonstersClues.immune_to_devils_trap,
                            MonstersClues.can_contact_a_person_in_a_dream, MonstersClues.can_send_people_to_the_past,
                            MonstersClues.can_appear_out_of_thin_air, MonstersClues.high_strength,
                            MonstersClues.can_exorcise_certain_demons_with_hand_on_forehead, MonstersClues.bright_light,
                            MonstersClues.mimics_human_voice, MonstersClues.can_control_electronics,
                            MonstersClues.triangle_wound, MonstersClues.amnesia_blackout,
                            MonstersClues.can_teleport_people, MonstersClues.can_read_peoples_minds,
                            MonstersClues.can_become_invisible, MonstersClues.can_control_demons,

                            MonstersClues.travels_as_white_fog]
        self.angel.disable_methods = [MonstersDisableMethods.symbol_made_with_blood_against_angels,
                                      MonstersDisableMethods.exorcism_for_angels, MonstersDisableMethods.holy_oil,
                                      MonstersDisableMethods.enochian_spell, MonstersDisableMethods.angel_blade,
                                      MonstersDisableMethods.presence_of_the_mother]
        self.angel.kill_methods = [MonstersKillMethods.angel_blade, MonstersKillMethods.holy_oil,

                                   MonstersKillMethods.will_of_an_archangel, MonstersKillMethods.will_of_prince_of_hell,
                                   MonstersKillMethods.lance_of_archangel_michael]

        self.rougarou = Monster("Rougarou", description="Once a human. Now - rotten teeth, wormy skin. "
                                                        "When going through metamorphosis, their hunger increases. "
                                                        "At first for everything, but after a while - for human flesh. "
                                                        "Hunger grows, until it is irresistible. After the first bite "
                                                        "of the human flesh, they transform completely and fast. "
                                                        "They feed once, they're a monster forever. "
                                                        "This may be a genetic condition.",
                                episodes={"S04": [4], "S06": [10]})
        self.rougarou.clues = [MonstersClues.enormous_appetite, MonstersClues.body_metamorphosis,
                               MonstersClues.high_strength, MonstersClues.bloodshot_eyes, MonstersClues.wormy_skin]
        self.rougarou.kill_methods = [MonstersKillMethods.burn_it]

        self.samhain = Monster("Samhain", description="A demon that is the origin of Halloween. Celts believed, that "
                                                      "the 31st of October is the day, when the veil is the thinnest "
                                                      "between the living and dead. And this is also Samhain's night. "
                                                      "Masks were put on to hide from him, sweets left on doorsteps to "
                                                      "appease him and faces carved into pumpkins to worship him.",
                               episodes={"S04": [7]})
        self.samhain.clues = [MonstersClues.travels_as_black_fog, MonstersClues.white_eyes, MonstersClues.yellow_blast,
                              MonstersClues.can_bring_back_dead_people, MonstersClues.can_summon_ghosts]
        self.samhain.disable_methods = [MonstersDisableMethods.extrusion_by_people_with_abilities]

        self.fallen_angel = Monster("Fallen angel", description="An angel, that disobeyed the orders "
                                                                "and fell to Earth.", episodes={"S04": [9, 10]})
        self.fallen_angel.clues = [MonstersClues.people_hear_voices, MonstersClues.can_see_real_appearance_of_entities,
                                   MonstersClues.telekinesis, MonstersClues.people_acting_weirdly,
                                   MonstersClues.can_hear_angel_radio, MonstersClues.can_hear_demon_radio,
                                   MonstersClues.falling_meteor]

        self.demon_alastair = Monster("Demon Alastair", description="A very powerful demon. Tortures souls in Hell.",
                                      episodes={"S04": [9, 10, 15, 16]})
        self.demon_alastair.clues = [MonstersClues.white_eyes, MonstersClues.demon_killing_knife_is_ineffective,
                                     MonstersClues.immune_to_extrusion_by_people_with_abilities,
                                     MonstersClues.immune_to_exorcism_of_an_angel]
        self.demon_alastair.disable_methods = [MonstersDisableMethods.demon_killing_knife,
                                               MonstersDisableMethods.reconnection_of_angel_with_its_grace,
                                               MonstersDisableMethods.enochian_devils_trap,
                                               MonstersDisableMethods.holy_water,
                                               MonstersDisableMethods.salt_or_salted_bullets]
        self.demon_alastair.kill_methods = [MonstersKillMethods.will_of_a_person_with_abilities]

        self.siren = Monster("Siren", description="Beautiful creatures, that prey on men, "
                                                  "entice them with their siren song. For men, they are perfect and "
                                                  "they want to do anything for them. "
                                                  "Sirens lived on islands in the past. Has a venom in it's mouth. "
                                                  "Can be killed with it's own venom or the blood of the victim, "
                                                  "that is under the spell.",
                             episodes={"S04": [14]})
        self.siren.clues = [MonstersClues.people_dead_weirdly, MonstersClues.people_acting_weirdly,
                            MonstersClues.high_oxytocin_levels, MonstersClues.can_read_peoples_minds,
                            MonstersClues.real_appearance_can_be_seen_in_a_reflection_or_camera]
        self.siren.kill_methods = [MonstersKillMethods.its_own_venom]

        self.angel_zachariah = Monster("Angel Zachariah", description="High Tier Angel. Died in S05E18.",
                                       episodes={"S04": [17, 18, 22], "S05": [1, 4, 16, 18]})
        self.angel_zachariah.clues = [MonstersClues.can_put_people_into_alternate_timelines, MonstersClues.telekinesis,
                                      MonstersClues.can_erase_and_bring_back_memories, MonstersClues.can_vanish,
                                      MonstersClues.can_give_people_diseases, MonstersClues.can_repair_human_body,
                                      MonstersClues.can_appear_out_of_thin_air]
        self.angel_zachariah.disable_methods = [MonstersDisableMethods.symbol_made_with_blood_against_angels]
        self.angel_zachariah.kill_methods = [MonstersKillMethods.angel_blade]

        self.prophet = Monster("Prophet of the Lord", description="A person that is gifted with the knowledge "
                                                                  "of the future.",
                               episodes={"S04": [18, 22], "S05": [1, 9, 22]})
        self.prophet.clues = [MonstersClues.can_see_future, MonstersClues.protected_by_an_archangel,
                              MonstersClues.visions]

        self.archangel = Monster("Archangel", description="They are heaven's most terrifying weapon. "
                                                          "They are fierce and absolute.", episodes={"S04": [18, 22]})
        self.archangel.clues = [MonstersClues.small_earth_quake, MonstersClues.bright_light]

        self.ghoul = Monster("Ghoul", description="Ghoul is a creature, that feeds on dead people. "
                                                  "It can take the form of a person that it ate with all memories "
                                                  "and thoughts.",
                             episodes={"S04": [19], "S06": [10]})
        self.ghoul.clues = [MonstersClues.empty_graves, MonstersClues.body_torn_apart, MonstersClues.missing_body,
                            MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                            MonstersClues.holy_water_does_not_affect_it, MonstersClues.silver_does_not_affect_it]
        self.ghoul.kill_methods = [MonstersKillMethods.decapitation]

        self.archangel_lucyfer = Monster("Archangel - Lucyfer",
                                         description="Archangel, that disobeyed God when he requested to bow before "
                                                     "the men. To upset God he twisted one of the people into Lilith.",
                                         episodes={"S04": [22], "S05": [1, 3, 4, 10, 19, 22]})
        self.archangel_lucyfer.clues = [MonstersClues.weird_things_behavior, MonstersClues.true_voice_can_hurt_people,
                                        MonstersClues.bright_light, MonstersClues.weird_weather, MonstersClues.visions,
                                        MonstersClues.people_seeing_strange_things, MonstersClues.biblical_like_events,
                                        MonstersClues.people_hear_voices, MonstersClues.can_read_peoples_minds,
                                        MonstersClues.can_make_themselves_appear_as_they_like, MonstersClues.cold_spots,
                                        MonstersClues.can_give_hallucinations, MonstersClues.can_vanish,
                                        MonstersClues.can_appear_out_of_thin_air, MonstersClues.revelation_omens,
                                        MonstersClues.
                                            missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                                        MonstersClues.immune_to_colt_of_colt, MonstersClues.flashing_lights,
                                        MonstersClues.telekinesis, MonstersClues.temperature_fluctuations,

                                        MonstersClues.travels_as_white_fog,
                                        MonstersClues.people_burned_on_the_ceiling,
                                        MonstersClues.in_true_form_burns_eyes_of_people, MonstersClues.bible_burns_it]
        self.archangel_lucyfer.disable_methods = [MonstersDisableMethods.cage_of_lucyfer_in_hell,
                                                  MonstersDisableMethods.colt_of_colt_with_magic_bullets,

                                                  MonstersDisableMethods.symbol_made_with_blood_against_angels,
                                                  MonstersDisableMethods.holy_oil,
                                                  MonstersDisableMethods.angel_knuckle_duster]
        self.archangel_lucyfer.kill_methods = [MonstersKillMethods.archangel_blade,

                                               MonstersKillMethods.the_darkness]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # -------------------------------------------------- SEASON 5 --------------------------------------------------

        self.archangel_michael = Monster("Archangel - Michael", description="He commands the heavenly host. "
                                                                            "He was the one, who brought down Lucifer "
                                                                            "to Hell. He did it with his sword "
                                                                            "(Sword of Archangel Michael) - for now, "
                                                                            "only mentioned in S05E01. "
                                                                            "Can kill other angels with a touch.",
                                         episodes={"S05": [13, 18, 22]})
        self.archangel_michael.clues = [MonstersClues.can_put_a_person_to_sleep,
                                        MonstersClues.can_erase_and_bring_back_memories,
                                        MonstersClues.can_send_people_back_to_their_time,
                                        MonstersClues.can_kill_angels_with_a_touch,

                                        MonstersClues.travels_as_white_fog]
        self.archangel_michael.disable_methods = [MonstersDisableMethods.holy_oil,
                                                  MonstersDisableMethods.cage_of_lucyfer_in_hell,

                                                  MonstersDisableMethods.symbol_made_with_blood_against_angels]
        self.archangel_michael.kill_methods = [MonstersKillMethods.archangel_blade,

                                               MonstersKillMethods.the_darkness]

        self.god = Monster("THE God", description="The light, the beginning of everything. "
                                                  "Brother of the Darkness. A being with almost unlimited power. "
                                                  "Only mentioned for now. According to Death - he will die too "
                                                  "some day by Death's hand (S05E21). At the end of the S05E22 "
                                                  "Chuck disappears, hinting he is THE God.")
        self.god.clues = [MonstersClues.can_bring_back_dead_angels, MonstersClues.can_teleport_people,
                          MonstersClues.shining_of_magic_amulet, MonstersClues.can_bring_back_angelic_grace]
        self.god.kill_methods = [
                                 MonstersKillMethods.the_darkness]

        self.horseman_war = Monster("Horseman War", description="One of the four horseman. Can give people "
                                                                "hallucinations with his ring. "
                                                                "The ring is a source of his power.",
                                    episodes={"S05": [2]})
        self.horseman_war.clues = [MonstersClues.people_dead_weirdly, MonstersClues.people_acting_weirdly,
                                   MonstersClues.black_eyes, MonstersClues.salt_does_not_affect_it,
                                   MonstersClues.people_seeing_strange_things, MonstersClues.immune_to_exorcism,
                                   MonstersClues.can_take_form_of_other_people, MonstersClues.can_read_peoples_minds,
                                   MonstersClues.can_give_hallucinations]
        self.horseman_war.disable_methods = [MonstersDisableMethods.demon_killing_knife]

        self.archangel_raphael = Monster("Archangel Raphael", description="One of the Archangels of God.",
                                         episodes={"S05": [3], "S06": [3, 15, 20]})
        self.archangel_raphael.clues = [MonstersClues.bright_light, MonstersClues.invulnerable,
                                        MonstersClues.telekinesis, MonstersClues.can_vanish,
                                        MonstersClues.can_hurt_people_with_a_thought]
        self.archangel_raphael.disable_methods = [MonstersDisableMethods.holy_oil]
        self.archangel_raphael.kill_methods = [MonstersKillMethods.archangel_blade]

        self.pagan_god_leshii = Monster("Pagan god Leshi", description="Guardian of the forest in Balkan legends. "
                                                                       "He is a mischievous god and can take "
                                                                       "infinite forms. Can only be pleased with "
                                                                       "the blood of his worshippers. He would drain "
                                                                       "them, then stuff their stomachs with seeds.",
                                        episodes={"S05": [5]})
        self.pagan_god_leshii.clues = [MonstersClues.cold_spots, MonstersClues.weird_things_behavior,
                                       MonstersClues.weird_electronics_behavior, MonstersClues.people_dead_weirdly,
                                       MonstersClues.people_seeing_things_or_figures,
                                       MonstersClues.seeds_in_victims_stomachs, MonstersClues.can_read_peoples_minds,
                                       MonstersClues.can_make_themselves_appear_as_they_like]
        self.pagan_god_leshii.kill_methods = [MonstersKillMethods.chop_a_head_off_with_an_iron_axe]

        self.antichrist = Monster("Antichrist", description="Also known as Cambion or Katako. Half-demon, half-human, "
                                                            "but far more powerful than any of them. Can make real, "
                                                            "whatever comes to his mind.",
                                  episodes={"S05": [6]})
        self.antichrist.clues = [MonstersClues.claws, MonstersClues.animal_like_attack, MonstersClues.no_cold_spots,
                                 MonstersClues.people_dead_weirdly, MonstersClues.strange_different_things_happening,
                                 MonstersClues.no_sulfur, MonstersClues.can_exorcise_demons_with_a_thought,
                                 MonstersClues.telekinesis, MonstersClues.can_vanish]

        self.demon_crowley = Monster("Demon - Crowley", description="Crossroads demon in S05. "
                                                                    "King of Hell in S06. "
                                                                    "According to a crossroads demon, "
                                                                    "he's real name is Fergus Rodric MacLeod. "
                                                                    "He was born in Canisbay, Scotland 1661. "
                                                                    "Supposedly died in S06E10, but in S06E19 it is "
                                                                    "revealed he was working with Castiel.",
                                     episodes={"S05": [10, 20, 21], "S06": [4, 7, 8, 10, 19, 20]})
        self.demon_crowley.clues = [MonstersClues.can_vanish, MonstersClues.pact_sealed_with_a_kiss,
                                    MonstersClues.summoned_by_placing_box_in_the_crossroads, MonstersClues.telekinesis,
                                    MonstersClues.victims_got_better_at_something_up_to_ten_years_earlier,
                                    MonstersClues.can_appear_out_of_thin_air, MonstersClues.can_control_electronics,
                                    MonstersClues.weird_fire_spontaneous_combustion, MonstersClues.can_become_invisible,
                                    MonstersClues.can_bring_back_dead_people, MonstersClues.can_give_people_diseases,

                                    MonstersClues.black_blood, MonstersClues.burned_by_holy_water,
                                    MonstersClues.travels_as_red_fog, MonstersClues.red_eyes]
        self.demon_crowley.disable_methods = [MonstersDisableMethods.devils_trap]

        self.reaper_death = Monster("Reaper - Death", description="One of the Horseman, the pale rider. "
                                                                  "Angel of Death. Can be brought to the Earth "
                                                                  "at midnight through a place of awful carnage. "
                                                                  "Summoned in S05E10 and his actions seen in S05E15.",
                                    episodes={"S05": [21], "S06": [11]})
        self.reaper_death.clues = [MonstersClues.number_of_reapers_appearing, MonstersClues.can_bring_back_dead_people,
                                   MonstersClues.can_kill_people_with_a_thought, MonstersClues.people_dead_weirdly,
                                   MonstersClues.can_appear_out_of_thin_air, MonstersClues.can_put_a_soul_back_to_a_body,
                                   MonstersClues.can_go_to_lucifers_cage_and_back_with_ease]
        self.reaper_death.kill_methods = [

                                          MonstersKillMethods.scythe_of_death]

        self.wraith = Monster("Wraith", description="Creatures, that crack the head and feed on brain juice. "
                                                    "Can poison people and drive them crazy.", episodes={"S05": [11]})
        self.wraith.clues = [MonstersClues.people_dead_weirdly, MonstersClues.no_black_fog, MonstersClues.no_sulfur,
                             MonstersClues.no_cold_spots, MonstersClues.bite_marks_on_peoples_necks,
                             MonstersClues.victims_brain_devoid_of_water, MonstersClues.silver_burns_its_skin,
                             MonstersClues.can_take_form_of_other_people, MonstersClues.people_seeing_things_or_figures,
                             MonstersClues.people_hear_voices, MonstersClues.people_seeing_strange_things,
                             MonstersClues.real_appearance_can_be_seen_in_a_reflection_or_camera,
                             MonstersClues.high_strength, MonstersClues.people_loosing_their_minds,
                             MonstersClues.long_spike_from_the_arm]
        self.wraith.disable_methods = [MonstersDisableMethods.silver_or_silver_bullets]
        self.wraith.kill_methods = [MonstersKillMethods.silver_blade]

        self.cupid = Monster("Cupid", description="A lower tier of an angel - cherub, third class angel. "
                                                  "Binds people that are supposed to be with each other.",
                             episodes={"S05": [14]})
        self.cupid.clues = [MonstersClues.people_dead_weirdly, MonstersClues.people_acting_weirdly,
                            MonstersClues.no_emf, MonstersClues.no_sulfur, MonstersClues.marks_on_victims_hearts,
                            MonstersClues.invisible_entity, MonstersClues.can_vanish, MonstersClues.invulnerable,
                            MonstersClues.naked_man]
        self.cupid.kill_methods = [

                                   MonstersKillMethods.angel_blade]

        self.horseman_famine = Monster("Horseman Famine", description="Makes people starve for something they lack "
                                                                      "or they want (sex, attention, food, drugs, "
                                                                      "love, etc.). Can feed on souls of his victims "
                                                                      "or souls of demons. When he eats souls "
                                                                      "of demons, he can be killed by a person "
                                                                      "with abilities.",
                                       episodes={"S05": [14]})
        self.horseman_famine.clues = [MonstersClues.people_dead_weirdly, MonstersClues.people_acting_weirdly,
                                      MonstersClues.telekinesis, MonstersClues.can_exorcise_demons_with_a_thought,
                                      MonstersClues.victims_starve_for_something, MonstersClues.can_read_peoples_minds,
                                      MonstersClues.immune_to_extrusion_by_people_with_abilities]
        self.horseman_famine.kill_methods = [MonstersKillMethods.will_of_a_person_with_abilities]

        self.zombie = Monster("Zombie", description="A person brought back from the dead by Horseman Death. "
                                                    "At first a normal person, after a while turns into "
                                                    "human flesh-loving monster.",
                              episodes={"S05": [15]})
        self.zombie.clues = [MonstersClues.silver_does_not_affect_it, MonstersClues.holy_water_does_not_affect_it,
                             MonstersClues.salt_does_not_affect_it, MonstersClues.missing_body,
                             MonstersClues.feeds_on_human_flesh]
        self.zombie.kill_methods = [MonstersKillMethods.head_shot]

        self.angel_joshua = Monster("Angel Joshua", description="Angel, that guards the Heavens garden and the one, "
                                                                "that God talks to.", episodes={"S05": [16]})
        self.angel_joshua.clues = [MonstersClues.can_read_peoples_minds, MonstersClues.can_bring_back_dead_people]

        self.false_prophet = Monster("False Prophet", description="False Prophet rises, when Lucifer walks the Earth. "
                                                                  "Book of Revelations calls her "
                                                                  "'The Whore of Babylon'. Her goal is to drag as many "
                                                                  "souls to Hell as possible. Can only be killed "
                                                                  "by a true servant of heaven "
                                                                  "(like a devoted priest).",
                                     episodes={"S05": [17]})
        self.false_prophet.clues = [MonstersClues.can_read_peoples_minds, MonstersClues.can_control_demons,
                                    MonstersClues.can_take_form_of_other_people, MonstersClues.can_see_future,
                                    MonstersClues.visions, MonstersClues.telekinesis,
                                    MonstersClues.real_appearance_can_be_seen_in_a_reflection_or_camera]
        self.false_prophet.kill_methods = [MonstersKillMethods.stake_made_from_cypress_tree_in_babylon]

        self.god_mercury = Monster("God Mercury", description="Roman god of messengers. Died in S05E19.",
                                   episodes={"S05": [19]})
        self.god_mercury.clues = [MonstersClues.moves_fast, MonstersClues.people_dead_weirdly, MonstersClues.immortal,
                                  MonstersClues.can_appear_out_of_thin_air,
                                  MonstersClues.
                                      missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
        self.god_mercury.kill_methods = [MonstersKillMethods.will_of_an_archangel]

        self.ganesh = Monster("Ganesh", description="Hindu Elephant god of success and wisdom. Died in S05E19.",
                              episodes={"S05": [19]})
        self.ganesh.clues = [MonstersClues.can_appear_as_an_elephant, MonstersClues.people_dead_weirdly,
                             MonstersClues.immortal, MonstersClues.weird_things_behavior,
                             MonstersClues.people_seeing_strange_things,
                             MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
        self.ganesh.kill_methods = [MonstersKillMethods.will_of_an_archangel]

        self.odin = Monster("Odin", description="Norse god of wisdom, poetry and death. Died in S05E19.",
                            episodes={"S05": [19]})
        self.odin.clues = [MonstersClues.people_dead_weirdly, MonstersClues.immortal,
                           MonstersClues.weird_things_behavior,
                           MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
        self.odin.kill_methods = [MonstersKillMethods.will_of_an_archangel]

        self.kali = Monster("Kali", description="Hindu goddess of death, time and doomsday.", episodes={"S05": [19]})
        self.kali.clues = [MonstersClues.people_dead_weirdly, MonstersClues.immortal, MonstersClues.telekinesis,
                           MonstersClues.weird_things_behavior, MonstersClues.seen_as_fire,
                           MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]

        self.baron_samedi = Monster("Baron Samedi", description="One of the Iwa of Haitian Voodoo. He is the Iwa of "
                                                                "the dead. The master of magic. Died in S05E19.",
                                    episodes={"S05": [19]})
        self.baron_samedi.kill_methods = [MonstersKillMethods.will_of_an_archangel]

        self.baldur = Monster("Baldur", description="Norse god of good, beauty and wisdom. Died in S05E19.",
                              episodes={"S05": [19]})
        self.baldur.clues = [MonstersClues.people_dead_weirdly, MonstersClues.immortal,
                             MonstersClues.weird_things_behavior,
                             MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
        self.baldur.kill_methods = [MonstersKillMethods.stabbing_the_heart]

        self.zao_shen = Monster("Zao Shen", description="Chinese god of the kitchen. Died in S05E19.",
                                episodes={"S05": [19]})
        self.zao_shen.clues = [MonstersClues.people_dead_weirdly, MonstersClues.immortal,
                               MonstersClues.weird_things_behavior,
                               MonstersClues.
                                   missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
        self.zao_shen.kill_methods = [MonstersKillMethods.stake_made_from_unknown_wood]

        self.isis = Monster("Isis", description="Egyptian goddess of healing and magic. Died in S05E19.",
                            episodes={"S05": [19]})
        self.isis.clues = [MonstersClues.people_dead_weirdly, MonstersClues.immortal,
                           MonstersClues.weird_things_behavior,
                           MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area]
        self.isis.kill_methods = [MonstersKillMethods.will_of_an_archangel]

        self.horseman_pestilence = Monster("Horseman Pestilence", description="One of the horseman, "
                                                                              "that brings disease and pests.",
                                           episodes={"S05": [19, 21]})
        self.horseman_pestilence.clues = [MonstersClues.general_sickness, MonstersClues.increased_pest_activity,
                                          MonstersClues.weird_electronics_behavior]

        self.soulless_person = Monster("Soulless person", description="A person without a soul - only the 'meatsuit'.",
                                       episodes={"S05": [21], "S06": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]})
        self.soulless_person.clues = [MonstersClues.people_acting_weirdly, MonstersClues.lack_of_empathy,
                                      MonstersClues.sociopath_like_behavior, MonstersClues.does_not_sleep]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # -------------------------------------------------- SEASON 6 --------------------------------------------------

        self.alpha_shapeshifter = Monster("Alpha Shapeshifter", description="First of it's kind. Does not shed "
                                                                            "it's skin to change into other people. "
                                                                            "There is a connection between it "
                                                                            "and it's babies. Even an elephant "
                                                                            "tranquilizes does not affect it "
                                                                            "long enough. Killed in S06E10.",
                                          episodes={"S05": [2, 10]})
        self.alpha_shapeshifter.clues = [MonstersClues.people_dead_weirdly, MonstersClues.no_sulfur,
                                         MonstersClues.missing_babies, MonstersClues.moves_fast, MonstersClues.no_emf,
                                         MonstersClues.high_strength, MonstersClues.silver_does_not_affect_it,
                                         MonstersClues.can_make_themselves_appear_as_they_like,
                                         MonstersClues.missing_or_dead_people_regularly_in_the_same_area]
        self.alpha_shapeshifter.disable_methods = [MonstersDisableMethods.iridium_or_iridium_blade]
        self.alpha_shapeshifter.kill_methods = [MonstersKillMethods.iridium_blade_decapitation]

        self.angel_balthazar = Monster("Angel Balthazar", description="Angel, that stole a lot of angel weapons "
                                                                      "after the Apocalypse was canceled.",
                                       episodes={"S06": [3, 11, 15, 17]})
        self.angel_balthazar.clues = [MonstersClues.can_vanish, MonstersClues.can_appear_out_of_thin_air,
                                      MonstersClues.marks_on_victims_souls, MonstersClues.can_change_the_past]
        self.angel_balthazar.disable_methods = [MonstersDisableMethods.holy_oil]

        self.lamia = Monster("Lamia", description="Juices hearts, chugs the blood. "
                                                  "These monsters usually appear in Greece.", episodes={"S06": [4]})
        self.lamia.clues = [MonstersClues.no_emf, MonstersClues.missing_heart, MonstersClues.claws,
                            MonstersClues.no_sulfur, MonstersClues.no_hex_bags]
        self.lamia.kill_methods = [MonstersKillMethods.silver_knife_blessed_by_a_priest,
                                   MonstersKillMethods.mix_of_salt_and_rosemary_thrown_it_and_burned]

        self.okami = Monster("Okami", description="Monster with fangs like a vampire, but larger and not retractable. "
                                                  "Usually appear in Japan.",
                             episodes={"S06": [4]})
        self.okami.clues = [MonstersClues.people_dead_weirdly, MonstersClues.feeds_on_women_during_their_sleep,
                            MonstersClues.needle_like_teeth, MonstersClues.high_strength]
        self.okami.kill_methods = [MonstersKillMethods.stab_it_seven_times_with_bamboo_dagger_blessed_by_shinto_priest,
                                   MonstersKillMethods.blend_it]

        self.vampire_alpha = Monster("Vampire Alpha", description="First Vampire. All Vampires are descendants "
                                                                  "of the Alpha. Has control over other vampires.",
                                     episodes={"S06": [5, 7]})
        self.vampire_alpha.clues = [MonstersClues.can_give_hallucinations, MonstersClues.mind_control,
                                    MonstersClues.can_put_a_person_to_sleep, MonstersClues.invulnerable,
                                    MonstersClues.great_sense_of_smell, MonstersClues.moves_fast,
                                    MonstersClues.can_appear_out_of_thin_air]
        self.vampire_alpha.kill_methods = [

                                           MonstersKillMethods.colt_of_colt_with_magic_bullets]

        self.veritas = Monster("Veritas", description="Goddess of Truth. Can be summoned with a cat skull, "
                                                      "grains of paradise seed and devil's shoestring. "
                                                      "Loves cats, dogs hate her. Can make people tell the truth. "
                                                      "Died in S06E06.",
                               episodes={"S06": [6]})
        self.veritas.clues = [MonstersClues.missing_body, MonstersClues.suicides, MonstersClues.no_emf,
                              MonstersClues.no_sulfur, MonstersClues.no_hex_bags, MonstersClues.blue_eyes,
                              MonstersClues.telekinesis, MonstersClues.high_strength,
                              MonstersClues.people_acting_weirdly]
        self.veritas.kill_methods = [MonstersKillMethods.silver_knife_dipped_in_dogs_blood]

        self.fairy = Monster("Fairy", description="Little people with or without wings. Can be mistaken with UFO "
                                                  "encounters. They like in another reality - Avalon. Only people, "
                                                  "that were in their land and came back can see them. Fairies can be "
                                                  "summoned and put back into their land by a spell. "
                                                  "They abduct only first sons. There are different kings of fairies. "
                                                  "Dark fairies burn, when touched with silver. "
                                                  "No matter how powerful, the fairy must stop and count each grain, "
                                                  "when salt or sugar is spilled in front of them. "
                                                  "If you want to win a fairy's favor, leave a bowl of fresh cream.",
                             episodes={"S06": [9]})
        self.fairy.clues = [MonstersClues.strange_different_things_happening, MonstersClues.bright_light,
                            MonstersClues.people_seeing_strange_things, MonstersClues.flashing_lights,
                            MonstersClues.missing_or_dead_people_regularly_in_the_same_area, MonstersClues.has_wings,
                            MonstersClues.small_people, MonstersClues.high_strength, MonstersClues.invisible_entity,
                            MonstersClues.can_vanish, MonstersClues.can_appear_out_of_thin_air,
                            MonstersClues.can_sense_peoples_souls]
        self.fairy.disable_method = [MonstersDisableMethods.iron_or_iron_bullets, MonstersClues.silver_burns_its_skin,
                                     MonstersDisableMethods.spilled_sugar_or_salt]
        self.fairy.kill_methods = [MonstersKillMethods.microwave_it, MonstersKillMethods.silver_blade]

        self.dragon = Monster("Dragon", description="Flying creatures form the legends. They like virgins and gold. "
                                                    "Live in caves or underground, dark, wet places. They disappeared "
                                                    "almost 700 years ago (from 2010).", episodes={"S06": [12]})
        self.dragon.clues = [MonstersClues.people_seeing_strange_things, MonstersClues.people_dead_weirdly,
                             MonstersClues.missing_attacked_virgin_women, MonstersClues.has_wings, MonstersClues.claws,
                             MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                             MonstersClues.likes_gold, MonstersClues.weird_fire_spontaneous_combustion,
                             MonstersClues.can_create_fire_large_temperatures, MonstersClues.high_strength]
        self.dragon.disable_methods = [MonstersDisableMethods.blade_forged_with_dragons_blood]
        self.dragon.kill_methods = [MonstersKillMethods.blade_forged_with_dragons_blood]

        self.mother_of_all = Monster("Mother of all", description="Mother of all monsters. Was in a Purgatory, "
                                                                  "until released in S06E12. Calls herself Eve. "
                                                                  "She was walking the face of the Earth "
                                                                  "10 000 years ago. Every monster can be traced "
                                                                  "back to her. Can talk to every monster, "
                                                                  "that is alive. Killed in S06E19.",
                                     episodes={"S06": [12, 16]})
        self.mother_of_all.clues = [MonstersClues.telekinesis, MonstersClues.weird_electronics_behavior,
                                    MonstersClues.real_appearance_can_be_seen_in_a_reflection_or_camera,
                                    MonstersClues.mind_control, MonstersClues.people_dead_weirdly,
                                    MonstersClues.people_acting_weirdly, MonstersClues.people_hear_voices,
                                    MonstersClues.can_turn_people_into_monsters, MonstersClues.can_appear_out_of_thin_air,
                                    MonstersClues.can_make_themselves_appear_as_they_like, MonstersClues.can_vanish]
        self.mother_of_all.disable_methods = [MonstersDisableMethods.ashes_of_a_phoenix]
        self.mother_of_all.kill_methods = [MonstersKillMethods.ashes_of_a_phoenix]

        self.arachne = Monster("Arachne", description="No one has seen it outside of Crete for 2000 years. "
                                                      "When in mating time it has a type, that it likes.",
                               episodes={"S06": [13]})
        self.arachne.clues = [MonstersClues.missing_or_dead_people_regularly_in_the_same_area,
                              MonstersClues.left_cobweb, MonstersClues.high_strength, MonstersClues.multiple_pupils,
                              MonstersClues.fire_does_not_affect_it, MonstersClues.head_shot_does_not_affect_it]
        self.arachne.kill_methods = [MonstersKillMethods.decapitation]

        self.possessing_worm = Monster("Possessing worm", description="Worm, that can possess a person and control "
                                                                      "their mind. It is spread by the Mother of All.",
                                       episodes={"S06": [16]})
        self.possessing_worm.clues = [MonstersClues.amnesia_blackout, MonstersClues.people_acting_weirdly,
                                      MonstersClues.black_blood, MonstersClues.mind_control, MonstersClues.worm,
                                      MonstersClues.people_dead_weirdly, MonstersClues.invulnerable,
                                      MonstersClues.high_strength]
        self.possessing_worm.disable_methods = [MonstersDisableMethods.electricity]
        self.possessing_worm.kill_methods = [MonstersKillMethods.electricity]

        self.fate = Monster("Fate", description="Sisters Fates (Atropos, two other unknown) from Greek Mythology. "
                                                "They are responsible for the way you die.", episodes={"S06": [17]})
        self.fate.clues = [MonstersClues.weird_things_behavior, MonstersClues.people_dead_weirdly, MonstersClues.no_emf,
                           MonstersClues.bad_luck, MonstersClues.left_gold_thread, MonstersClues.can_stop_time]

        self.phoenix = Monster("Phoenix", description="A creature, that can burn people with it's touch. "
                                                      "Dies in a fire.", episodes={"S06": [18]})
        self.phoenix.clues = [MonstersClues.weird_fire_spontaneous_combustion, MonstersClues.empty_graves,
                              MonstersClues.burned_people, MonstersClues.invulnerable]
        self.phoenix.disable_methods = [MonstersDisableMethods.iron_or_iron_bullets]
        self.phoenix.kill_methods = [MonstersKillMethods.colt_of_colt_with_magic_bullets]

        self.jefferson_starship = Monster("Jefferson Starship", description="A monster, that is a combination of "
                                                                            "a Vampire and a Wraith created by Eve. "
                                                                            "Dean named it in S06E19 and all of them "
                                                                            "died in the same episode.",
                                          episodes={"S06": [19]})
        self.jefferson_starship.clues = [MonstersClues.needle_like_teeth, MonstersClues.moving_in_groups_usually,
                                         MonstersClues.bright_eyes, MonstersClues.long_spike_from_the_arm,
                                         MonstersClues.feeds_on_blood]
        self.jefferson_starship.kill_methods = [MonstersKillMethods.decapitation, MonstersKillMethods.will_of_an_angel]

        self.unknown = Monster("Unknown", description="", episodes={"S06": [20]})
        self.unknown.clues = []


        # -------------------------------------------------- SEASON 7 --------------------------------------------------



        # -------------------------------------------------- SEASON 8 --------------------------------------------------



        # -------------------------------------------------- SEASON 9 --------------------------------------------------



        # SEASON XX - unknown when:

        self.thule = Monster("Thule", description="Nazi members. Used blood magic to make themselves almost undead.")
        self.thule.clues = [MonstersClues.weird_fire_spontaneous_combustion]
        self.thule.kill_methods = [MonstersKillMethods.burn_it, MonstersClues.people_dead_weirdly]

        self.nephilim = Monster("Nephilim", description="Child of human and angel/archangel. "
                                                        "Human with an angelic grace.")
        self.nephilim.clues = [MonstersClues.weird_weather, MonstersClues.biblical_like_events]

        # -------------------------------------------------- SEASON 10 -------------------------------------------------

        self.angel_watcher = Monster("Angel Watcher - Grigori")
        self.angel_watcher.clues = [MonstersClues.triangle_wound_with_burns]
        self.angel_watcher.kill_methods = [MonstersKillMethods.angel_sword]

        self.knight_of_hell = Monster("Knight of hell (Abaddon)")
        self.knight_of_hell.kill_methods = [MonstersKillMethods.first_blade]

        self.witch_from_ozz = Monster("Witch from Ozz")
        self.witch_from_ozz.clues = [MonstersClues.travels_as_black_green_fog]
        self.witch_from_ozz.kill_methods = [MonstersKillMethods.magic_red_high_heels]

        # -------------------------------------------------- SEASON 11 -------------------------------------------------

        self.darkness = Monster("Darkness", description="Sister of God. He was the light, she is the dark. "
                                                        "A being with almost unlimited power.")
        self.darkness.clues = [MonstersClues.people_dead_weirdly, MonstersClues.leaves_soulless_people_behind,
                               MonstersClues.leaves_zombie_like_people_with_black_veins_around_neck,
                               MonstersClues.telekinesis, MonstersClues.weird_weather,
                               MonstersClues.enormous_black_fog]
        self.darkness.disableMethod = [MonstersDisableMethods.all_of_angels_single_blow]

        self.whisper = Monster("Whisper")
        self.whisper.clues = [MonstersClues.body_torn_apart, MonstersClues.no_blood_in_the_body,
                              MonstersClues.animal_like_attack, MonstersClues.feeding_during_solar_eclipse]
        self.whisper.kill_methods = [MonstersKillMethods.decapitation, MonstersKillMethods.silver_bullet_into_the_heart]

        self.nachzehrer = Monster("Nachzehrer (Ghul & Vampire) aka Ghulpire")
        self.nachzehrer.clues = [MonstersClues.bright_eyes, MonstersClues.weird_animal_behavior,
                                 MonstersClues.skin_left_behind, MonstersClues.ozone_smell]
        self.nachzehrer.disable_methods = [MonstersDisableMethods.silver_or_silver_bullets,
                                           MonstersDisableMethods.decapitation]
        self.nachzehrer.kill_methods = [MonstersKillMethods.copper_coin_placed_under_the_tongue]

        self.zanna = Monster("Zanna", description="Invisible entities that help children when they are young. "
                                                  "When a child no longer needs leeding Zanna leaves a child.")
        self.zanna.clues = [MonstersClues.kids_imaginary_friend]
        self.zanna.kill_methods = [MonstersKillMethods.zanna_killing_knife]

        self.banshee = Monster("Banshee")
        self.banshee.clues = [MonstersClues.emf, MonstersClues.flashing_lights, MonstersClues.feeding_at_night,
                              MonstersClues.ghost_like_creature, MonstersClues.victims_hear_screams,
                              MonstersClues.feeding_on_vulnerable]
        self.banshee.disable_methods = [MonstersDisableMethods.celtic_imprisonment_spell]
        self.banshee.kill_methods = [MonstersKillMethods.gold_blade]

        self.quareen = Monster("Quareen", description="Slave creature with bodily form. "
                                                      "When curse is layed on a person, "
                                                      "Quareen seduces this person as a form of deepest, "
                                                      "darkest desire and kills one. "
                                                      "The person that possesses a Quareens heart, commands it.")
        self.quareen.clues = [MonstersClues.people_dead_weirdly, MonstersClues.missing_heart]
        self.quareen.kill_methods = [MonstersKillMethods.stabbing_the_heart]

        self.soul_eater = Monster("Soul Eater", description="Ghost-like creature existing between worlds. "
                                                            "Soul eater moves into a house and makes a nest, "
                                                            "which exists outside time and space. "
                                                            "The nest feels like a house that a soul eater is in.")
        self.soul_eater.clues = [MonstersClues.emf, MonstersClues.weird_noises, MonstersClues.flashing_lights,
                                 MonstersClues.ghost_like_creature, MonstersClues.cold_spots,
                                 MonstersClues.feeling_of_something_bad,
                                 MonstersClues.victims_in_coma_fading_and_dying]
        self.soul_eater.disable_methods = [MonstersDisableMethods.celtic_sigil_to_trap_monsters]
        self.soul_eater.kill_methods = [MonstersKillMethods.celtic_sigil]

        self.bissan = Monster("Bissan", description="Spirits of the Cicada. "
                                                    "Every 27 years they come out and have orgies. "
                                                    "They can't multiply on their own due to a lack of junk, "
                                                    "so they 'posses' people to do it.")
        self.bissan.clues = [MonstersClues.junkless_creature, MonstersClues.mutant_pale_creature,
                             MonstersClues.green_eyes, MonstersClues.weird_noises,
                             MonstersClues.missing_or_dead_people_regularly_in_the_same_area,
                             MonstersClues.needle_like_teeth]
        self.bissan.kill_methods = [MonstersKillMethods.decapitation]

        # -------------------------------------------------- SEASON 12 -------------------------------------------------

        self.myling = Monster("Myling", description="Scandinavian children ghost. "
                                                    "They try to bring adults and kill them.")
        self.myling.clues = [MonstersClues.victims_hear_children_cry, MonstersClues.people_dead_weirdly]
        self.myling.kill_methods = [MonstersKillMethods.burn_salted_corpse,
                                    MonstersKillMethods.destroy_the_object_that_the_ghost_is_bound_to]

        self.satyr = Monster("Satyr", description="Half man half goat creature from greek mythology. "
                                                  "They lead people to the woods to grand orgies. "
                                                  "When orgy is over satyr feeds on the victim.")
        self.satyr.clues = [MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                            MonstersClues.goat_man]

        self.moloch = Monster("Moloch", description="God of sacrifice.")
        self.moloch.clues = [MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                             MonstersClues.goat_man]
        self.moloch.kill_methods = [MonstersKillMethods.colt_of_colt_with_magic_bullets]

        # -------------------------------------------------- SEASON 13 -------------------------------------------------

        self.empty = Monster("Empty", description="The place (and a cosmic being) that angels "
                                                  "and demons go to when they die. "
                                                  "THE God has no power there.")

        # -------------------------------------------------- SEASON 14 -------------------------------------------------



        # -------------------------------------------------- SEASON 15 -------------------------------------------------




        self.monsters = [monster for monster in self.__dict__.values() if isinstance(monster, Monster)]

    def print_all_sorted_clues(self):
        print(Colors.BOLD + Colors.YELLOW + "\nBase of all clues:" + Colors.ENDC)
        sorted_clues = sorted(self.clues)
        for clue_number, clue in enumerate(sorted_clues, 1):
            print(" »%5d  " % clue_number + clue)

    def print_all_clues(self):
        print(Colors.BOLD + Colors.YELLOW + "\nBase of all clues:" + Colors.ENDC)
        for clue_number, clue in enumerate(self.clues, 1):
            print(" »%5d  " % clue_number + clue)

    def choose_clues(self) -> List[str]:
        clues = input(Colors.UNDERLINE + "\nChoose clues:" + Colors.ENDC + " ")
        clues = re.sub('[a-zA-Z,&^%$#@?|/:;"_=]', ' ', clues)
        chosen_clues = [self.clues[int(clue) - 1] for clue in clues.split()
                        if (clue.isdigit() and int(clue) <= len(self.clues))]
        return chosen_clues

    def print_all_matches(self, selected_clues: List[str]):
        monster_clues_dict = {}
        for monster_number, monster in enumerate(self.monsters):
            if monster.clues is not None \
                    and (clues_intersection := len(set(monster.clues).intersection(set(selected_clues)))):
                monster_clues_dict[monster_number] = clues_intersection
        sorted_monster_clues_dict = {m: c for m, c in sorted(monster_clues_dict.items(), key=lambda item: item[1],
                                                             reverse=True)}
        print(f"\n{len(sorted_monster_clues_dict)} MATCHED MONSTERS FOUND: \n")
        for monster_number, number_of_matching_clues in sorted_monster_clues_dict.items():
            print(Colors.BOLD + Colors.BLUE + f"{number_of_matching_clues}/{len(selected_clues)} Matches:"
                  + Colors.ENDC, end=" ")
            self.monsters[monster_number].print_all()
            print("")

    def print_all_monsters(self):
        for monster in self.monsters:
            monster.print_all()

    def print_monsters_names(self):
        sorted_monsters = sorted([monster.name for monster in self.monsters])
        print(Colors.RED + Colors.BOLD + "All monsters:" + Colors.ENDC)
        for monster in sorted_monsters:
            print(" »  " + monster)
