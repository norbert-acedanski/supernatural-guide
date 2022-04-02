import traceback
import time
import re
from MonsterBase import MonsterBase
from CursesBase import CursesBase
from Colors import bcolors

def chooseOption():
    choosenOption = 1
    while choosenOption != 0:
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
        choosenOptionStr = input()
        choosenOptionStr = re.sub('[a-zA-Z,.&^%$#@?|/:;"_=]', '', choosenOptionStr)
        if choosenOptionStr.isdigit():
            choosenOption = int(choosenOptionStr)
        else:
            choosenOption = -1
        if choosenOption == 1:
            baseOfMonsters.printMonstersNames()
        elif choosenOption == 2:
            baseOfMonsters.printAllMonsters()
        elif choosenOption == 3:
            baseOfMonsters.printAllSortedSymptoms()
        elif choosenOption == 4:
            baseOfMonsters.printAllSymptoms()
            baseOfMonsters.chooseSymptoms()
            baseOfMonsters.printAllMachtes()
        elif choosenOption == 5:
            baseOfCurses.printCursesNames()
        elif choosenOption == 6:
            baseOfCurses.printAllCurses()
        elif choosenOption == 7:
            baseOfCurses.printAllSortedSymptoms()
        elif choosenOption == 8:
            baseOfCurses.printAllSymptoms()
            baseOfCurses.chooseSymptoms()
            baseOfCurses.printAllMachtes()
        elif choosenOption == 0:
            print("Thank you for playing with this project!")
        else:
            print("Choose option from the list...")
            pass

try:
    baseOfMonsters = MonsterBase()
    baseOfCurses = CursesBase()
    chooseOption()

except ValueError as ve:
    print(traceback.format_exc())

except Exception as e:
    print(traceback.format_exc())