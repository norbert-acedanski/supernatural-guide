import re
from Monsters import Monster
from Colors import bcolors


class MonsterBase:
    def __init__(self):
        self.symptoms = ["ripped throat", "burned eyes of victims", "eyes - black", "weird weather", "blood - black", "burned by holy water", 
                         "sulfur", "victims wound shaped like triangle", "victims wound shaped like triangle with burns around", "traveling as a black fog", "traveling as a black - green fog", 
                         "people missing/dead weirdly, similarly, randomly across a time(weeks/months/years) in the same area", "people burned on the ceiling of their house", "groups of people missing/dead regularly in the same area", "mooving fast", "strange roar", 
                         "able to use doors (inteligence)", "claws", "mimics human voice", "enormous black fog", "leaves zombie-like people with black vains around neck behind", 
                         
                         "traveling as a red fog", "eyes - red", "EMF", "reacts to Gods name in latin", "summon by saying Bloody Marry in front of the mirror", 
                         "objects seen in nightvision", "being at 2 places at once", "eyes - bright", "weird animal behavior", "skin left behind", 
                         "invisible entity", "ozone smell", "telekinesis", "weird noises", "flashing lights", 
                         "weird things behavior", "seen as a scarecrow", "body torn apart", "no blood in the body", "animal-like attack", 
                         
                         "feeding during the solar eclipse", "missing heart", "leaving soulless people behind", "high strength", "kids's imaginary friend", 
                         "people dead weirdly", "visions", "feeding at night", "ghost-like creature", "victims hear scream", 
                         "feeding on vulnerable", "cold spots", "feeling of something bad", "victims in coma, fading and dying", "junkless creatures", 
                         "mutant pale creature", "eyes - green", "needle-like teeth", "shining of the magic neckles", "victims hear childrens cry", 

                         "weird fire/spontanious combustion", "Bible burns him", "traveling as a white fog", "eyes - yellow", "invisible dogs", 
                         "goat-man", "biblical-like events (storms, diseases, plagues, power losses)", "empty graves"]

        self.kill_method = ["decapitation", "angel blade", "exorcism", "demon killing knife", "holy oil", "first blade",
                           "angel sword", "colt of Colt with magic bullets (silver bullets covered with holy oil, mirra and sage than use a spell)", "magic red high heels", "witch-killing brew", "scythe of the death", 
                           "burn salted corps/remains or destroy object that ghost is bound to", "burn it", "silver bullets into the heart", "surviving the curse", "mixture of Angelica root, van-van oil, dust from the crossroads and other put into the walls facing each world side on each floor", 
                           "burn the sacred tree", "copper coin placed under the tongue", "Zanna killing knife", "cut throat", "gold blade", 
                           
                           "stabing the heart", "will of archangel", "celtic sigil made of blood in the house and in the nest", "The Darkness", "like a human", 
                           "bullet into the head", "lance of the Archangel Michael", "will of Prince of Hell", "will of the Nephilim"]
        
        self.disable_method = ["iron bullets/iron in general", "salt/salted bullets", "symbols of Anastasia (anable to cross)", "dead mans blood", "silver/silver bullets", "decapitation",
                              "Lucyfers cage in hell", "witchcatcher", "all of angels single blow (release of energy)", "celtic imprisonment spell", "symbol made with blood", 
                              "celtic sigit to trap monsters", "holy oil - can't cross it", "dust for hell hounds?", "angel knuckle duster"]
        
        self.cure_methods = ["coctail made of blood of the vampire that bit the victim", "plasma therapy wit the blood of the warevolf that bit the victim"]
        self.chosen_symptoms = []

        # SEASON #1:

        self.prince_of_hell = Monster("Prince of Hell (Azazel, Ramiel, Asmodeus, Dagon)", "The oldest of old demons. One generation after Lilith. They were turned by Lucyfer himself before the Atlantis drown. They were trained to be demonic generals in the war against heaven.")
        self.prince_of_hell.symptoms = [self.symptoms[12], self.symptoms[3], self.symptoms[64]]
        self.prince_of_hell.kill_methods = [self.kill_method[7], self.kill_method[27], self.kill_method[29]]

        self.vengeful_spirit = Monster("Vengeful Spirit")
        self.vengeful_spirit.symptoms = [self.symptoms[11], self.symptoms[25], self.symptoms[26], self.symptoms[31], self.symptoms[32], self.symptoms[33],
                                         self.symptoms[23], self.symptoms[44], self.symptoms[46], self.symptoms[49], self.symptoms[52]]
        self.vengeful_spirit.disable_methods = [self.disable_method[0], self.disable_method[1]]
        self.vengeful_spirit.kill_methods = [self.kill_method[11]]

        self.wendigo = Monster("Wendigo", "It's a product of a kanibalism.")
        self.wendigo.symptoms = [self.symptoms[13], self.symptoms[14], self.symptoms[15], self.symptoms[16], self.symptoms[17], self.symptoms[18]]
        self.wendigo.disable_methods = [self.disable_method[2]]
        self.wendigo.kill_methods = [self.kill_method[12]]

        self.demon = Monster("Demon")
        self.demon.symptoms = [self.symptoms[2], self.symptoms[4], self.symptoms[5], self.symptoms[6], self.symptoms[9], self.symptoms[23],
                               self.symptoms[24], self.symptoms[33], self.symptoms[46]]
        self.demon.kill_methods = [self.kill_method[1], self.kill_method[2], self.kill_method[3], self.kill_method[7], self.kill_method[27], self.kill_method[22]]

        self.shape_shifter = Monster("Shape Shifter")
        self.shape_shifter.symptoms = [self.symptoms[27], self.symptoms[28], self.symptoms[29], self.symptoms[30]]
        self.shape_shifter.kill_methods = [self.kill_method[13]]

        self.revenge_curse = Monster("Revenge Curse")
        self.revenge_curse.symptoms = [self.symptoms[11], self.symptoms[46]]
        self.revenge_curse.kill_methods = [self.kill_method[14]]

        self.poltergeist = Monster("Poltergeist")
        self.poltergeist.symptoms = [self.symptoms[34], self.symptoms[35], self.symptoms[36], self.symptoms[33], self.symptoms[23], self.symptoms[49]]
        self.poltergeist.kill_methods = [self.kill_method[15]]

        self.god_of_norse_vanir = Monster("God Of Norse - Vanir", "Norvegian God of the harvest. Once a year it requires a sacriface in order to maintain prosperity.")
        self.god_of_norse_vanir.symptoms = [self.symptoms[13], self.symptoms[23], self.symptoms[37]]
        self.god_of_norse_vanir.kill_methods = [self.kill_method[16]]

        # SEASON 2:



        # SEASON 3:



        # SEASON 4:



        # SEASON 5:



        # SEASON 6:



        # SEASON 7:



        # SEASON 8:



        # SEASON 9:



        # SEASON #XX:

        self.demon_crowley = Monster("Demon - King of Hell - Crowley")
        self.demon_crowley.symptoms = [self.symptoms[4], self.symptoms[5], self.symptoms[21], self.symptoms[22]]

        self.werewolf = Monster("Warewolf")
        self.werewolf.symptoms = [self.symptoms[38], self.symptoms[40], self.symptoms[42]]
        self.werewolf.kill_methods = [self.kill_method[13]]
        self.werewolf.cure_methods = [self.cure_methods[1]]

        self.vampire = Monster("Vampire")
        self.vampire.symptoms = [self.symptoms[0], self.symptoms[39], self.symptoms[58]]
        self.vampire.disable_methods = [self.disable_method[3]]
        self.vampire.kill_methods = [self.kill_method[0], self.kill_method[1]]
        self.vampire.cure_methods = [self.cure_methods[0]]

        self.angel = Monster("Angel")
        self.angel.symptoms = [self.symptoms[1], self.symptoms[7], self.symptoms[63]]
        self.angel.disable_methods = [self.disable_method[10]]
        self.angel.kill_methods = [self.kill_method[1], self.kill_method[4], self.kill_method[22], self.kill_method[27], self.kill_method[28]]

        self.cupid = Monster("Cupid")
        self.cupid.kill_methods = [self.kill_method[1]]

        self.archangel_lucyfer = Monster("Archangel - Lucyfer")
        self.archangel_lucyfer.symptoms = [self.symptoms[47], self.symptoms[36], self.symptoms[35], self.symptoms[33], self.symptoms[12], self.symptoms[1], self.symptoms[62], self.symptoms[63]]
        self.archangel_lucyfer.disable_methods = [self.disable_method[6], self.disable_method[10], self.disable_method[12], self.disable_method[14]]
        self.archangel_lucyfer.kill_methods = [self.kill_method[24]]

        self.archangel_michael = Monster("Archangel - Michael")
        self.archangel_michael.symptoms = [self.symptoms[63]]
        self.archangel_michael.disable_methods = [self.disable_method[6], self.disable_method[10]]
        self.archangel_michael.kill_methods = [self.kill_method[24]]

        self.god = Monster("THE God", "The light, the beginning of everything. Brother of the Darkness. A being with almost unlimited power.")
        self.god.symptoms = [self.symptoms[59]]
        self.god.kill_methods = [self.kill_method[24]]

        self.psychic = Monster("Psychic")
        self.psychic.symptoms = [self.symptoms[46]]
        self.psychic.kill_methods = [self.kill_method[25]]

        self.thule = Monster("Thule", "Nazi members. Used blood magic to make themselves almost undead.")
        self.thule.symptoms = [self.symptoms[61]]
        self.thule.kill_methods = [self.kill_method[12], self.symptoms[46]]

        self.vampire_alpha = Monster("Vampire Alpha", "First Vampire. All Vampires are descendants of the Alpha.")
        self.vampire_alpha.kill_methods = [self.kill_method[7]]

        self.hell_hound = Monster("Hell Hound", "Creation of God, but they were too vicious so God kept them short. Now they hunt people that sold their souls.")
        self.hell_hound.symptoms = [self.symptoms[65]]
        self.hell_hound.kill_methods = [self.kill_method[3], self.kill_method[6]]
        self.hell_hound.disable_methods = [self.disable_method[13]]

        self.nephilim = Monster("Nephilim", "Child of human and angel/archangel. Human with an angelic grace.")
        self.nephilim.symptoms = [self.symptoms[3], self.symptoms[67]]
        
        # SEASON #10:

        self.angel_watcher = Monster("Angel Watcher - Grigori")
        self.angel_watcher.symptoms = [self.symptoms[8]]
        self.angel_watcher.kill_methods = [self.kill_method[6]]

        self.knight_of_hell = Monster("Knight of hell (Abaddon)")
        self.knight_of_hell.kill_methods = [self.kill_method[5]]

        self.witch_from_ozz = Monster("Witch from Ozz")
        self.witch_from_ozz.symptoms = [self.symptoms[10]]
        self.witch_from_ozz.kill_methods = [self.kill_method[8]]

        self.witch = Monster("Witch")
        self.witch.symptoms = [self.symptoms[11], self.symptoms[42]]
        self.witch.disableMethod = [self.disable_method[7]]
        self.witch.kill_methods = [self.kill_method[9], self.kill_method[19], self.symptoms[22]]

        self.reaper_death = Monster("Reaper - Death")
        self.reaper_death.kill_methods = [self.kill_method[10]]

        # SEASON 11:

        self.darkness = Monster("Darkness", "Sister of God. He was the light, she is the dark. A being with almost unlimited power.")
        self.darkness.symptoms = [self.symptoms[19], self.symptoms[20], self.symptoms[43], self.symptoms[33], self.symptoms[3], self.symptoms[46]]
        self.darkness.disableMethod = [self.disable_method[8]]

        self.whisper = Monster("Whisper")
        self.whisper.symptoms = [self.symptoms[38], self.symptoms[39], self.symptoms[40], self.symptoms[41]]
        self.whisper.kill_methods = [self.kill_method[0], self.kill_method[13]]

        self.nachzehrer = Monster("Nachzehrer (Ghul & Vampire) aka Ghulpire")
        self.nachzehrer.symptoms = [self.symptoms[28], self.symptoms[29], self.symptoms[30], self.symptoms[32]]
        self.nachzehrer.disable_methods = [self.disable_method[4], self.disable_method[5]]
        self.nachzehrer.kill_methods = [self.kill_method[17]]

        self.zanna = Monster("Zanna", "Invisible entities that help children when they are young. When a child no longer needs leeding Zanna leaves a child.")
        self.zanna.symptoms = [self.symptoms[45]]
        self.zanna.kill_methods = [self.kill_method[18]]

        self.banshee = Monster("Banshee")
        self.banshee.symptoms = [self.symptoms[23], self.symptoms[35], self.symptoms[48], self.symptoms[49], self.symptoms[50], self.symptoms[51]]
        self.banshee.disable_methods = [self.disable_method[9]]
        self.banshee.kill_methods = [self.kill_method[20]]

        self.quareen = Monster("Quareen", "Slave creature with bodily form. When curse is layed on a person, Quareen seduces this person as a form of deepest, darkest desire and kills one. The preson that posseses a Quareens heart, commands it.")
        self.quareen.symptoms = [self.symptoms[46], self.symptoms[42]]
        self.quareen.kill_methods = [self.kill_method[21]]

        self.soul_eater = Monster("Soul Eater", "Ghost-like creature existing between worlds. Soul eater moves into a house and makes a nest, which exists outside time and space. The nest feels like a house that a soul eater is in.")
        self.soul_eater.symptoms = [self.symptoms[23], self.symptoms[34], self.symptoms[35], self.symptoms[49], self.symptoms[52], self.symptoms[53],
                                    self.symptoms[54]]
        self.soul_eater.disable_methods = [self.disable_method[11]]
        self.soul_eater.kill_methods = [self.kill_method[23]]

        self.bissan = Monster("Bissan", "Spirits of the Cicada. Every 27 years they come out and have orgies. They can't multiply on their own due to a lack of junk so they 'posses' people to do it.")
        self.bissan.symptoms = [self.symptoms[55], self.symptoms[13], self.symptoms[56], self.symptoms[57], self.symptoms[34], self.symptoms[58]]
        self.bissan.kill_methods = [self.kill_method[0]]

        # SEASON 12:

        self.myling = Monster("Myling", "Scandinavian children ghost. They vry to bring adaults and kill them.")
        self.myling.symptoms = [self.symptoms[60], self.symptoms[46]]
        self.myling.kill_methods = [self.kill_method[11]]

        self.satyr = Monster("Satyr", "Half man half goat creature from greek mythology. They lead people to the woods to grand orgies. When orgy is over satyr feeds on the victim.")
        self.satyr.symptoms = [self.symptoms[11], self.symptoms[66]]

        self.moloch = Monster("Moloch", "God of sacrifice.")
        self.moloch.symptoms = [self.symptoms[11], self.symptoms[66]]
        self.moloch.kill_methods = [self.kill_method[7]]

        # SEZON 13:

        self.empty = Monster("Empty", "The place (and a cosmic beeing) that angels and demons go to when they die. THE God has no power there.")

        self.ghul = Monster("Ghul", "Ghul is a creature, that feeds on dead people. It can take the form of a person that it ate.")
        self.ghul.symptoms = [self.symptoms[68]]
        self.ghul.kill_methods = [self.kill_method[0]]

        self.monsters = [self.prince_of_hell, self.vengeful_spirit, self.wendigo, self.demon, self.shape_shifter, self.revenge_curse,
                         self.poltergeist, self.god_of_norse_vanir,

                         self.demon_crowley, self.werewolf, self.vampire, self.angel, self.cupid,
                         self.archangel_lucyfer, self.archangel_michael, self.god, self.psychic, self.thule,
                         self.vampire_alpha, self.hell_hound, self.nephilim,

                         self.angel_watcher, self.knight_of_hell, self.witch_from_ozz, self.witch, self.reaper_death,

                         self.darkness, self.whisper, self.nachzehrer, self.zanna, self.banshee,
                         self.quareen, self.soul_eater, self.bissan,

                         self.myling, self.satyr, self.moloch,
                         self.empty, self.ghul]

    def print_all_sorted_symptoms(self):
        print(bcolors.BOLD + bcolors.YELLOW + "\nBase of all clues:" + bcolors.ENDC)
        sorted_symptoms = sorted(self.symptoms)
        for symptom_number, symptom in enumerate(sorted_symptoms, 1):
            print(" »%5d  " % symptom_number + symptom)

    def print_all_symptoms(self):
        print(bcolors.BOLD + bcolors.YELLOW + "\nBase of all clues:" + bcolors.ENDC)
        for symptom_number, symptom in enumerate(self.symptoms, 1):
            print(" »%5d  " % symptom_number + symptom)

    def choose_symptoms(self):
        symptoms = input(bcolors.UNDERLINE + "\nChoose clues:" + bcolors.ENDC + " ")
        symptoms = re.sub('[a-zA-Z,&^%$#@?|/:;"_=]', ' ', symptoms)
        self.chosen_symptoms = [int(symptom) - 1 for symptom in symptoms.split() if (symptom.isdigit() and int(symptom) <= len(self.symptoms))]
        if not self.chosen_symptoms:
            print("No clues chosen. Try again")
            self.choose_symptoms()

    def print_all_matches(self):
        monster_symptom_list = [0]*len(self.monsters)
        for monster_number, monster in enumerate(self.monsters):
            if monster.symptoms is not None:
                for symptom in monster.symptoms:
                    for chosen_symptom in self.chosen_symptoms:
                        if symptom == self.symptoms[chosen_symptom]:
                            monster_symptom_list[monster_number] += 1
        for symptom_number, symptom_match_count in enumerate(monster_symptom_list):
            if symptom_match_count != 0:
                print(bcolors.BOLD + bcolors.BLUE + "\n" + str(symptom_match_count) + "/" + str(len(self.chosen_symptoms)) + " Matches:" + bcolors.ENDC, end=" ")
                self.monsters[symptom_number].print_all()

    def print_all_monsters(self):
        for monster in self.monsters:
            monster.print_all()

    def print_monsters_names(self):
        sorted_monsters = sorted([monster.name for monster in self.monsters])
        print(bcolors.RED + bcolors.BOLD + "All monsters:" + bcolors.ENDC)
        for monster in sorted_monsters:
            print(" »  " + monster)