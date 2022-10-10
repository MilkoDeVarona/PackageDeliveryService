# Package Class. Instantiates package objects
class Package:
    # Initializes a package object
    # O(1) constant time
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, weight,
                 notes, status, departure_time, delivery_time, address_id):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.address_id = address_id
        self.departure_time = departure_time
        self.delivery_time = delivery_time

    # Overwrites print(Package), otherwise it will print object reference
    # O(1) constant time
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % ( self.package_id, self.address, self.city, self.state, self.zip_code,self.delivery_deadline, self.weight, self.notes, self.status, self.address_id, self.departure_time, self.delivery_time)


# Updates package info
# O(1) constant time
def p_info(package, delivery_time, status):
    package_id = package.package_id
    address = package.address
    city = package.city
    state = package.state
    zip_code = package.zip_code
    delivery_deadline = package.delivery_deadline
    weight = package.weight
    notes = package.notes
    status = status
    address_id = package.address_id
    departure_time = package.departure_time
    delivery_time = delivery_time
    p = Package(package_id, address, city, state, zip_code, delivery_deadline, weight, notes, status, departure_time,
                delivery_time, address_id)
    return p
