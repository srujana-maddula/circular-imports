def get_discount(price: float) -> float:
    if price > 500:
        return price * 0.10
    return price * 0.05

def get_discounted_catalog() -> dict:
    products = ["laptop", "phone", "tablet"]
    return {p: get_base_price(p) - get_discount(get_base_price(p)) for p in products}

from pricing import get_base_price  # moved to bottom
