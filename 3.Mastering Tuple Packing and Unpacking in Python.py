# Task 1

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Jeff", "Xbox", 1),
    ("Jason", "Phone", 3),
    # More orders...
]

def process_orders(orders):
    for order in orders:
        customer_name, product, quantity = order
        print(f"Customer: {customer_name}, Product: {product}, Quantity: {quantity}\n")

process_orders(orders)
