from colors import Colors
from event import Event
from events_data import EventClues, EventDisableMethods


class EventsBase:

    apocalypse = Event("Apocalypse", description="Apocalypse is an event, that can be brought by breaking any 66 seals "
                                                 "of possible 600 of them. When 66 seals are broken, Lucyfer is "
                                                 "released from his cage. The first seal is broken when a righteous "
                                                 "man sheds blood in Hell. The last seal is the first created demon's "
                                                 "death. After Lucifer is released, four horseman also come to earth.",
                       episodes={"S04": [2, 7, 9, 15, 16, 21, 22], "S05": [1, 2, 4]})
    apocalypse.clues = [EventClues.first_seal, EventClues.rise_of_the_witnesses, EventClues.summoning_of_samhain,
                        EventClues.rippers_killed_under_the_solstice_moon, EventClues.ten_extinct_species_in_one_day,
                        EventClues.fifteen_fishing_man_blind, EventClues.somebody_killing_66_children,
                        EventClues.last_seal, EventClues.biblical_like_events]
    apocalypse.disable_methods = [EventDisableMethods.prevent_all_seals_from_being_broken]

    def __init__(self):
        self.events = [event for event in self.__class__.__dict__.values() if isinstance(event, Event)]
        self.clues = [clue for key, clue in list(EventClues.__dict__.items()) if not key.startswith("__")]
        self.disable_methods = [d_method for key, d_method in list(EventDisableMethods.__dict__.items())
                                if not key.startswith("__")]

    def print_events_names(self):
        sorted_events = sorted([event.name for event in self.events])
        print(Colors.RED + Colors.BOLD + "All events:" + Colors.ENDC)
        for place in sorted_events:
            print(" *  " + place)

    def print_all_sorted_clues(self):
        print(Colors.BOLD + Colors.YELLOW + "\nBase of all clues:" + Colors.ENDC)
        sorted_clues = sorted(self.clues)
        for clue_number, clue in enumerate(sorted_clues, 1):
            print(" »%5d  " % clue_number + clue)

    def print_all_events(self):
        for event in sorted(self.events, key=lambda event: event.name):
            event.print_all()
