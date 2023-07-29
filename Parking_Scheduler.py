def display_parked_vehicles(vehicles):
    if not vehicles:
        print("No vehicles are currently parked.")
    else:
        print("List of Parked Vehicles:")
        for idx, vehicle in enumerate(vehicles, start=1):
            print(f"{idx}. {vehicle['type']} - {vehicle['plate']}")


def add_new_vehicle(vehicles):
    vehicle_type = input("Enter the type of vehicle (e.g., car, bike, truck): ")
    plate_number = input("Enter the vehicle plate number: ")
    vehicle = {'type': vehicle_type, 'plate': plate_number}
    vehicles.append(vehicle)
    print("Vehicle added successfully.")


def remove_vehicle(vehicles):
    display_parked_vehicles(vehicles)
    if not vehicles:
        return

    try:
        choice = int(input("Enter the index of the vehicle to remove: "))
        if 1 <= choice <= len(vehicles):
            removed_vehicle = vehicles.pop(choice - 1)
            print(f"{removed_vehicle['type']} - {removed_vehicle['plate']} removed from the parking lot.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


def main():
    vehicles = []

    while True:
        print("PARKING SCHEDULER")
        print("1. Display Parked Vehicles")
        print("2. Add New Vehicle")
        print("3. Remove Vehicle from Parking Lot")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_parked_vehicles(vehicles)
        elif choice == '2':
            add_new_vehicle(vehicles)
        elif choice == '3':
            remove_vehicle(vehicles)
        elif choice == '0':
            print("Thank you for using the Parking Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
