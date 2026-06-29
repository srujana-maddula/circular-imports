from catalog import BASE_PRICES

def get_discount(price: float) -> float:
    if price > 500:
        return price * 0.10
    return price * 0.05

def get_discounted_catalog() -> dict:
    products = list(BASE_PRICES.keys())
    return {p: BASE_PRICES[p] - get_discount(BASE_PRICES[p]) for p in products}
