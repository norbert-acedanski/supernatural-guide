from typing import Dict, List

from colors import Colors


class Organization:
    def __init__(self, name: str, description: str = None, episodes: Dict[str, List[int]] = None):
        self.name = name
        self.description = description
        self.episodes = episodes
        self.knowledge = None

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
        print(Colors.YELLOW + "Knowledge:" + Colors.ENDC)
        if self.knowledge is not None:
            for knowledge in self.knowledge:
                print("  »  " + knowledge)
        else:
            print("  »  None found")
