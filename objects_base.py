from colors import Colors
from object import Object
from objects_data import ObjectAbilities, ObjectMaintenance, ObjectDestroyMethods


class ObjectsBase:
    def __init__(self):
        self.abilities = [ability for key, ability in list(ObjectAbilities.__dict__.items())
                          if not key.startswith("__")]
        self.maintenance_methods = [method for key, method in list(ObjectMaintenance.__dict__.items())
                                    if not key.startswith("__")]

        self.colt_of_colt = Object("Colt of Colt", description="Colt made by Samuel Colt in 1835, when Halley's Comet "
                                                               "was overhead and the same night those men died "
                                                               "at the Alamo. He made it for a hunter along with "
                                                               "13 bullets. Bullets can be crafted for this gun.",
                                   episodes={"S01": [20, 21, 22], "S02": [1, 22], "S03": [4]})
        self.colt_of_colt.abilities = [ObjectAbilities.can_kill_anything]

        self.charm_against_demons = Object("Charm against demons", description="Fend off possessions. Stops a demon "
                                                                               "from taking a person as a host.",
                                           episodes={"S02": [14]})
        self.charm_against_demons.abilities = [ObjectAbilities.unables_possessions]

        self.demon_killing_knife = Object("Demon killing knife", description="Can literally kill demons, "
                                                                             "not get them back to hell.",
                                          episodes={"S03": [1]})
        self.demon_killing_knife.abilities = [ObjectAbilities.can_kill_demons]

        self.lucky_rabbits_foot = Object("Lucky rabbits foot",
                                         description="Person, who touches it becomes incredibly lucky. If another "
                                                     "person touches it, the previous one becomes incredibly unlucky "
                                                     "and dies in a week. To make one, you have to cut rabbits foot in "
                                                     "a cemetery under a full moon on a Friday the 13th.",
                                         episodes={"S03": [3]})
        self.lucky_rabbits_foot.abilities = [ObjectAbilities.grants_incredible_luck]
        self.lucky_rabbits_foot.destroy_methods = [ObjectDestroyMethods.burn_it]

        self.objects = [object for object in self.__dict__.values() if isinstance(object, Object)]

    def print_objects_names(self):
        sorted_objects = sorted([object.name for object in self.objects])
        print(Colors.RED + Colors.BOLD + "All objects:" + Colors.ENDC)
        for object in sorted_objects:
            print(" *  " + object)

    def print_all_objects(self):
        for object in self.objects:
            object.print_all()
