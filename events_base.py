from colors import Colors
from event import Event
from events_data import EventClues, EventDisableMethods


class EventsBase:
    def __init__(self):
        self.clues = [clue for key, clue in list(EventClues.__dict__.items()) if not key.startswith("__")]
        self.disable_methods = [d_method for key, d_method in list(EventDisableMethods.__dict__.items())
                                if not key.startswith("__")]

        self.apocalypse = Event("Apocalypse", description="Apocalypse is an event, that can be brought by breaking all "
                                                          "66 seals. When all seals are broken, Lucyfer is released "
                                                          "from his cage.", episodes={"S04": [2]})
        self.apocalypse.clues = [EventClues.rise_of_the_witnesses]


        self.events = [event for event in self.__dict__.values() if isinstance(event, Event)]

    def print_events_names(self):
        sorted_places = sorted([place.name for place in self.events])
        print(Colors.RED + Colors.BOLD + "All places:" + Colors.ENDC)
        for place in sorted_places:
            print(" *  " + place)

    def print_all_sorted_clues(self):
        print(Colors.BOLD + Colors.YELLOW + "\nBase of all clues:" + Colors.ENDC)
        sorted_clues = sorted(self.clues)
        for clue_number, clue in enumerate(sorted_clues, 1):
            print(" »%5d  " % clue_number + clue)

    def print_all_events(self):
        for place in self.events:
            place.print_all()
