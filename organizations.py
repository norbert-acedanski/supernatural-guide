from organization import Organization
from organizations_data import OrganizationKnowledge


class OrganizationsBase:
    man_of_letters = Organization("Man of letters", description="An organization, that stores knowledge "
                                                                "of the supernatural. The crest of Man of Letters is "
                                                                "The Aquarian Star. It represents great magical power. "
                                                                "According to Henry it stood at the gates of "
                                                                "Atlantis itself.", episodes={"S18": [12]})
    man_of_letters.knowledge = [OrganizationKnowledge.time_travel, OrganizationKnowledge.demon_killing_knife,
                                OrganizationKnowledge.haitian_symbol_for_speaking_to_the_dead,
                                OrganizationKnowledge.knights_of_hell]
