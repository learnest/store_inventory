from src.db_utils import read_json,write_json,database_init
from src.items import Product,Inventory
from src.inventory_system import add_product,show_inventory,delete_product,edit_product
    
def exit_prog(data,data_to_save):
    data.update(data_to_save)
    write_json('database.json', data)
    exit()

def main_menu():
    print("1. Add item/product")
    print("2. Browse currently available items/products")
    print("3. Edit current product")
    print("4. Delete product")
    print("5. Exit program")
    user_option = int(input("Choose which option:"))
    match user_option:
        case 1:
           add_product(data,inventory)
           print("Back to main menu")
        case 2:
            show_inventory(data, inventory)
            print("Back to main menu")
        case 3:
            edit_product(data)
            print("Back to main menu")
        case 4:
           delete_product(data)
           print("Back to main menu")
        case 5:
            exit_prog(data,data_to_save)
        case _:
            raise IndexError("")
    
if __name__ == '__main__':
    inventory = Inventory()
    database_init()
    data = read_json(filename='database.json')
    data_to_save = {}
    while True:

        main_menu()
