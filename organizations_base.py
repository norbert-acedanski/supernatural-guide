from colors import Colors
from organization import Organization
from organizations_data import OrganizationKnowledge


class OrganizationsBase:
    man_of_letters = Organization("Man of Letters", description="An organization, that stores knowledge "
                                                                "of the supernatural. The crest of Man of Letters is "
                                                                "The Aquarian Star. It represents great magical power. "
                                                                "According to Henry it stood at the gates of "
                                                                "Atlantis itself. They have a base in Lebanon, Kansas, "
                                                                "that contains a library of books about supernatural. "
                                                                "One of the members was L. Franck Baum, the writer. "
                                                                "He wrote books about his daughter in Ozz. Charlie "
                                                                "broke the fourth wall in their compound in S09E04.",
                                  episodes={"S08": [12, 13, 14, 16, 20, 22, 23], "S09": [4, 5]})
    man_of_letters.knowledge = [OrganizationKnowledge.time_travel, OrganizationKnowledge.demon_killing_knife,
                                OrganizationKnowledge.haitian_symbol_for_speaking_to_the_dead,
                                OrganizationKnowledge.knights_of_hell, OrganizationKnowledge.drakopoolos_journal,
                                OrganizationKnowledge.summoning_of_zeus, OrganizationKnowledge.irregular_jinns,
                                OrganizationKnowledge.demonic_possessions, OrganizationKnowledge.oz,
                                OrganizationKnowledge.monitoring_of_apocalyptic_events,
                                OrganizationKnowledge.inuit_magic]

    the_judah_initiative = Organization("The Judah initiative", description="They were active during WW2. A group of "
                                                                            "rabbis that were good saboteurs. "
                                                                            "They knew Man of Letters. It was founded "
                                                                            "to fight The Thule Society.",
                                        episodes={"S08": [13]})
    the_judah_initiative.knowledge = [OrganizationKnowledge.golem_magic]

    the_thule_society = Organization("The Thule Society", description="Nazi necromancers. A secret fraternity, that "
                                                                      "sponsored the early days of the Nazi Party.",
                                     episodes={"S08": [13]})
    the_thule_society.knowledge = [OrganizationKnowledge.immortal_life]

    def __init__(self):
        self.organizations = [organization for organization in self.__dict__.values() if isinstance(organization,
                                                                                                    Organization)]

    def print_organizations_names(self):
        sorted_organizations = sorted([organization.name for organization in self.organizations])
        print(Colors.RED + Colors.BOLD + "All organizations:" + Colors.ENDC)
        for organization in sorted_organizations:
            print(" *  " + organization)

    def print_all_organizations(self):
        for organization in self.organizations:
            organization.print_all()
