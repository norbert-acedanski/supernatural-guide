from organization import Organization
from organizations_data import OrganizationKnowledge


class OrganizationsBase:
    man_of_letters = Organization("Man of Letters", description="An organization, that stores knowledge "
                                                                "of the supernatural. The crest of Man of Letters is "
                                                                "The Aquarian Star. It represents great magical power. "
                                                                "According to Henry it stood at the gates of "
                                                                "Atlantis itself. They have a base in Lebanon, Kansas, "
                                                                "that contains a library of books about supernatural.",
                                  episodes={"S18": [12, 13, 14, 16]})
    man_of_letters.knowledge = [OrganizationKnowledge.time_travel, OrganizationKnowledge.demon_killing_knife,
                                OrganizationKnowledge.haitian_symbol_for_speaking_to_the_dead,
                                OrganizationKnowledge.knights_of_hell, OrganizationKnowledge.drakopoolos_journal,
                                OrganizationKnowledge.summoning_of_zeus]

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