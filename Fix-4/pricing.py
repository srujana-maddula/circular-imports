from catalog import BASE_PRICES
from discount import get_discount

def get_base_price(product: str) -> float:
    return BASE_PRICES.get(product, 0.0)

def get_final_price(product: str, quantity: int) -> float:
    price = get_base_price(product) * quantity
    return price - get_discount(price)

print(get_final_price("laptop", 3))
