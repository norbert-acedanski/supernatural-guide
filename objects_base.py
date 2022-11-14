from colors import Colors
from object import Object
from objects_data import ObjectAbilities, ObjectMaintenance


class ObjectsBase:
    def __init__(self):
        self.abilities = [ability for key, ability in list(ObjectAbilities.__dict__.items())
                          if not key.startswith("__")]
        self.maintenance_methods = [method for key, method in list(ObjectMaintenance.__dict__.items())
                                    if not key.startswith("__")]

        self.colt_of_colt = Object("Colt of Colt", description="Colt made by Samuel Colt in 1835, when Halley's Comet "
                                                               "was overhead and the same night those men died "
                                                               "at the Alamo. He made it for a hunter along with "
                                                               "13 bullets.",
                                   episodes={"S01": [20, 21, 22], "S02": [1]})
        self.colt_of_colt.abilities = [ObjectAbilities.can_kill_anything]

        self.objects = [object for object in self.__dict__.values() if isinstance(object, Object)]

    def print_objects_names(self):
        sorted_objects = sorted([object.name for object in self.objects])
        print(Colors.RED + Colors.BOLD + "All objects:" + Colors.ENDC)
        for object in sorted_objects:
            print(" *  " + object)

    def print_all_objects(self):
        for object in self.objects:
            object.print_all()


