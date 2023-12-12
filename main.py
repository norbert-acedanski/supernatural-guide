import re
import os

from events_base import EventsBase
from monsters_base import MonsterBase
from curses_base import CursesBase
from objects_base import ObjectsBase
from places_base import PlacesBase
from organizations_base import OrganizationsBase
from colors import Colors


def choose_option():
    chosen_option = 1
    print_values = ["print all monster names", "print all monsters with their attributes",
                    "print all clues of monsters", "find matching monster",
                    "print all curses names",  "print all curses with their attributes",
                    "print all clues of curses", "find matching curse",
                    "print all objects names", "print all objects with their attributes",
                    "print all places names", "print all places with their attributes",
                    "print all events names", "print all events with their attributes",
                    "print all organizations names", "print all organizations with their attributes"]
    while chosen_option != 0:
        print(Colors.GREEN + Colors.BOLD + "\nChoose option: " + Colors.ENDC)
        for option_number, print_value in zip(range(1, 17), print_values):
            print(Colors.MAGENTA + str(option_number) + Colors.ENDC + " - " + print_value)
        print(Colors.MAGENTA + "0" + Colors.ENDC + " - exit")
        print(Colors.MAGENTA + "c" + Colors.ENDC + " - clear the screen")
        chosen_option_str = input()
        chosen_option_str = re.sub('[a-bd-zA-Z,.&^%$#@?|/:;"_=]', '', chosen_option_str)
        if chosen_option_str.isdigit():
            chosen_option = int(chosen_option_str)
        elif chosen_option_str == "c":
            chosen_option = -2
        else:
            chosen_option = -1
        if chosen_option == 1:
            base_of_monsters.print_monsters_names()
        elif chosen_option == 2:
            base_of_monsters.print_all_monsters()
        elif chosen_option == 3:
            base_of_monsters.print_all_sorted_clues()
        elif chosen_option == 4:
            base_of_monsters.print_all_clues()
            while not (chosen_clues := base_of_monsters.choose_clues()):
                print("No clues chosen, try again...")
            base_of_monsters.print_all_matches(chosen_clues)
        elif chosen_option == 5:
            base_of_curses.print_curses_names()
        elif chosen_option == 6:
            base_of_curses.print_all_curses()
        elif chosen_option == 7:
            base_of_curses.print_all_sorted_clues()
        elif chosen_option == 8:
            base_of_curses.print_all_clues()
            while not (chosen_clues := base_of_curses.choose_clues()):
                print("No clues chosen, try again...")
            base_of_curses.print_all_matches(chosen_clues)
        elif chosen_option == 9:
            base_of_objects.print_objects_names()
        elif chosen_option == 10:
            base_of_objects.print_all_objects()
        elif chosen_option == 11:
            base_of_places.print_places_names()
        elif chosen_option == 12:
            base_of_places.print_all_places()
        elif chosen_option == 13:
            base_of_events.print_events_names()
        elif chosen_option == 14:
            base_of_events.print_all_events()
        elif chosen_option == 15:
            base_of_organizations.print_organizations_names()
        elif chosen_option == 16:
            base_of_organizations.print_all_organizations()
        elif chosen_option == 0:
            print("Thank you for playing with this project!")
        elif chosen_option == -2:
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Choose option from the list...")


if __name__ == "__main__":
    base_of_monsters = MonsterBase()
    base_of_curses = CursesBase()
    base_of_objects = ObjectsBase()
    base_of_places = PlacesBase()
    base_of_events = EventsBase()
    base_of_organizations = OrganizationsBase()
    choose_option()
