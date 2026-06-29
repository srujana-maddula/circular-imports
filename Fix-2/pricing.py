def get_base_price(product: str) -> float:
    base_prices = {"laptop": 1000.0, "phone": 600.0, "tablet": 400.0}
    return base_prices.get(product, 0.0)

def get_final_price(product: str, quantity: int) -> float:
    price = get_base_price(product) * quantity
    return price - get_discount(price)

from discount import get_discount  # moved to bottom

print(get_final_price("laptop", 3))
