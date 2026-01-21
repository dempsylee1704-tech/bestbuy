class Product:


    def __init__(self, name, price, quantity):
        if name.strip() == "":
            raise ValueError("Name can't be empty!")
        if price < 0:
            raise ValueError("Price can't be negativ")
        if quantity < 0:
            raise ValueError("Quantity can't be negativ")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity can't be negativ")
        self.quantity = quantity
        if quantity == 0:
            self.active = False


    def is_active(self) -> bool:
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity) -> float:
        if not self.active:
            raise ValueError(f"No more {self.name} in stock.")
        if quantity <= 0:
            raise ValueError(f"Enter a positiv amount")
        if quantity > self.quantity:
            raise ValueError(f"Not enough {self.name} in stock.")

        total_price = self.price * quantity
        new_quantity = self.quantity - quantity
        self.set_quantity(new_quantity)

        return total_price
