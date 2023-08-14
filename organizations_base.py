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
                                                                "broke the fourth wall in their compound in S09E04. "
                                                                "They have more power than the Coven of Witches. "
                                                                "Eileen Leahy is a granddaughter of one of the Man of "
                                                                "Letters members (according to S11E11).",
                                  episodes={"S08": [12, 13, 14, 16, 20, 22, 23],
                                            "S09": [4, 5, 6, 7, 9, 11, 14, 16, 17],
                                            "S10": [3, 8, 11, 12, 17, 18, 21, 22], "S11": [4, 7, 8, 11]})
    man_of_letters.knowledge = [OrganizationKnowledge.time_travel, OrganizationKnowledge.demon_killing_knife,
                                OrganizationKnowledge.haitian_symbol_for_speaking_to_the_dead,
                                OrganizationKnowledge.knights_of_hell, OrganizationKnowledge.drakopoolos_journal,
                                OrganizationKnowledge.summoning_of_zeus, OrganizationKnowledge.irregular_jinns,
                                OrganizationKnowledge.demonic_possessions, OrganizationKnowledge.oz,
                                OrganizationKnowledge.monitoring_of_apocalyptic_events,
                                OrganizationKnowledge.inuit_magic, OrganizationKnowledge.extinct_languages,
                                OrganizationKnowledge.angel_weakening, OrganizationKnowledge.angel_leaving_its_vessel,
                                OrganizationKnowledge.the_inner_workings_of_angels,
                                OrganizationKnowledge.dishonored_and_forgotten,
                                OrganizationKnowledge.werewolf_transgenderism, OrganizationKnowledge.symbology,
                                OrganizationKnowledge.anti_tracking_box_and_symbols,
                                OrganizationKnowledge.occult_families, OrganizationKnowledge.styne_family,
                                OrganizationKnowledge.werther_project, OrganizationKnowledge.exorcisms,
                                OrganizationKnowledge.whispers, OrganizationKnowledge.nachzehrers,
                                OrganizationKnowledge.pre_biblical_lore, OrganizationKnowledge.zanna_lore]

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

    the_styne_family = Organization("The Styne family",
                                    description="A family of multi-generational, centuries-old wrong. They used spells "
                                                "to create disease, destabilize markets ad even helped the Nazis "
                                                "before they came into power, profited from all of them. They made "
                                                "a ton mopping up the Black Plague, started the Hundred Years War. "
                                                "All of the spells came from the book of unspeakable evil - Book of "
                                                "the Damned. They lost it about 100 years ago. Members of the family "
                                                "are stronger, more resistant to everything. Styne family specializes "
                                                "in bioengineering and body enhancements. The name of the original "
                                                "family was altered out of necessity. Before the change it was called "
                                                "Frankenstein. The family is over 1000 years old. Dean killed a lot of "
                                                "them in S10E22.",
                                    episodes={"S10": [18, 21, 22]})

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
