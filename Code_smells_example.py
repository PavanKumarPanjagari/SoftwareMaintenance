def calculate_total_price(items):
    total = 0
    for item in items:
        total += calculate_item_price(item)
    return total

def calculate_item_price(item):
    if item.quantity <= 0:
        return 0  # Quantity is not positive, so the item is not included in the total
    elif item.price > 100:
        return item.price * 0.9  # Apply a 10% discount
    else:
        return item.price * 0.95  # Apply a 5% discount
