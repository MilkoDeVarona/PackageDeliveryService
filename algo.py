import csv
import datetime
import filereader
from filereader import return_distance_info
from packages import p_info
from truck import truck1, truck2, truck3
hash_table_1 = filereader.append_packages()
hash_table_2 = filereader.return_hash_table()


# Finds distance between two given addresses using distance information from function return_distance_info()
# O(1) constant time
def return_addresses_distance(x, y):
    d = return_distance_info()
    distance = d[x][y]
    if distance == '':
        distance = d[y][x]
    return float(distance)


# Compares and finds the smallest distance between two addresses on a list using information from
# function return_addresses_distance(). Returns the next closest package
# O(n^2) quadratic time
def smallest_distance(a, packages_addresses):
    small_distance = 0
    for c, first_value in enumerate(packages_addresses):
        for second_value in packages_addresses[c + 1:]:
            address_one_distance = return_addresses_distance(int(a), int(first_value.address_id))
            address_two_distance = return_addresses_distance(int(a), int(second_value.address_id))
            if small_distance == 0:
                small_distance = address_one_distance
            if address_one_distance < small_distance and address_one_distance < address_two_distance:
                small_distance = address_one_distance
            if address_two_distance < small_distance and address_two_distance < address_one_distance:
                small_distance = address_two_distance
    for c, p in enumerate(packages_addresses):
        if return_addresses_distance(int(a), int(packages_addresses[c].address_id)) == small_distance:
            return p


# Arranges packages on the truck by using function smallest_distance(). Adds returned package to a new list. Sets
# current address to the returned package and removes it from the truck. Returns the new list after all packages
# have been run through.
# O(n) linear time
def order_by_smallest_distance(package_addresses):
    current_address = 0
    ordered_packages = []
    while len(package_addresses) > 0:
        package = smallest_distance(current_address, package_addresses)
        current_address = package.address_id
        ordered_packages.append(package)
        package_addresses.remove(package)
        if len(package_addresses) <= 1:
            ordered_packages.append(package_addresses[0])
            break
    return ordered_packages


# Orders packages in the trucks by smallest distance
# O(n) linear time
def load_by_distance():
    for p_id in truck1.package_id:
        p = hash_table_1.search(p_id)
        p.departure_time = truck1.departure_time
        truck1.append_packages_to_truck(p)
    truck1.packages_in_truck = (order_by_smallest_distance(truck1.return_packages_in_truck()))
    for p_id in truck2.package_id:
        p = hash_table_1.search(p_id)
        p.departure_time = truck2.departure_time
        truck2.append_packages_to_truck(p)
    truck2.packages_in_truck = (order_by_smallest_distance(truck2.return_packages_in_truck()))
    for p_id in truck3.package_id:
        p = hash_table_1.search(p_id)
        p.departure_time = truck3.departure_time
        truck3.append_packages_to_truck(p)
    truck3.packages_in_truck = (order_by_smallest_distance(truck3.return_packages_in_truck()))
    trucks = [truck1, truck2, truck3]
    return trucks


# Transports packages and adds distance traveled and time spent
# O(n^2) quadratic time
def transport_packages(trucks, hashtable):
    for c, t in enumerate(trucks):
        packages_in_truck = t.packages_in_truck
        truck_departure_time = t.departure_time
        for p in packages_in_truck:
            hashtable.insert(p.package_id, p_info(p, truck_departure_time, 'En route'))
        for c2, p in enumerate(packages_in_truck):
            if c2 > 0:
                miles_traveled = return_addresses_distance(int(packages_in_truck[c2 - 1].address_id), int(packages_in_truck[c2].address_id)) / 18
                time_between_places = datetime.timedelta(hours=miles_traveled)
                truck_departure_time = truck_departure_time + time_between_places
                t.append_distance_traveled(return_addresses_distance(int(packages_in_truck[c2 - 1].address_id), int(packages_in_truck[c2].address_id)))
                hashtable.insert(packages_in_truck[c2].package_id, p_info(p, truck_departure_time, 'Delivered'))
                continue
            miles_traveled = return_addresses_distance(0, int(packages_in_truck[c2].address_id)) / 18
            time_between_places = datetime.timedelta(hours=miles_traveled)
            truck_departure_time = truck_departure_time + time_between_places
            t.append_distance_traveled(return_addresses_distance(0, int(packages_in_truck[c2].address_id)))
            hashtable.insert(packages_in_truck[c2].package_id, p_info(p, truck_departure_time, 'Delivered'))
            remaining = hashtable.search(packages_in_truck[-1].package_id)
            if remaining.status == 'Delivered':
                t.append_distance_traveled(return_addresses_distance(0, int(packages_in_truck[-1].address_id)))
                truck_departure_time = truck_departure_time + time_between_places
    return trucks


# ________________________________________________________________________________________________

# Displays total miles driven per truck and total miles driven for the three trucks
# O(n) linear time
def check_total_distance_traveled():
    trucks = load_by_distance()
    transport_packages(trucks, hash_table_2)
    total = trucks[0].return_distance_traveled() + trucks[1].return_distance_traveled() + trucks[
        2].return_distance_traveled()
    print("------------------------------------------------------\n")
    print("Truck 1: total miles " + str(trucks[0].return_distance_traveled()))
    print("Truck 2: total miles " + str(trucks[1].return_distance_traveled()))
    print("Truck 3: total miles " + str(trucks[2].return_distance_traveled()))
    print("\nTotal Distance: " + str(total))
    print("\n------------------------------------------------------")


# Displays status of all packages at the end of day
# O(n) linear time
def check_status_for_all_packages():
    trucks = load_by_distance()
    transport_packages(trucks, hash_table_2)
    for p in range(1, 41):
        package = hash_table_2.search(p)
        # Changes package 9 address
        package_9 = hash_table_1.search(9)
        package_9.address = '410 S State St.'
        package_9.city = 'Salt Lake City'
        package_9.state = 'UT'
        package_9.zip_code = '84111'
        package_9.address_id = 19
        print("\nPACKAGE ID:", package.package_id)
        print("ADDRESS:", package.address + ",", package.city + ",", package.state + "", package.zip_code)
        print("WEIGHT:", package.weight)
        print("DEPARTURE TIME:", package.departure_time)
        print("DELIVERY TIME:", package.delivery_time)
        print("DELIVERY DEADLINE:", package.delivery_deadline)
        print("STATUS:", package.status)
        print("\n------------------------------------------------------")


# Displays status of all packages at a specified time
# O(n) linear time
def check_status_for_specific_time():
    trucks = load_by_distance()
    time_period = input("Choose a time to view the status of all packages using 'HH MM':\n")
    (h, m) = time_period.split(' ')
    user_chosen_time = datetime.timedelta(hours=int(h), minutes=int(m))
    transport_packages(trucks, hash_table_2)
    for p in range(1, 41):
        package = hash_table_2.search(p)
        delivery_time = package.delivery_time
        departure_time = package.departure_time
        if user_chosen_time < delivery_time and user_chosen_time < departure_time:
            package.status = 'At hub'
        if user_chosen_time < delivery_time and user_chosen_time >= departure_time:
            package.status = 'En route'
        if user_chosen_time >= delivery_time:
            package.status = 'Delivered'
        # Handles package 9 change of address after 10:20 am
        if user_chosen_time >= datetime.timedelta(hours=10, minutes=20):
            package_9 = hash_table_1.search(9)
            package_9.address = '410 S State St.'
            package_9.city = 'Salt Lake City'
            package_9.state = 'UT'
            package_9.zip_code = '84111'
            package_9.address_id = 19
        print("\nPACKAGE ID:", package.package_id)
        print("ADDRESS:", package.address + ",", package.city + ",", package.state + "", package.zip_code)
        print("WEIGHT:", package.weight)
        print("DEPARTURE TIME:", package.departure_time)
        print("DELIVERY TIME:", package.delivery_time)
        print("DELIVERY DEADLINE:", package.delivery_deadline)
        print("STATUS:", package.status)
        print("\n------------------------------------------------------")


# Displays status of a specified package at a specified time
# O(n) linear time
def check_status_for_specific_package():
    trucks = load_by_distance()
    package_id = input("Choose package ID:\n")
    time_period = input("Choose a time to view the status of the package using 'HH MM':\n")
    (h, m) = time_period.split(' ')
    user_chosen_time = datetime.timedelta(hours=int(h), minutes=int(m))
    transport_packages(trucks, hash_table_2)
    package = hash_table_2.search(int(package_id))
    delivery_time = package.delivery_time
    departure_time = package.departure_time
    if user_chosen_time < delivery_time and user_chosen_time < departure_time:
        package.status = 'At hub'
    if user_chosen_time < delivery_time and user_chosen_time >= departure_time:
        package.status = 'En route'
    if user_chosen_time >= delivery_time:
        package.status = 'Delivered'
    # Handles package 9 change of address  after 10:20 am
    if user_chosen_time >= datetime.timedelta(hours=10, minutes=20):
        package_9 = hash_table_1.search(9)
        package_9.address = '410 S State St.'
        package_9.city = 'Salt Lake City'
        package_9.state = 'UT'
        package_9.zip_code = '84111'
        package_9.address_id = 19
    print("------------------------------------------------------\n")
    print("PACKAGE ID:", package.package_id)
    print("ADDRESS:", package.address + ",", package.city + ",", package.state + "", package.zip_code)
    print("WEIGHT:", package.weight)
    print("DEPARTURE TIME:", package.departure_time)
    print("DELIVERY TIME:", package.delivery_time)
    print("DELIVERY DEADLINE:", package.delivery_deadline)
    print("STATUS:", package.status)
    print("\n------------------------------------------------------")
