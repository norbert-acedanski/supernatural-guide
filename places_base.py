from colors import Colors
from place import Place
from places_data import PlaceClues


class PlacesBase:
    def __init__(self):
        self.clues = [clue for key, clue in list(PlaceClues.__dict__.items()) if not key.startswith("__")]

        self.hell = Place("Hell", description="Place of eternal torture. People are either tortured, or torture others.",
                          episodes={"S03": [16], "S04": [1, 8, 10]})
        self.hell.clues = [PlaceClues.people_chained_in_a_void, PlaceClues.electrical_storms, PlaceClues.dark_place,
                           PlaceClues.flashing_lights, PlaceClues.time_runs_faster_there]

        self.alternate_timeline = Place("Alternate timeline",
                                        description="A universe, where the history played out differently",
                                        episodes={"S04": [17], "S05": [4]})
        self.alternate_timeline.clues = [PlaceClues.different_history, PlaceClues.different_memories,
                                         PlaceClues.strange_feeling_that_things_should_be_different]

        self.places = [place for place in self.__dict__.values() if isinstance(place, Place)]

    def print_places_names(self):
        sorted_places = sorted([place.name for place in self.places])
        print(Colors.RED + Colors.BOLD + "All places:" + Colors.ENDC)
        for place in sorted_places:
            print(" *  " + place)

    def print_all_places(self):
        for place in self.places:
            place.print_all()
