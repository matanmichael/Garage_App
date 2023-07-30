import os
import json
from prettytable import PrettyTable
import pprint

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def write_json_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"File '{file_path}' updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

def read_data_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in '{file_path}'.")
        return None

def add_car_to_json(file_path):
    data = read_data_from_json(file_path)
    if data is None:
        data = []

    car_id = 1
    if data:
        # Get the last car's ID and increment it by 1
        car_id = max(car["id"] for car in data) + 1

    car_make = input("Enter car make: ")
    car_model = input("Enter car model: ")
    car_year = int(input("Enter car year: "))

    new_car = {
        "id": car_id,
        "make": car_make,
        "model": car_model,
        "year": car_year
    }

    data.append(new_car)
    write_json_file(file_path, data)

def display_data_as_table(data):
    if not data:
        print("No data to display.")
        return
    table = PrettyTable()
    table.field_names = list(data[0].keys())
    for entry in data:
        table.add_row(entry.values())
    print(table)

def update_car_by_id(file_path, car_id):
    data = read_data_from_json(file_path)
    if data is not None:
        for car in data:
            if car.get("id") == car_id:
                print(f"Current details of car with ID {car_id}:")
                print("Make:", car["make"])
                print("Model:", car["model"])
                print("Year:", car["year"])

                car_make = input("Enter new make: ")
                car_model = input("Enter new model: ")
                car_year = int(input("Enter new year: "))

                car["make"] = car_make
                car["model"] = car_model
                car["year"] = car_year

                write_json_file(file_path, data)
                print(f"Car with ID {car_id} updated successfully.")
                return
        print(f"Error: Car with ID '{car_id}' not found in JSON data.")

def delete_object_by_id(file_path, object_id):
    data = read_data_from_json(file_path)
    if data is not None:
        deleted = False
        for item in data:
            if item.get("id") == object_id:
                data.remove(item)
                deleted = True
                break

        if deleted:
            write_json_file(file_path, data)
            print(f"Object with ID {object_id} deleted successfully.")
        else:
            print(f"Error: Object with ID '{object_id}' not found in JSON data.")

def display_car_by_id(file_path, car_id):
    data = read_data_from_json(file_path)
    if data is not None:
        for car in data:
            if car.get("id") == car_id:
                print("Car Details:")
                pprint.pprint(car, indent=4)
                return

        print(f"Error: Car with ID '{car_id}' not found in JSON data.")


def main(): 
    msg ="nothing selected"
    while(True):
        print(msg)
        print("c - add a new car to the list")
        print("r - display all car list")
        print("u - update a car status")
        print("d - delete a car by ID")
        print("f - display car by ID")
        print("X - exit")
        userChoice=input('what do you want to do?')
        clearConsole()
        if userChoice== "c":
            add_car_to_json("car_list.json")
            msg ="car added"
        elif userChoice== "r":
            data_to_show = read_data_from_json("car_list.json")
            display_data_as_table(data_to_show)
            msg ="car list display"
        elif userChoice== "u":
            update_car_by_id("car_list.json", car_id = int(input("Enter the ID of the car you want to update: ")))
            msg= "car status updated"
        elif userChoice== "d":
            delete_object_by_id("car_list.json", object_id = int(input("Enter the ID of the object you want to delete: ")))
            msg ="car removed from list"
        elif userChoice== "f":
            display_car_by_id("car_list.json", car_id = int(input("Enter the ID of the car you want to display: ")))
            msg ="car by id display"
        elif userChoice == "x":
            return print("program has closed")     
        else:
            print ("try again")

if __name__ == "__main__":
    main()

