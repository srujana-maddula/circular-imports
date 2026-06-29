from pricing import get_base_price
from discount import get_discount

PRODUCTS = ["laptop", "phone", "tablet"]


def get_final_price(product: str, quantity: int) -> float:
    price = get_base_price(product) * quantity
    return price - get_discount(price)


def get_discounted_catalog() -> dict:
    return {
        p: get_base_price(p) - get_discount(get_base_price(p))
        for p in PRODUCTS
    }


print(get_final_price("laptop", 3))
print(get_discounted_catalog())
