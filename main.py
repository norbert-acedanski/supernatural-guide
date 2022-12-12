import traceback
import re
from monsters_base import MonsterBase
from curses_base import CursesBase
from objects_base import ObjectsBase
from colors import Colors


def choose_option():
    chosen_option = 1
    while chosen_option != 0:
        print(Colors.GREEN + Colors.BOLD + "\nChoose option: " + Colors.ENDC)
        print(Colors.MAGENTA + "1" + Colors.ENDC + " - print all monster names")
        print(Colors.MAGENTA + "2" + Colors.ENDC + " - print all monsters with their attributes")
        print(Colors.MAGENTA + "3" + Colors.ENDC + " - print all clues of monsters")
        print(Colors.MAGENTA + "4" + Colors.ENDC + " - find matching monster")
        print(Colors.MAGENTA + "5" + Colors.ENDC + " - print all curses names")
        print(Colors.MAGENTA + "6" + Colors.ENDC + " - print all curses with their attributes")
        print(Colors.MAGENTA + "7" + Colors.ENDC + " - print all clues of curses")
        print(Colors.MAGENTA + "8" + Colors.ENDC + " - find matching curse")
        print(Colors.MAGENTA + "9" + Colors.ENDC + " - print all objects names")
        print(Colors.MAGENTA + "10" + Colors.ENDC + " - print all objects with their attributes")
        print(Colors.MAGENTA + "0" + Colors.ENDC + " - exit")
        chosen_option_str = input()
        chosen_option_str = re.sub('[a-zA-Z,.&^%$#@?|/:;"_=]', '', chosen_option_str)
        if chosen_option_str.isdigit():
            chosen_option = int(chosen_option_str)
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
        elif chosen_option == 0:
            print("Thank you for playing with this project!")
        else:
            print("Choose option from the list...")
            pass


if __name__ == "__main__":
    try:
        base_of_monsters = MonsterBase()
        base_of_curses = CursesBase()
        base_of_objects = ObjectsBase()
        choose_option()
    except Exception as e:
        print(traceback.format_exc())
