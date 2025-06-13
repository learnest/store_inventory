from src.items import Product,Inventory

def add_product(data_to_save,inventory: Inventory):
    while True:
        name = input("Item name: ")
        sku = input("Item registration code: ")
        quantity = int(input("Current quantity: "))
        price = int(input("Price: "))

        # Create the Product object
        item = Product(sku, name, quantity, price)

        # Add it to the inventory using sku as the key
        inventory.item_list[sku] = item
        print(f"Item '{name}' with SKU: '{sku}' added successfully!")
        data_to_save[sku] = item.write_to_dict()
        # Optionally ask if the user wants to add another item
        continue_adding = input("Do you want to add another item? (y/n): ")
        if continue_adding.lower() != 'y':
            break

    return data_to_save
    

def show_inventory(data, inventory:Inventory):
    view_option = input("Choose which data you want to see? From (d)atabase or (m)emory: ")
    if view_option.lower() == 'm': 
        print("Showing data from memory: ")
        for n, (sku, product) in enumerate(inventory.item_list.items(), start=1):
            print(f"{n}. SKU: {sku} - Item Name: {product.name} | Current qty: {product.quantity} -  Current price: Rp {product.price}")
    elif view_option.lower() == 'd':
        for n, (sku, product_details) in enumerate(data.items(),start=1):
            print(f"{n}. SKU:{sku}: {product_details['name']} | Quantity: {product_details['quantity']} | Price: {product_details['price']}")
    else:
        raise ValueError("PRESS 'd' to view data in saved database, 'm' to view curent unsaved database")

    
def delete_product(data):
    print("Deleting product from database")
    for n, (sku, product_details) in enumerate(data.items(), start=1):
        print(f"{n}. {sku} - {product_details["name"]}")
    product_sku = list(data.keys())
    data_to_delete = int(input("Choose which product from database  you want to delete: ")) - 1
    
    try:
        if data_to_delete < 0 or data_to_delete > len(data):
            raise IndexError("ERROR: Input out of range. Please input within the range of option")
        else:
            delete_index = product_sku[data_to_delete]
            get_deleted_product = data[delete_index]['name']
            get_deleted_sku = data[delete_index]['sku']
            del data[delete_index]
            print(f"You removed {get_deleted_sku} - {get_deleted_product} from the database")
            
    except ValueError:
        print("Please put number for the option")

def edit_product(data):
    print("Editing product from database")
    for n, (sku, product_details) in enumerate(data.items(), start=1):
        print(f"{n}. {sku} - {product_details["name"]}")
    product_sku = list(data.keys())
    data_to_edit = int(input("Choose which product from database you want to edit: ")) - 1
    try:
        if data_to_edit < 0 or data_to_edit > len(data):
            raise IndexError("ERROR: Input out of range. Please input within the range of option")
        else:
            while True:
                edit_index = product_sku[data_to_edit]
                print(f"You want to edit {edit_index}")
                print("1. Item SKU")
                print("2. Item name")
                print("3. Item current stock")
                print("4. Item price")
                print("5. Finish editing")
                user_option = int(input("Choose which entry you want to edit: "))
                if user_option == 1:
                    new_sku = input("New SKU: ")
                    data[new_sku] = data.pop(edit_index)
                    data[new_sku]["sku"] = new_sku
                elif user_option == 2:
                    data[edit_index]["name"] = input("Please input new name")
                elif user_option == 3:
                    data[edit_index]["quantity"] = input("Please input new quantity/stock")
                elif user_option == 4:
                    data[edit_index]["price"] = input("Please input new price")
                elif user_option == 5:
                    print("Finished editing. Now back to main menu")
                    break
    except ValueError:
        print("Please put number for the option")