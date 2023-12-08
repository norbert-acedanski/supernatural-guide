from colors import Colors
from place import Place
from places_data import PlaceClues


class PlacesBase:
    hell = Place("Hell", description="Place of eternal torture. People are either tortured, or torture others. Hell "
                                     "can be accessed via a Portal guarded by a Reaper in S11E10.",
                 episodes={"S03": [16], "S04": [1, 8, 10], "S06": [20], "S08": [19], "S10": [3], "S11": [9, 10],
                           "S15": [3, 8]})
    hell.clues = [PlaceClues.people_chained_in_a_void, PlaceClues.electrical_storms, PlaceClues.dark_place,
                  PlaceClues.flashing_lights, PlaceClues.time_runs_faster_there, PlaceClues.endless_queue,
                  PlaceClues.screaming_people, PlaceClues.skeletons_on_the_ground, PlaceClues.cells_with_people_inside]

    alternate_timeline = Place("Alternate timeline",
                               description="A universe, where the history played out differently. Can be accessed via "
                                           "a spell or an Angel can put you in one. In S12E23 we see a world, where "
                                           "Sam and Dean are never born and this Universe is in a war between in "
                                           "Heaven and Hell. Mary and Lucyfer are trapped in there in S12E23. GOD lost "
                                           "count on how many Universes there are.",
                               episodes={"S04": [17], "S05": [4], "S06": [15, 17], "S12": [23], "S13": [2, 18, 21, 22],
                                         "S14": [13]})
    alternate_timeline.clues = [PlaceClues.different_history, PlaceClues.different_memories,
                                PlaceClues.strange_feeling_that_things_should_be_different]

    heaven = Place("Heaven", description="Place where good people go after they die. It is not a single place, but "
                                         "collection of all of the peoples personal heavens. There is a road, that "
                                         "goes through heaven called Axis Mundi. It is different for everyone. "
                                         "It can be a literal road, but also a model, a picture, magazine. "
                                         "Leads to a garden in the center. After the Fall of Angels, the Heaven is "
                                         "sealed by Metatron with a spell. There is a portal from Heaven to Earth "
                                         "created by Metatron, for Angels to travel between those two places. Angels "
                                         "can't sense it because it changes its location. Heaven has it's own prison. "
                                         "A Human can escape his/her heaven by finding a thing, that does not belong "
                                         "in the place, they are in and following it. Heaven is powered by Angels "
                                         "(according to Naomi from S1319).",
                   episodes={"S05": [16], "S08": [7, 10, 17, 23], "S09": [18, 22, 23], "S10": [2, 17], "S11": [18, 22],
                             "S13": [13, 18, 19], "S14": [8, 19]})
    heaven.clues = [PlaceClues.good_memories_relived, PlaceClues.changing_scenery, PlaceClues.bright_place]

    purgatory = Place("Purgatory", description="A place, where all monsters go, after they die. Can be opened with an "
                                               "ancient ritual and let 'Mother' to the Earth. In a place, that is the "
                                               "entrance, you have to use a proper spell, drop dragon blood down and "
                                               "let a virgin fall to the door. Opened in S06E12. Can also be opened in "
                                               "any place, but a proper spell, blood of a virgin, blood of a Purgatory "
                                               "native monster and it has to be the eclipse. A proper sigil has to be "
                                               "drawn on a wall. Opened again in S06E22 to let all creatures into "
                                               "Castiel. Opened again in S07E01 to let all creatures into Purgatory. "
                                               "One can go to Purgatory, when using Leviathan killing weapon in close "
                                               "proximity. GOD made a back door for humans to escape if one ever got "
                                               "to Purgatory. It also has a direct connection to Hell through "
                                               "a portal, where 3 trees meet 1. A rogue reaper can transfer "
                                               "a person into it.", episodes={"S07": [23], "S08": [1, 19], "S15": [9]})
    purgatory.clues = [PlaceClues.dark_place, PlaceClues.monsters_nearby,
                       PlaceClues.when_a_person_comes_back_from_it_a_bright_light_appears]

    oz = Place("Oz", description="A magical land, where Dorothy was as a child. You can enter Oz in different ways, "
                                 "like tornado, yey of a hurricane, a whirlpool, but there is a key to Oz. Inserted "
                                 "into any door - it opens a portal to Oz (a golden path). When used with a proper "
                                 "spell - it can open door to any place in Oz.", episodes={"S09": [4]})
    oz.clues = [PlaceClues.castle_structure_on_a_hill, PlaceClues.golden_path, PlaceClues.emerald_city]

    empty = Place("Empty", description="Place (and a cosmic being), where a Reaper want's Sam and Dean to go when they "
                                       "die. Mentioned in S11E17. First appearance in S13E03. A place that angels and "
                                       "demons go to when they die. THE God has no power there. According to Empty "
                                       "(being), before GOD and Amara there was nothing but Empty. When Angel or a "
                                       "Demon comes here, they sleep peacefully forever. Castiel is the first being, "
                                       "that became awake, Lucyfer is the second in S14E07.",
                  episodes={"S13": [3, 4], "S14": [7, 17, 20]})
    empty.clues = [PlaceClues.dark_place, PlaceClues.levitating_black_goo]

    def __init__(self):
        self.places = [place for place in self.__class__.__dict__.values() if isinstance(place, Place)]
        self.clues = [clue for key, clue in list(PlaceClues.__dict__.items()) if not key.startswith("__")]

    def print_places_names(self):
        sorted_places = sorted([place.name for place in self.places])
        print(Colors.RED + Colors.BOLD + "All places:" + Colors.ENDC)
        for place in sorted_places:
            print(" *  " + place)

    def print_all_places(self):
        for place in self.places:
            place.print_all()
