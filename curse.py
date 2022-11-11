from typing import Dict, List

from colors import Colors


class Curse:
    def __init__(self, name: str, description: str = None, episodes: Dict[str, List[int]] = None):
        self.name = name
        self.description = description
        self.episodes = episodes
        self.clues = None
        self.disable_methods = None

    def print_name(self):
        print(Colors.GREEN + "\n" + self.name + ":" + Colors.ENDC)

    def print_description(self):
        if self.description is not None:
            print("   " + self.description)

    def print_episodes(self):
        if self.episodes is not None:
            print(Colors.BLUE + "Show seeings: " + Colors.ENDC)
            for season, episodes in self.episodes.items():
                episodes_str = [str(episode) for episode in episodes]
                print(f"   {season}: " + ", ".join(episodes_str))
    
    def print_clues_base(self):
        print(Colors.YELLOW + "Clues:" + Colors.ENDC)
        if self.clues is not None:
            for clue in self.clues:
                print("  *  " + clue)
        else:
            print("  *  None found...")

    def print_disable_methods(self):
        print(Colors.MAGENTA + "Disable Methods:" + Colors.ENDC)
        if self.disable_methods is not None:
            for method in self.disable_methods:
                print("  *  " + method)
        else:
            print("  *  None found...")

    def print_all(self):
        self.print_name()
        self.print_description()
        self.print_episodes()
        self.print_clues_base()
        self.print_disable_methods()
