from product import Product

class Order:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def get_total(self) -> float:
        return self.product.price * self.quantity

laptop = Product("laptop", 1000.0)
order = Order(laptop, 3)
print(order.get_total())
