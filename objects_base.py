from colors import Colors
from object import Object
from objects_data import ObjectAbilities, ObjectMaintenance, ObjectDestroyMethods, JohnWinchesterJournal


class ObjectsBase:
    def __init__(self):
        self.abilities = [ability for key, ability in list(ObjectAbilities.__dict__.items())
                          if not key.startswith("__")]
        self.maintenance_methods = [method for key, method in list(ObjectMaintenance.__dict__.items())
                                    if not key.startswith("__")]

        # SEASON 1:

        # TODO: Watch each episode until S04E18 that contains John's journal
        # List of episodes, that the journal appears in:
        # https://supernatural.fandom.com/wiki/John_Winchester%27s_Journal#Appearances
        self.john_winchesters_journal = Object("John Winchester's Journal",
                                               description="A journal of John Winchester, that contains a lot "
                                                           "information about monsters in Supernatural Universe.",
                                               episodes={"S01": [], "S04": [19]})
        self.john_winchesters_journal._information = {"S04E19": JohnWinchesterJournal.entry_about_johns_other_son}

        self.colt_of_colt = Object("Colt of Colt", description="Colt made by Samuel Colt in 1835, when Halley's Comet "
                                                               "was overhead and the same night those men died "
                                                               "at the Alamo. He made it for a hunter along with "
                                                               "13 bullets. Bullets can be crafted for this gun.",
                                   episodes={"S01": [20, 21, 22], "S02": [1, 22], "S03": [4, 5, 9]})
        self.colt_of_colt.abilities = [ObjectAbilities.can_kill_anything]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 2:

        self.charm_against_demons = Object("Charm against demons", description="Fend off possessions. Stops a demon "
                                                                               "from taking a person as a host.",
                                           episodes={"S02": [14], "S03": [12]})
        self.charm_against_demons.abilities = [ObjectAbilities.unables_possessions]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 3:

        self.demon_killing_knife = Object("Demon killing knife", description="Can literally kill demons, "
                                                                             "not get them back to hell. "
                                                                             "Cannot kill certain kinds of demons.",
                                          episodes={"S03": [1, 9, 16], "S04": [1, 9, 20, 22], "S05": [1]})
        self.demon_killing_knife.abilities = [ObjectAbilities.can_kill_demons, ObjectAbilities.cannot_kill_angels]

        self.lucky_rabbits_foot = Object("Lucky rabbits foot",
                                         description="Person, who touches it becomes incredibly lucky. If another "
                                                     "person touches it, the previous one becomes incredibly unlucky "
                                                     "and dies in a week. To make one, you have to cut rabbits foot in "
                                                     "a cemetery under a full moon on a Friday the 13th.",
                                         episodes={"S03": [3]})
        self.lucky_rabbits_foot.abilities = [ObjectAbilities.grants_incredible_luck]
        self.lucky_rabbits_foot.destroy_methods = [ObjectDestroyMethods.burn_it]

        self.sleep_potion = Object("Sleep Potion", description="Made of African Dream Root. Was use by shaman and "
                                                               "medicine men for centuries. It is used for "
                                                               "dream-walking - entering another person's dreams.",
                                   episodes={"S03": [10]})
        self.sleep_potion.abilities = [ObjectAbilities.can_make_a_person_sleep_for_days,
                                       ObjectAbilities.brings_back_dreams_for_those_that_dont_have_them,
                                       ObjectAbilities.gives_people_control_over_dreams]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 4:

        self.sigint_against_angels = Object("Sigint against angels", description="Sigint made with blood, that can "
                                                                                 "send angels back to heaven. "
                                                                                 "Can be used to send back a specific "
                                                                                 "angel type.",
                                            episodes={"S04": [10, 22]})
        self.sigint_against_angels.abilities = [ObjectAbilities.can_send_angels_back_to_heaven]

        self.angel_grace = Object("Angel grace", description="A power source for an angel", episodes={"S04": [10]})
        self.angel_grace.abilities = [ObjectAbilities.can_appear_as_falling_meteor,
                                      ObjectAbilities.the_place_it_hits_is_not_destroyed_but_flourishes,
                                      ObjectAbilities.can_kill_entities_when_reconnecting_with_an_angel]

        self.reaper_imprison_sigint = Object("Reaper imprison sigint", description="Sigint, that can trap a reaper.",
                                             episodes={"S04": [15]})
        self.reaper_imprison_sigint.abilities = [ObjectAbilities.traps_a_reaper]

        self.angel_protection_sigint = Object("Angel protection sigint", description="Angels can't get past it when "
                                                                                     "the place is marked with it.",
                                              episodes={"S04": [15]})
        self.angel_protection_sigint.abilities = [ObjectAbilities.angels_cant_get_past_it]

        self.angel_blade = Object("Angel blade", description="A triangular, silvery blade, that each angel has.",
                                  episodes={"S04": [16], "S05": [1]})
        self.angel_blade.abilities = [ObjectAbilities.can_kill_angels]

        self.lucifers_cage = Object("Lucifer's Cage", description="A prison build specifically to contain archangelic "
                                                                  "powers (not seen yet).")
        self.lucifers_cage.abilities = [ObjectAbilities.traps_an_archangel]

        # ---------------------------------------------- ALL EPISODES DONE ---------------------------------------------

        # SEASON 5:

        self.sword_of_archangel_michael = Object("Sword of Archangel Michael", description="A vessel, that Archangel "
                                                                                           "Michael possesses - a very "
                                                                                           "special person, that can "
                                                                                           "hold archangels power.",
                                                 episodes={"S05": [1]})

        self.objects = [obj for obj in self.__dict__.values() if isinstance(obj, Object)]

    def print_objects_names(self):
        sorted_objects = sorted([obj.name for obj in self.objects])
        print(Colors.RED + Colors.BOLD + "All objects:" + Colors.ENDC)
        for obj in sorted_objects:
            print(" *  " + obj)

    def print_all_objects(self):
        for obj in self.objects:
            obj.print_all()
