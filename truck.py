from datetime import timedelta


# Truck class. Instantiates truck objects
class Truck:
    # Initializes a truck object
    # O(1) constant time
    def __init__(self, package_id, departure_time):
        self.package_id = package_id
        self.departure_time = departure_time
        self.total_distance = 0
        self.packages_in_truck = []

    # Adds distance traveled
    # O(1) constant time
    def append_distance_traveled(self, distance):
        self.total_distance += distance

    # Returns distance traveled
    # O(1) constant time
    def return_distance_traveled(self):
        return self.total_distance

    # Adds packages to truck
    # O(1) constant time
    def append_packages_to_truck(self, packages):
        self.packages_in_truck.append(packages)

    # Returns packages in truck
    # O(1) constant time
    def return_packages_in_truck(self):
        return self.packages_in_truck


# Manually loads packages into the trucks
truck1 = Truck([13, 14, 15, 16, 19, 20, 1, 5, 7, 22, 29, 30, 34, 37, 39, 31], timedelta(hours=8, minutes=00))
truck2 = Truck([3, 18, 36, 38, 25, 28, 32, 4, 6, 8, 9, 10, 17, 21, 26, 40], timedelta(hours=9, minutes=5))
truck3 = Truck([2, 11, 12, 23, 24, 27, 33, 35], timedelta(hours=11, minutes=00))
