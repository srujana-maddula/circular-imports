def get_base_price(product: str) -> float:
    base_prices = {
        "laptop": 1000.0,
        "phone": 600.0,
        "tablet": 400.0,
    }
    return base_prices.get(product, 0.0)
