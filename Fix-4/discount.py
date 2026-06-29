def get_discount(price: float) -> float:
    if price > 500:
        return price * 0.10
    return price * 0.05
