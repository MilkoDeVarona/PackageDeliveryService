import csv
from hashtable import HashTable
from packages import Package
hash_table = HashTable()


# Returns hash table
# O(1) constant time
def return_hash_table():
    return hash_table


# Takes address and package data from .csv files and adds them to the hash table
# O(n) linear time
def append_packages():
    def append_address_info():
        with open('csv/addresses.csv') as address_list:
            addresses = list(csv.reader(address_list, delimiter=','))
            return addresses
    address_info = append_address_info()
    with open('csv/packages.csv', encoding='utf-8-sig') as p:
        package_list = csv.reader(p, delimiter=',')
        for package in package_list:
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            delivery_deadline = package[5]
            weight = package[6]
            notes = package[7]
            status = 'At hub'
            departure_time = ''
            delivery_time = ''
            for a in address_info:
                if address == a[2].strip():
                    address_id = a[0]
                    break
            package = Package(package_id, address, city, state, zip_code, delivery_deadline, weight, notes, status,
                              departure_time, delivery_time, address_id)
            hash_table.insert(package_id, package)
    return hash_table
