from typing import Dict, List

from colors import Colors


class Object:
    def __init__(self, name: str, description: str = None, episodes: Dict[str, List[int]] = None):
        self.name = name
        self.description = description
        self.episodes = episodes
        self.abilities = None
        self.maintenance_methods = None
        self.destroy_methods = None

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

    def print_abilities(self):
        print(Colors.YELLOW + "Abilities:" + Colors.ENDC)
        if self.abilities is not None:
            for ability in self.abilities:
                print("  *  " + ability)
        else:
            print("  *  None found")

    def print_maintenance_methods(self):
        print(Colors.MAGENTA + "Maintenance Methods:" + Colors.ENDC)
        if self.maintenance_methods is not None:
            for method in self.maintenance_methods:
                print("  *  " + method)
        else:
            print("  *  None found...")

    def print_destroy_methods(self):
        print(Colors.MAGENTA + "Destroy Methods:" + Colors.ENDC)
        if self.destroy_methods is not None:
            for method in self.destroy_methods:
                print("  *  " + method)
        else:
            print("  *  None found...")

    def print_all(self):
        self.print_name()
        self.print_description()
        self.print_episodes()
        self.print_abilities()
        self.print_maintenance_methods()
        self.print_destroy_methods()
