def calculate_total_price(items):
    total = 0

    def calculate_item_price(item):
        if item.price > 100:
            return item.price * 0.9
        else:
            return item.price * 0.95

    for item in items:
        if item.quantity > 0:
            total += calculate_item_price(item)

    return total
