from colors import Colors
from place import Place
from places_data import PlaceClues


class PlacesBase:
    def __init__(self):
        self.clues = [clue for key, clue in list(PlaceClues.__dict__.items()) if not key.startswith("__")]

        self.hell = Place("Hell", description="Place of eternal torture. People are either tortured, or torture others.",
                          episodes={"S03": [16], "S04": [1, 8, 10], "S06": [20]})
        self.hell.clues = [PlaceClues.people_chained_in_a_void, PlaceClues.electrical_storms, PlaceClues.dark_place,
                           PlaceClues.flashing_lights, PlaceClues.time_runs_faster_there, PlaceClues.endless_queue]

        self.alternate_timeline = Place("Alternate timeline",
                                        description="A universe, where the history played out differently. "
                                                    "Can be accessed via a spell or an angel can put you in one.",
                                        episodes={"S04": [17], "S05": [4], "S06": [15, 17]})
        self.alternate_timeline.clues = [PlaceClues.different_history, PlaceClues.different_memories,
                                         PlaceClues.strange_feeling_that_things_should_be_different]

        self.heaven = Place("Heaven", description="Place where good people go after they die. It is not a single "
                                                  "place, but collection of all of the peoples personal heavens. "
                                                  "There is a road, that goes through heaven called Axis Mundi. "
                                                  "It is different for everyone. It can be a literal road, but also "
                                                  "a model, a picture, magazine. Leads to a garden in the center.",
                            episodes={"S05": [16]})
        self.heaven.clues = [PlaceClues.good_memories_relived, PlaceClues.changing_scenery]

        self.purgatory = Place("Purgatory", description="A place, where all monsters go, after they die. "
                                                        "Can be opened with an ancient ritual and let 'Mother' "
                                                        "to the Earth. In a place, that is the entrance, "
                                                        "you have to use a proper spell, drop dragon blood down "
                                                        "and let a virgin fall to the door. Opened in S06E12. "
                                                        "Can also be opened in any place, but a proper spell, "
                                                        "blood of a virgin, blood of a Purgatory native monster and "
                                                        "it has to be the eclipse. A proper sigil has to be drawn "
                                                        "on a wall. Opened again in S06E22 to let all creatures "
                                                        "into Castiel. Opened again in S07E01 to let all creatures "
                                                        "into Purgatory. One can go to Purgatory, when using Leviathan "
                                                        "killing weapon in close proximity.", episodes={"S07": [23]})
        self.purgatory.clues = [PlaceClues.dark_place, PlaceClues.monsters_nearby]

        self.places = [place for place in self.__dict__.values() if isinstance(place, Place)]

    def print_places_names(self):
        sorted_places = sorted([place.name for place in self.places])
        print(Colors.RED + Colors.BOLD + "All places:" + Colors.ENDC)
        for place in sorted_places:
            print(" *  " + place)

    def print_all_places(self):
        for place in self.places:
            place.print_all()
