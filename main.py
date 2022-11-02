import traceback
import re
from MonsterBase import MonsterBase
from CursesBase import CursesBase
from colors import Colors


def choose_option():
    chosen_option = 1
    while chosen_option != 0:
        print(Colors.GREEN + Colors.BOLD + "\nChoose option: " + Colors.ENDC)
        print(Colors.MAGENTA + "1" + Colors.ENDC + " - print all monster names")
        print(Colors.MAGENTA + "2" + Colors.ENDC + " - print all monsters with their atributes")
        print(Colors.MAGENTA + "3" + Colors.ENDC + " - print all clues of monsters")
        print(Colors.MAGENTA + "4" + Colors.ENDC + " - find matching monster")
        print(Colors.MAGENTA + "5" + Colors.ENDC + " - print all curses names")
        print(Colors.MAGENTA + "6" + Colors.ENDC + " - print all curses with their atributes")
        print(Colors.MAGENTA + "7" + Colors.ENDC + " - print all clues of curses")
        print(Colors.MAGENTA + "8" + Colors.ENDC + " - find matching curse")
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
            base_of_monsters.print_all_sorted_symptoms()
        elif chosen_option == 4:
            base_of_monsters.print_all_symptoms()
            base_of_monsters.choose_symptoms()
            base_of_monsters.print_all_matches()
        elif chosen_option == 5:
            base_of_curses.print_curses_names()
        elif chosen_option == 6:
            base_of_curses.print_all_curses()
        elif chosen_option == 7:
            base_of_curses.print_all_sorted_symptoms()
        elif chosen_option == 8:
            base_of_curses.print_all_symptoms()
            base_of_curses.choose_symptoms()
            base_of_curses.print_all_matches()
        elif chosen_option == 0:
            print("Thank you for playing with this project!")
        else:
            print("Choose option from the list...")
            pass


if __name__ == "__main__":
    try:
        base_of_monsters = MonsterBase()
        base_of_curses = CursesBase()
        choose_option()
    except Exception as e:
        print(traceback.format_exc())
