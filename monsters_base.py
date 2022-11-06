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
                                                  "They were trained to be demonic generals in the war against heaven.")
        self.prince_of_hell.clues = [MonstersClues.people_burned_on_the_ceiling,

                                     MonstersClues.weird_things_behavior,
                                     MonstersClues.weird_weather, MonstersClues.yellow_eyes]
        self.prince_of_hell.kill_methods = [
                                            MonstersKillMethods.colt_of_colt_with_magic_bullets,
                                            MonstersKillMethods.lance_of_archangel_michael,
                                            MonstersKillMethods.will_of_a_nephilim]

        self.vengeful_spirit = Monster("Vengeful Spirit")
        self.vengeful_spirit.clues = [MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                                      MonstersClues.people_dead_weirdly, MonstersClues.ghost_like_creature,
                                      MonstersClues.weird_electronics_behavior, MonstersClues.weird_things_behavior,
                                      MonstersClues.local_legend_about_somebody_killed_or_died,
                                      MonstersClues.telekinesis,

                                      MonstersClues.objects_seen_in_night_vision, MonstersClues.invisible_entity,
                                      MonstersClues.summoned_by_saying_bloody_marry_in_front_of_the_mirror,
                                      MonstersClues.ozone_smell,
                                      MonstersClues.emf, MonstersClues.high_strength, MonstersClues.cold_spots]
        self.vengeful_spirit.disable_methods = [
                                                MonstersDisableMethods.iron_or_iron_bullets,
                                                MonstersDisableMethods.salt_or_salted_bullets]
        self.vengeful_spirit.kill_methods = [MonstersKillMethods.bring_the_spirit_to_its_crime_place,

                                             MonstersKillMethods.burn_salted_corpe_or_destroy_object_that_ghost_is_bound_to
                                             ]

        self.wendigo = Monster("Wendigo", description="Wending in Cree Indian means 'evil, that devours'. "
                                                      "These creatures can live to hundreds of years. "
                                                      "Each Wendigo was once a man. "
                                                      "It's a product of a cannibalism - people in "
                                                      "camps/mineshafts/tribes due to lack of supplies eat others. "
                                                      "Stores other man as a supply for winters as food.")
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

        self.demon = Monster("Demon")
        self.demon.clues = [MonstersClues.black_eyes, MonstersClues.black_blood, MonstersClues.burned_by_holy_water,
                            MonstersClues.sulfur, MonstersClues.travels_as_black_fog, MonstersClues.emf,
                            MonstersClues.reacts_to_gods_name_in_latin, MonstersClues.telekinesis,
                            MonstersClues.people_dead_weirdly]
        self.demon.kill_methods = [MonstersKillMethods.angel_blade, MonstersKillMethods.exorcism,
                                   MonstersKillMethods.demon_killing_knife, MonstersKillMethods.will_of_an_archangel,
                                   MonstersKillMethods.colt_of_colt_with_magic_bullets,
                                   MonstersKillMethods.lance_of_archangel_michael]

        self.shape_shifter = Monster("Shape Shifter")
        self.shape_shifter.clues = [MonstersClues.being_at_two_places_at_once, MonstersClues.bright_eyes,
                                    MonstersClues.weird_animal_behavior, MonstersClues.skin_left_behind]
        self.shape_shifter.kill_methods = [MonstersKillMethods.silver_bullet_into_the_heart]

        self.revenge_curse = Monster("Revenge Curse")
        self.revenge_curse.clues = [MonstersClues.missing_or_dead_people_in_similar_way_randomly_across_time_in_the_same_area,
                                    MonstersClues.people_dead_weirdly]
        self.revenge_curse.kill_methods = [MonstersKillMethods.surviving_the_curse]

        self.poltergeist = Monster("Poltergeist")
        self.poltergeist.clues = [MonstersClues.weird_noises, MonstersClues.flashing_lights,
                                  MonstersClues.weird_things_behavior, MonstersClues.telekinesis, MonstersClues.emf,
                                  MonstersClues.ghost_like_creature]
        self.poltergeist.kill_methods = [MonstersKillMethods.angelica_root_mixture]

        self.god_of_norse_vanir = Monster("God Of Norse - Vanir",
                                          description="Norvegian God of the harvest. "
                                                      "Once a year it requires a sacriface "
                                                      "in order to maintain prosperity.")
        self.god_of_norse_vanir.clues = [MonstersClues.missing_or_dead_people_regularly_in_the_same_area,
                                         MonstersClues.emf, MonstersClues.seen_as_a_scarecrow]
        self.god_of_norse_vanir.kill_methods = [MonstersKillMethods.burn_the_sacred_tree]

        # SEASON 2:



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

        self.werewolf = Monster("Werewolf")
        self.werewolf.clues = [MonstersClues.body_torn_apart, MonstersClues.animal_like_attack,
                               MonstersClues.missing_heart]
        self.werewolf.kill_methods = [MonstersKillMethods.silver_bullet_into_the_heart]
        self.werewolf.cure_methods = \
            [MonstersCureMethods.plasma_therapy_with_the_blood_of_the_werewolf_that_bit_the_victim]

        self.vampire = Monster("Vampire")
        self.vampire.clues = [MonstersClues.ripped_throat, MonstersClues.no_blood_in_the_body,
                              MonstersClues.needle_like_teeth]
        self.vampire.disable_methods = [MonstersDisableMethods.dead_mans_blood]
        self.vampire.kill_methods = [MonstersKillMethods.decapitation, MonstersKillMethods.angel_blade]
        self.vampire.cure_methods = [MonstersCureMethods.cocktail_made_of_blood_of_the_vampire_that_bit_the_victim]

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

        self.psychic = Monster("Psychic")
        self.psychic.clues = [MonstersClues.people_dead_weirdly]
        self.psychic.kill_methods = [MonstersKillMethods.like_any_human]

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
        self.myling.kill_methods = [MonstersKillMethods.burn_salted_corpe_or_destroy_object_that_ghost_is_bound_to]

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


        self.monsters = [monster for monster in self.__dict__.values() if not isinstance(monster, list)]

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