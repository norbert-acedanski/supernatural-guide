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

        self.killMethod = ["decapitation", "angel blade", "exorcism", "demon killing knife", "holy oil", "first blade", 
                           "angel sword", "colt of Colt with magic bullets (silver bullets covered with holy oil, mirra and sage than use a spell)", "magic red high heels", "witch-killing brew", "scythe of the death", 
                           "burn salted corps/remains or destroy object that ghost is bound to", "burn it", "silver bullets into the heart", "surviving the curse", "mixture of Angelica root, van-van oil, dust from the crossroads and other put into the walls facing each world side on each floor", 
                           "burn the sacred tree", "copper coin placed under the tongue", "Zanna killing knife", "cut throat", "gold blade", 
                           
                           "stabing the heart", "will of archangel", "celtic sigil made of blood in the house and in the nest", "The Darkness", "like a human", 
                           "bullet into the head", "lance of the Archangel Michael", "will of Prince of Hell", "will of the Nephilim"]
        
        self.disableMethod = ["iron bullets/iron in general", "salt/salted bullets", "symbols of Anastasia (anable to cross)", "dead mans blood", "silver/silver bullets", "decapitation", 
                              "Lucyfers cage in hell", "witchcatcher", "all of angels single blow (release of energy)", "celtic imprisonment spell", "symbol made with blood", 
                              "celtic sigit to trap monsters", "holy oil - can't cross it", "dust for hell hounds?", "angel knuckle duster"]
        
        self.cureMethods = ["coctail made of blood of the vampire that bit the victim", "plasma therapy wit the blood of the warevolf that bit the victim"]
        self.chosenSymptoms = []

        # SESON #1:

        self.PrinceOfHell = Monster("Prince of Hell (Azazel, Ramiel, Asmodeus, Dagon)", "The oldest of old demons. One generation after Lilith. They were turned by Lucyfer himself before the Atlantis drown. They were trained to be demonic generals in the war against heaven.")
        self.PrinceOfHell.symptoms = [self.symptoms[12], self.symptoms[3], self.symptoms[64]]
        self.PrinceOfHell.killMethods = [self.killMethod[7], self.killMethod[27], self.killMethod[29]]

        self.WengefulSpirit = Monster("Vengeful Spirit")
        self.WengefulSpirit.symptoms = [self.symptoms[11], self.symptoms[25], self.symptoms[26], self.symptoms[31], self.symptoms[32], self.symptoms[33], 
                                        self.symptoms[23], self.symptoms[44],self.symptoms[46], self.symptoms[49], self.symptoms[52]]
        self.WengefulSpirit.disableMethods = [self.disableMethod[0], self.disableMethod[1]]
        self.WengefulSpirit.killMethods = [self.killMethod[11]]

        self.Wendigo = Monster("Wendigo", "It's a product of a kanibalism.")
        self.Wendigo.symptoms = [self.symptoms[13], self.symptoms[14], self.symptoms[15], self.symptoms[16], self.symptoms[17], self.symptoms[18]]
        self.Wendigo.disableMethods = [self.disableMethod[2]]
        self.Wendigo.killMethods = [self.killMethod[12]]

        self.Demon = Monster("Demon")
        self.Demon.symptoms = [self.symptoms[2], self.symptoms[4], self.symptoms[5], self.symptoms[6], self.symptoms[9], self.symptoms[23], 
                               self.symptoms[24], self.symptoms[33], self.symptoms[46]]
        self.Demon.killMethods = [self.killMethod[1], self.killMethod[2], self.killMethod[3], self.killMethod[7], self.killMethod[27], self.killMethod[22]]

        self.ShapeShifter = Monster("Shape Shifter")
        self.ShapeShifter.symptoms = [self.symptoms[27], self.symptoms[28], self.symptoms[29], self.symptoms[30]]
        self.ShapeShifter.killMethods = [self.killMethod[13]]

        self.RevengeCurse = Monster("Revenge Curse")
        self.RevengeCurse.symptoms = [self.symptoms[11], self.symptoms[46]]
        self.RevengeCurse.killMethods = [self.killMethod[14]]

        self.Poltergeist = Monster("Poltergeist")
        self.Poltergeist.symptoms = [self.symptoms[34], self.symptoms[35], self.symptoms[36], self.symptoms[33], self.symptoms[23], self.symptoms[49]]
        self.Poltergeist.killMethods = [self.killMethod[15]]

        self.GodOfNorseVanir = Monster("God Of Norse - Vanir", "Norvegian God of the harvest. Once a year it requires a sacriface in order to maintain prosperity.")
        self.GodOfNorseVanir.symptoms = [self.symptoms[13], self.symptoms[23], self.symptoms[37]]
        self.GodOfNorseVanir.killMethods = [self.killMethod[16]]

        # SESON 2:



        # SESON 3:



        # SESON 4:



        # SESON 5:



        # SESON 6:



        # SESON 7:



        # SESON 8:



        # SESON 9:



        # SESON #XX:

        self.DemonCrowley = Monster("Demon - King of Hell - Crowley")
        self.DemonCrowley.symptoms = [self.symptoms[4], self.symptoms[5], self.symptoms[21], self.symptoms[22]]

        self.Warewolf = Monster("Warewolf")
        self.Warewolf.symptoms = [self.symptoms[38], self.symptoms[40], self.symptoms[42]]
        self.Warewolf.killMethods = [self.killMethod[13]]
        self.Warewolf.cureMethods = [self.cureMethods[1]]

        self.Vampire = Monster("Vampire")
        self.Vampire.symptoms = [self.symptoms[0], self.symptoms[39], self.symptoms[58]]
        self.Vampire.disableMethods = [self.disableMethod[3]]
        self.Vampire.killMethods = [self.killMethod[0], self.killMethod[1]]
        self.Vampire.cureMethods = [self.cureMethods[0]]

        self.Angel = Monster("Angel")
        self.Angel.symptoms = [self.symptoms[1], self.symptoms[7], self.symptoms[63]]
        self.Angel.disableMethods = [self.disableMethod[10]]
        self.Angel.killMethods = [self.killMethod[1], self.killMethod[4], self.killMethod[22], self.killMethod[27], self.killMethod[28]]

        self.Cupid = Monster("Cupid")
        self.Cupid.killMethods = [self.killMethod[1]]

        self.ArchangelLucyfer = Monster("Archangel - Lucyfer")
        self.ArchangelLucyfer.symptoms = [self.symptoms[47], self.symptoms[36], self.symptoms[35], self.symptoms[33], self.symptoms[12], self.symptoms[1], self.symptoms[62], self.symptoms[63]]
        self.ArchangelLucyfer.disableMethods = [self.disableMethod[6], self.disableMethod[10], self.disableMethod[12], self.disableMethod[14]]
        self.ArchangelLucyfer.killMethods = [self.killMethod[24]]

        self.ArchangelMichael = Monster("Archangel - Michael")
        self.ArchangelMichael.symptoms = [self.symptoms[63]]
        self.ArchangelMichael.disableMethods = [self.disableMethod[6],self.disableMethod[10]]
        self.ArchangelMichael.killMethods = [self.killMethod[24]]

        self.God = Monster("THE God", "The light, the beginning of everything. Brother of the Darkness. A being with almost unlimited power.")
        self.God.symptoms = [self.symptoms[59]]
        self.God.killMethods = [self.killMethod[24]]

        self.Psychic = Monster("Psychic")
        self.Psychic.symptoms = [self.symptoms[46]]
        self.Psychic.killMethods = [self.killMethod[25]]

        self.Thul = Monster("Thul", "Nazi members. Used blood magic to make themselves almost undead.")
        self.Thul.symptoms = [self.symptoms[61]]
        self.Thul.killMethods = [self.killMethod[12], self.symptoms[46]]

        self.VampireAlpha = Monster("Vampire Alpha", "First Vampire. All Vampires are descendants of the Alpha.")
        self.VampireAlpha.killMethods = [self.killMethod[7]]

        self.HellHound = Monster("Hell Hound", "Creation of God, but they were too vicious so God kept them short. Now they hunt people that sold their souls.")
        self.HellHound.symptoms = [self.symptoms[65]]
        self.HellHound.killMethods = [self.killMethod[3], self.killMethod[6]]
        self.HellHound.disableMethods = [self.disableMethod[13]]

        self.Nephilim = Monster("Nephilim", "Child of human and angel/archangel. Human with an angelic grace.")
        self.Nephilim.symptoms = [self.symptoms[3], self.symptoms[67]]
        
        # SESON #10:

        self.AngelWatcher = Monster("Angel Watcher - Grigori")
        self.AngelWatcher.symptoms = [self.symptoms[8]]
        self.AngelWatcher.killMethods = [self.killMethod[6]]

        self.KnightOfHell = Monster("Knight of hell (Abaddon)")
        self.KnightOfHell.killMethods = [self.killMethod[5]]

        self.WitchFromOzz = Monster("Witch from Ozz")
        self.WitchFromOzz.symptoms = [self.symptoms[10]]
        self.WitchFromOzz.killMethods = [self.killMethod[8]]

        self.Witch = Monster("Witch")
        self.Witch.symptoms = [self.symptoms[11], self.symptoms[42]]
        self.Witch.disableMethod = [self.disableMethod[7]]
        self.Witch.killMethods = [self.killMethod[9], self.killMethod[19], self.symptoms[22]]

        self.ReaperDeath = Monster("Reaper - Death")
        self.ReaperDeath.killMethods = [self.killMethod[10]]

        # SESON 11:

        self.Darkness = Monster("Darkness", "Sister of God. He was the light, she is the dark. A being with almost unlimited power.")
        self.Darkness.symptoms = [self.symptoms[19], self.symptoms[20], self.symptoms[43], self.symptoms[33], self.symptoms[3], self.symptoms[46]]
        self.Darkness.disableMethod = [self.disableMethod[8]]

        self.Whisper = Monster("Whisper")
        self.Whisper.symptoms = [self.symptoms[38], self.symptoms[39], self.symptoms[40], self.symptoms[41]]
        self.Whisper.killMethods = [self.killMethod[0], self.killMethod[13]]

        self.Nachzehrer = Monster("Nachzehrer (Ghul & Vampire) aka Ghulpire")
        self.Nachzehrer.symptoms = [self.symptoms[28], self.symptoms[29], self.symptoms[30], self.symptoms[32]]
        self.Nachzehrer.disableMethods = [self.disableMethod[4], self.disableMethod[5]]
        self.Nachzehrer.killMethods = [self.killMethod[17]]

        self.Zanna = Monster("Zanna", "Invisible entities that help children when they are young. When a child no longer needs leeding Zanna leaves a child.")
        self.Zanna.symptoms = [self.symptoms[45]]
        self.Zanna.killMethods = [self.killMethod[18]]

        self.Banshee = Monster("Banshee")
        self.Banshee.symptoms = [self.symptoms[23], self.symptoms[35], self.symptoms[48], self.symptoms[49], self.symptoms[50], self.symptoms[51]]
        self.Banshee.disableMethods = [self.disableMethod[9]]
        self.Banshee.killMethods = [self.killMethod[20]]

        self.Quareen = Monster("Quareen", "Slave creature with bodily form. When curse is layed on a person, Quareen seduces this person as a form of deepest, darkest desire and kills one. The preson that posseses a Quareens heart, commands it.")
        self.Quareen.symptoms = [self.symptoms[46], self.symptoms[42]]
        self.Quareen.killMethods = [self.killMethod[21]]

        self.SoulEater = Monster("Soul Eater", "Ghost-like creature existing between worlds. Soul eater moves into a house and makes a nest, which exists outside time and space. The nest feels like a house that a soul eater is in.")
        self.SoulEater.symptoms = [self.symptoms[23], self.symptoms[34], self.symptoms[35], self.symptoms[49], self.symptoms[52], self.symptoms[53], 
                                   self.symptoms[54]]
        self.SoulEater.disableMethods = [self.disableMethod[11]]
        self.SoulEater.killMethods = [self.killMethod[23]]

        self.Bissan = Monster("Bissan", "Spirits of the Cicada. Every 27 years they come out and have orgies. They can't multiply on their own due to a lack of junk so they 'posses' people to do it.")
        self.Bissan.symptoms = [self.symptoms[55], self.symptoms[13], self.symptoms[56], self.symptoms[57], self.symptoms[34], self.symptoms[58]]
        self.Bissan.killMethods = [self.killMethod[0]]

        # SESON 12:

        self.Myling = Monster("Myling", "Scandinavian children ghost. They vry to bring adaults and kill them.")
        self.Myling.symptoms = [self.symptoms[60], self.symptoms[46]]
        self.Myling.killMethods = [self.killMethod[11]]

        self.Satyr = Monster("Satyr", "Half man half goat creature from greek mythology. They lead people to the woods to grand orgies. When orgy is over satyr feeds on the victim.")
        self.Satyr.symptoms = [self.symptoms[11], self.symptoms[66]]

        self.Moloch = Monster("Moloch", "God of sacrifice.")
        self.Moloch.symptoms = [self.symptoms[11], self.symptoms[66]]
        self.Moloch.killMethods = [self.killMethod[7]]

        # SEZON 13:

        self.Empty = Monster("Empty", "The place (and a cosmic beeing) that angels and demons go to when they die. THE God has no power there.")

        self.Ghul = Monster("Ghul", "Ghul is a creature, that feeds on dead people. It can take the form of a person that it ate.")
        self.Ghul.symptoms = [self.symptoms[68]]
        self.Ghul.killMethods = [self.killMethod[0]]

        self.Monsters = [self.PrinceOfHell, self.WengefulSpirit, self.Wendigo, self.Demon, self.ShapeShifter, self.RevengeCurse, 
                         self.Poltergeist, self.GodOfNorseVanir, 

                         self.DemonCrowley, self.Warewolf, self.Vampire, self.Angel, self.Cupid, 
                         self.ArchangelLucyfer, self.ArchangelMichael, self.God, self.Psychic, self.Thul, 
                         self.VampireAlpha, self.HellHound, self.Nephilim, 
                         
                         self.AngelWatcher, self.KnightOfHell, self.WitchFromOzz, self.Witch, self.ReaperDeath, 
                         
                         self.Darkness, self.Whisper, self.Nachzehrer, self.Zanna, self.Banshee, 
                         self.Quareen, self.SoulEater, self.Bissan, 
                         
                         self.Myling, self.Satyr, self.Moloch, 
                         self.Empty, self.Ghul]

    def printAllSortedSymptoms(self):
        sortedSymptoms = [None]*len(self.symptoms)
        print(bcolors.BOLD + bcolors.YELLOW + "\nBase of all symptoms:" + bcolors.ENDC)
        i = 0
        sortedSymptoms = sorted(self.symptoms)
        for symptom in sortedSymptoms:
            print(" »%5d  " % (i + 1) + symptom)
            i += 1

    def printAllSymptoms(self):
        print(bcolors.BOLD + bcolors.YELLOW + "\nBase of all symptoms:" + bcolors.ENDC)
        i = 0
        for symptom in self.symptoms:
            print(" »%5d  " % (i + 1) + symptom)
            i += 1

    def chooseSymptoms(self):
        symptoms = input(bcolors.UNDERLINE + "\nChoose symptoms:" + bcolors.ENDC + " ")
        symptoms = re.sub('[a-zA-Z,&^%$#@?|/:;"_=]', ' ', symptoms)
        self.chosenSymptoms = [int(symptom) - 1 for symptom in symptoms.split() if (symptom.isdigit() and int(symptom) <= len(self.symptoms))]
        if self.chosenSymptoms == []:
            print("No symptoms chosen. Try again")
            self.chooseSymptoms()

    def printAllMachtes(self):
        monsterSymptomList = [None]*len(self.Monsters)
        for monster in range(len(self.Monsters)):
            monsterSymptomList[monster] = 0
        i = 0
        for monster in self.Monsters:
            if monster.symptoms is not None:
                for symptom in monster.symptoms:
                    for choosenSympton in self.chosenSymptoms:
                        if symptom == self.symptoms[choosenSympton]:
                            monsterSymptomList[i] += 1
            i += 1
        for number in range(len(monsterSymptomList)):
            if monsterSymptomList[number] != 0:
                print(bcolors.BOLD + bcolors.BLUE + "\n" + str(monsterSymptomList[number]) + "/" + str(len(self.chosenSymptoms)) + " Matches:" + bcolors.ENDC, end=" ")
                self.Monsters[number].printAll()

    def printAllMonsters(self):
        for monster in self.Monsters:
            monster.printAll()

    def printMonstersNames(self):
        sortedMonsters = [None]*len(self.Monsters)
        i = 0
        for monster in self.Monsters:
            sortedMonsters[i] = monster.name
            i += 1
        sortedMonsters = sorted(sortedMonsters)
        print(bcolors.RED + bcolors.BOLD + "All monsters:" + bcolors.ENDC)
        for name in range(len(sortedMonsters)):
            print(" »  " + sortedMonsters[name])