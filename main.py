import filereader
from algo import check_total_distance_traveled, check_status_for_all_packages, check_status_for_specific_time, check_status_for_specific_package

# Name: Milko De Varona
# Student ID: 001529121


# Main function.
def main():
    print('\n\nWGU Parcel Service')
    print('-------------------------------------------')
    print("1: Check total distance traveled")
    print("2: Check status for all packages at EOD")
    print("3: Check status for all packages at a specific time")
    print("4: Check status for a specific package")
    print("5: Close program\n")
    user_choice = input("Choose a number to continue:\n")
    # Shows distance driven per truck and total distance in miles
    if user_choice == '1':
        check_total_distance_traveled()
    # Shows all packages after the day has ended
    if user_choice == '2':
        check_status_for_all_packages()
    # Shows all packages at a specific time
    if user_choice == '3':
        check_status_for_specific_time()
    # Shows a specific package status
    if user_choice == '4':
        check_status_for_specific_package()
    # Closes the program.
    if user_choice == '5':
        exit()


main()
