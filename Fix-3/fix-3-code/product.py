from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from order import Order  # never runs at runtime

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def is_in_order(self, order: Order) -> bool:
        return order.product.name == self.name
