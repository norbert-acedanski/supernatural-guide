import re
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
        self.chosen_clues = []

        # SEASON 1:

        self.prince_of_hell = Monster("Prince of Hell (Azazel, Ramiel, Asmodeus, Dagon)",
                                      description="The oldest of old demons. One generation after Lilith. "
                                                  "They were turned by Lucyfer himself before the Atlantis drown. "
                                                  "They were trained to be demonic generals in the war against heaven.",
                                      episodes={"S01": [1, 21, 22], "S02": [1]})
        self.prince_of_hell.clues = [MonstersClues.people_burned_on_the_ceiling, MonstersClues.telekinesis,
                                     MonstersClues.weird_things_behavior, MonstersClues.yellow_eyes,
                                     MonstersClues.children_of_victims_that_died_on_the_ceiling_have_abilities,
                                     MonstersClues.mothers_burned_when_children_are_6_months_old,
                                     MonstersClues.weird_weather, MonstersClues.cattle_deaths,
                                     MonstersClues.temperature_fluctuations, MonstersClues.electrical_storms,
                                     MonstersClues.holy_water_does_not_affect_it, MonstersClues.travels_as_black_fog,
                                     MonstersClues.can_posses_a_reaper, MonstersClues.one_can_make_a_deal_with_it]
        self.prince_of_hell.kill_methods = [
                                            MonstersKillMethods.colt_of_colt_with_magic_bullets,
                                            MonstersKillMethods.lance_of_archangel_michael,
                                            MonstersKillMethods.will_of_a_nephilim]

        self.vengeful_spirit = Monster("Vengeful Spirit or Ghost (Bloody Mary, Hook Man)",
                                       description="Appears, when somebody died tragically, committed suicide "
                                                   "or was killed. Usually bound to a place or to things.",
                                       episodes={"S01": [1, 3, 5, 7, 9, 10, 13, 19]})
        self.vengeful_spirit.clues = [MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                                      MonstersClues.people_dead_weirdly, MonstersClues.ghost_like_creature,
                                      MonstersClues.weird_electronics_behavior, MonstersClues.weird_things_behavior,
                                      MonstersClues.local_legend_about_somebody_killed_or_died,
                                      MonstersClues.telekinesis, MonstersClues.invisible_entity,
                                      MonstersClues.missing_body, MonstersClues.high_strength,
                                      MonstersClues.can_control_water, MonstersClues.people_seeing_things_or_figures,
                                      MonstersClues.summoned_by_saying_bloody_marry_in_front_of_the_mirror,
                                      MonstersClues.objects_seen_in_night_vision, MonstersClues.weird_noises,
                                      MonstersClues.ozone_smell, MonstersClues.seen_as_fire,
                                      MonstersClues.people_acting_weirdly, MonstersClues.victims_hear_voices,
                                      MonstersClues.seen_as_black_truck, MonstersClues.emf,

                                      MonstersClues.cold_spots]
        self.vengeful_spirit.disable_methods = [MonstersKillMethods.bring_the_spirit_to_its_crime_place,
                                                MonstersKillMethods.bring_the_spirit_what_it_wants,
                                                MonstersDisableMethods.iron_or_iron_bullets,
                                                MonstersDisableMethods.salt_or_salted_bullets]
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

        self.skinwalker = Monster("Skinwalker", description="Not seen. Only mentioned in S01E02")
        self.skinwalker.clues = [MonstersClues.claws, MonstersClues.moves_fast]

        self.black_dog = Monster("Black Dog", description="Not seen. Only mentioned in S01E02")
        self.black_dog.clues = [MonstersClues.claws, MonstersClues.moves_fast]

        self.water_wraith = Monster("Water Wraith", description="Not seen. Only mentioned in S01E03")
        self.water_wraith.clues = [MonstersClues.can_control_water]

        self.demon = Monster("Demon", description="In every religion there is information about demonic possessions. "
                                                  "Demons are man that were stuck in hell for a long time.",
                             episodes={"S01": [4, 21, 22], "S02": [1]})
        self.demon.clues = [MonstersClues.black_eyes, MonstersClues.travels_as_black_fog, MonstersClues.emf,
                            MonstersClues.weird_electronics_behavior, MonstersClues.high_strength, MonstersClues.sulfur,
                            MonstersClues.burned_by_holy_water, MonstersClues.reacts_to_gods_name_in_latin,
                            MonstersClues.people_dead_weirdly, MonstersClues.telekinesis,

                            MonstersClues.black_blood]
        self.demon.kill_methods = [MonstersKillMethods.exorcism,

                                   MonstersKillMethods.angel_blade,
                                   MonstersKillMethods.demon_killing_knife, MonstersKillMethods.will_of_an_archangel,
                                   MonstersKillMethods.colt_of_colt_with_magic_bullets,
                                   MonstersKillMethods.lance_of_archangel_michael]
        self.demon.disable_methods = [MonstersDisableMethods.devils_trap]

        self.shapeshifter = Monster("Shapeshifter", description="These creatures can transform themselves into "
                                                                "other man or animals.",
                                    episodes={"S01": [6]})
        self.shapeshifter.clues = [MonstersClues.can_take_form_of_other_people, MonstersClues.skin_left_behind,
                                   MonstersClues.being_at_two_places_at_once, MonstersClues.bright_eyes,
                                   MonstersClues.weird_animal_behavior, MonstersClues.can_copy_memories_of_other_people]
        self.shapeshifter.kill_methods = [MonstersKillMethods.silver_bullet_into_the_heart]

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
                                                       "in order to maintain prosperity. Sacrifice takes place in April",
                                           episodes={"S01": [11]})
        self.norwegian_god_vanir.clues = [MonstersClues.missing_or_dead_people_regularly_in_the_same_area,
                                          MonstersClues.emf, MonstersClues.seen_as_a_scarecrow,
                                          MonstersClues.weird_noises]
        self.norwegian_god_vanir.disable_methods = [MonstersDisableMethods.bring_it_what_it_wants]
        self.norwegian_god_vanir.kill_methods = [MonstersKillMethods.burn_the_sacred_tree]

        self.rawhead = Monster("Rawhead", episodes={"S01": [12]})
        self.rawhead.kill_methods = [MonstersKillMethods.apply_large_voltage]

        self.reaper = Monster("Reaper", description="Can give and take life. Can also transfer illnesses of people.",
                              episodes={"S01": [12], "S02": [1]})
        self.reaper.clues = [MonstersClues.people_dead_weirdly, MonstersClues.people_cured_miraculously,
                             MonstersClues.weird_things_behavior, MonstersClues.people_seeing_things_or_figures,
                             MonstersClues.seen_as_a_person_in_a_suit, MonstersClues.ghost_like_creature,
                             MonstersClues.visible_by_other_ghosts_and_people_close_to_death_only,
                             MonstersClues.can_make_themselves_appear_as_they_like]

        self.people_with_abilities = Monster("People with abilities", description="People, that were infants, "
                                                                                  "when prince of hell killed "
                                                                                  "their mother on the ceiling",
                                             episodes={"S01": [14]})
        self.people_with_abilities.clues = [MonstersClues.people_dead_weirdly, MonstersClues.weird_things_behavior,
                                            MonstersClues.telekinesis,
                                            MonstersClues.their_mother_was_burned_on_the_ceiling_when_they_were_infants]
        self.people_with_abilities.kill_methods = [MonstersKillMethods.like_any_human]

        self.spring_heeled_jacks = Monster("Sprint Heeled Jacks", description="Not seen. Only mentioned in S01E15")
        self.spring_heeled_jacks.clues = [MonstersClues.people_kidnapped_weirdly]

        self.phantom_gassers = Monster("Phantom gassers", description="Not seen. Only mentioned in S01E15")
        self.phantom_gassers.clues = [MonstersClues.people_kidnapped_weirdly]

        self.werewolf = Monster("Werewolf", description="Not seen. Only mentioned in S01E16")
        self.werewolf.clues = [MonstersClues.body_torn_apart, MonstersClues.animal_like_attack,
                               MonstersClues.missing_heart]
        self.werewolf.kill_methods = [MonstersKillMethods.silver_bullet_into_the_heart]
        self.werewolf.cure_methods = \
            [MonstersCureMethods.plasma_therapy_with_the_blood_of_the_werewolf_that_bit_the_victim]

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
                                                      "One can become a vampire, when drinking vampire blood.",
                               episodes={"S01": [20]})
        self.vampire.clues = [MonstersClues.ripped_throat, MonstersClues.no_blood_in_the_body,
                              MonstersClues.needle_like_teeth, MonstersClues.moving_in_groups_usually,
                              MonstersClues.invulnerable, MonstersClues.high_strength, MonstersClues.bright_eyes,
                              MonstersClues.great_sense_of_smell, MonstersClues.white_skin]
        self.vampire.kill_methods = [MonstersKillMethods.decapitation, MonstersKillMethods.angel_blade,
                                     MonstersKillMethods.colt_of_colt_with_magic_bullets]
        self.vampire.disable_methods = [MonstersDisableMethods.dead_mans_blood]
        self.vampire.cure_methods = [MonstersCureMethods.cocktail_made_of_blood_of_the_vampire_that_bit_the_victim]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 2:

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

        # SEASON 3:



        # SEASON 4:



        # SEASON 5:



        # SEASON 6:



        # SEASON 7:



        # SEASON 8:



        # SEASON 9:



        # SEASON XX - unknown when:

        self.demon_crowley = Monster("Demon - King of Hell - Crowley")
        self.demon_crowley.clues = [MonstersClues.black_blood, MonstersClues.burned_by_holy_water,
                                    MonstersClues.travels_as_red_fog, MonstersClues.red_eyes]

        self.angel = Monster("Angel")
        self.angel.clues = [MonstersClues.burned_eyes_of_victims, MonstersClues.triangle_wound,
                            MonstersClues.travels_as_white_fog]
        self.angel.disable_methods = [MonstersDisableMethods.symbol_made_with_blood]
        self.angel.kill_methods = [MonstersKillMethods.angel_blade, MonstersKillMethods.holy_oil,
                                   MonstersKillMethods.will_of_an_archangel, MonstersKillMethods.will_of_prince_of_hell,
                                   MonstersKillMethods.lance_of_archangel_michael]

        self.cupid = Monster("Cupid")
        self.cupid.kill_methods = [MonstersKillMethods.angel_blade]

        self.archangel_lucyfer = Monster("Archangel - Lucyfer")
        self.archangel_lucyfer.clues = [MonstersClues.visions, MonstersClues.weird_things_behavior,
                                        MonstersClues.flashing_lights, MonstersClues.travels_as_white_fog,
                                        MonstersClues.people_burned_on_the_ceiling, MonstersClues.telekinesis,
                                        MonstersClues.burned_eyes_of_victims, MonstersClues.bible_burns_it]
        self.archangel_lucyfer.disable_methods = [MonstersDisableMethods.cage_of_lucyfer_in_hell,
                                                  MonstersDisableMethods.symbol_made_with_blood,
                                                  MonstersDisableMethods.holy_oil,
                                                  MonstersDisableMethods.angel_knuckle_duster]
        self.archangel_lucyfer.kill_methods = [MonstersKillMethods.the_darkness]

        self.archangel_michael = Monster("Archangel - Michael")
        self.archangel_michael.clues = [MonstersClues.travels_as_white_fog]
        self.archangel_michael.disable_methods = [MonstersDisableMethods.cage_of_lucyfer_in_hell,
                                                  MonstersDisableMethods.symbol_made_with_blood]
        self.archangel_michael.kill_methods = [MonstersKillMethods.the_darkness]

        self.god = Monster("THE God", description="The light, the beginning of everything. "
                                                  "Brother of the Darkness. A being with almost unlimited power.")
        self.god.clues = [MonstersClues.shining_of_magic_neckless]
        self.god.kill_methods = [MonstersKillMethods.the_darkness]

        self.thule = Monster("Thule", description="Nazi members. Used blood magic to make themselves almost undead.")
        self.thule.clues = [MonstersClues.weird_fire_spontaneous_combustion]
        self.thule.kill_methods = [MonstersKillMethods.burn_it, MonstersClues.people_dead_weirdly]

        self.vampire_alpha = Monster("Vampire Alpha", "First Vampire. All Vampires are descendants of the Alpha.")
        self.vampire_alpha.kill_methods = [MonstersKillMethods.colt_of_colt_with_magic_bullets]

        self.hell_hound = Monster("Hell Hound", description="Creation of God, but they were too vicious, "
                                                            "so God kept them short. "
                                                            "Now they hunt people that sold their souls.")
        self.hell_hound.clues = [MonstersClues.invisible_dogs]
        self.hell_hound.kill_methods = [MonstersKillMethods.demon_killing_knife, MonstersKillMethods.angel_sword]
        self.hell_hound.disable_methods = [MonstersDisableMethods.dust_for_hell_hounds]

        self.nephilim = Monster("Nephilim", description="Child of human and angel/archangel. "
                                                        "Human with an angelic grace.")
        self.nephilim.clues = [MonstersClues.weird_weather, MonstersClues.biblical_like_events]

        # SEASON 10:

        self.angel_watcher = Monster("Angel Watcher - Grigori")
        self.angel_watcher.clues = [MonstersClues.triangle_wound_with_burns]
        self.angel_watcher.kill_methods = [MonstersKillMethods.angel_sword]

        self.knight_of_hell = Monster("Knight of hell (Abaddon)")
        self.knight_of_hell.kill_methods = [MonstersKillMethods.first_blade]

        self.witch_from_ozz = Monster("Witch from Ozz")
        self.witch_from_ozz.clues = [MonstersClues.travels_as_black_green_fog]
        self.witch_from_ozz.kill_methods = [MonstersKillMethods.magic_red_high_heels]

        self.witch = Monster("Witch")
        self.witch.clues = \
            [MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
             MonstersClues.missing_heart]
        self.witch.disableMethod = [MonstersDisableMethods.witch_catcher]
        self.witch.kill_methods = [MonstersKillMethods.witch_killing_brew, MonstersKillMethods.cut_thoroat,
                                   MonstersClues.red_eyes]

        self.reaper_death = Monster("Reaper - Death")
        self.reaper_death.kill_methods = [MonstersKillMethods.scythe_of_death]

        # SEASON 11:

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
        self.soul_eater.disable_methods = [MonstersDisableMethods.celtic_sigit_to_trap_monsters]
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

        # SEASON 12:

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

        # SEASON 13:

        self.empty = Monster("Empty", description="The place (and a cosmic being) that angels "
                                                  "and demons go to when they die. "
                                                  "THE God has no power there.")

        self.ghoul = Monster("Ghoul", description="Ghoul is a creature, that feeds on dead people. "
                                                  "It can take the form of a person that it ate.")
        self.ghoul.clues = [MonstersClues.empty_graves]
        self.ghoul.kill_methods = [MonstersKillMethods.decapitation]

        # SEASON 14:

        # SEASON 15:


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

    def choose_clues(self):
        clues = input(Colors.UNDERLINE + "\nChoose clues:" + Colors.ENDC + " ")
        clues = re.sub('[a-zA-Z,&^%$#@?|/:;"_=]', ' ', clues)
        self.chosen_clues = [int(clue) - 1 for clue in clues.split() if (clue.isdigit() and int(clue) <= len(self.clues))]
        if not self.chosen_clues:
            print("No clues chosen. Try again")
            self.choose_clues()

    def print_all_matches(self):
        monster_clues_list = [0] * len(self.monsters)
        for monster_number, monster in enumerate(self.monsters):
            if monster.clues is not None:
                for clue in monster.clues:
                    for chosen_clue in self.chosen_clues:
                        if clue == self.clues[chosen_clue]:
                            monster_clues_list[monster_number] += 1
        for clue_number, clue_match_count in enumerate(monster_clues_list):
            if clue_match_count != 0:
                print(Colors.BOLD + Colors.BLUE + "\n" + str(clue_match_count) + "/" + str(len(self.chosen_clues)) + " Matches:" + Colors.ENDC, end=" ")
                self.monsters[clue_number].print_all()

    def print_all_monsters(self):
        for monster in self.monsters:
            monster.print_all()

    def print_monsters_names(self):
        sorted_monsters = sorted([monster.name for monster in self.monsters])
        print(Colors.RED + Colors.BOLD + "All monsters:" + Colors.ENDC)
        for monster in sorted_monsters:
            print(" »  " + monster)