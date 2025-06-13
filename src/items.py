class Product:
    def __init__(self, sku:str, name:str, quantity:int, price:int):
        self.sku = sku
        self.name = name
        self.quantity = quantity
        self.price = price          # Currency is IDR
        
        
    def quantity_sanity_check(self):
        if self.quantity < 0:
            raise ValueError("Quantity cannot be lower than zero")
            
    def price_sanity_check(self):
        if self.price < 0:
            raise ValueError("Price (in IDR) cannot be lower than zero")
    
    def __repr__(self):
        return f"SKU:{self.sku} -  Item name:{self.name} | Current stock: {self.quantity}, Current price: Rp {self.price}"
    
    def write_to_dict(self):
        return {
                "sku":self.sku,
                "name":self.name,
                "quantity":self.quantity,
                "price":self.price
                }

class Inventory:
    def __init__(self):
        self.item_list = {}