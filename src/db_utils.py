import json
import os

def database_init():
    print("Checking if database exist...")
    if not os.path.exists('database.json'):
        print("Database not found")
        print("Creating new database...")
        with open('database.json', 'w') as file:
            json.dump({}, file, indent=4)
        print("Database created successfully!")
    else:
        print("Database exist")
        print("Loading database...")

def write_json(filename, data):
    with open(filename,'w') as file:
        json.dump(data, file, indent=4)
        
def read_json(filename):
    with open(filename, 'r') as file:
        save_data = json.load(file)
    return save_data
