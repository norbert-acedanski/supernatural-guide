import traceback
import re
from MonsterBase import MonsterBase
from CursesBase import CursesBase
from Colors import bcolors


def choose_option():
    chosen_option = 1
    while chosen_option != 0:
        print(bcolors.GREEN + bcolors.BOLD + "\nChoose option: " + bcolors.ENDC)
        print(bcolors.MAGENTA + "1" + bcolors.ENDC + " - print all monster names")
        print(bcolors.MAGENTA + "2" + bcolors.ENDC + " - print all monsters with their atributes")
        print(bcolors.MAGENTA + "3" + bcolors.ENDC + " - print all clues of monsters")
        print(bcolors.MAGENTA + "4" + bcolors.ENDC + " - find matching monster")
        print(bcolors.MAGENTA + "5" + bcolors.ENDC + " - print all curses names")
        print(bcolors.MAGENTA + "6" + bcolors.ENDC + " - print all curses with their atributes")
        print(bcolors.MAGENTA + "7" + bcolors.ENDC + " - print all clues of curses")
        print(bcolors.MAGENTA + "8" + bcolors.ENDC + " - find matching curse")
        print(bcolors.MAGENTA + "0" + bcolors.ENDC + " - exit")
        chosen_option_str = input()
        chosen_option_str = re.sub('[a-zA-Z,.&^%$#@?|/:;"_=]', '', chosen_option_str)
        if chosen_option_str.isdigit():
            chosen_option = int(chosen_option_str)
        else:
            chosen_option = -1
        if chosen_option == 1:
            base_of_monsters.printMonstersNames()
        elif chosen_option == 2:
            base_of_monsters.printAllMonsters()
        elif chosen_option == 3:
            base_of_monsters.printAllSortedSymptoms()
        elif chosen_option == 4:
            base_of_monsters.printAllSymptoms()
            base_of_monsters.chooseSymptoms()
            base_of_monsters.printAllMachtes()
        elif chosen_option == 5:
            base_of_curses.printCursesNames()
        elif chosen_option == 6:
            base_of_curses.printAllCurses()
        elif chosen_option == 7:
            base_of_curses.printAllSortedSymptoms()
        elif chosen_option == 8:
            base_of_curses.printAllSymptoms()
            base_of_curses.chooseSymptoms()
            base_of_curses.printAllMachtes()
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
