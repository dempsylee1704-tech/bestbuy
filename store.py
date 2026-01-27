from products import Product

class Store:
    def __init__(self, product_lst):
        if not isinstance(product_lst, list):
            raise TypeError("product_lst must be a list")
        for p in product_lst:
            if not isinstance(p, Product):
                raise TypeError("All items in product_lst must be Product objects")
        self.product_lst = product_lst


    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("product must be a Product")
        self.product_lst.append(product)


    def remove_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("product must be a Product")
        if product not in self.product_lst:
            raise ValueError("Product not in store")
        self.product_lst.remove(product)


    def get_total_quantity(self) -> int:
        quantity_products = 0
        for product in self.product_lst:
            quantity_products += product.get_quantity()
        return quantity_products


    def get_all_products(self) -> list[Product]:
        active_products = []
        for product in self.product_lst:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            price = product.buy(quantity)
            total_price += price
        return total_price

