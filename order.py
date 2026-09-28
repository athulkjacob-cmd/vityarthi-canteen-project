"""
Order Module
Handles creating orders, tracking status, and contains dummy data.
"""
import menu

# Pre-loaded dummy data to make it look like a busy canteen
order_database = {
    1001: {
        "items": [
            {"name": "Veg Sandwich", "qty": 2, "subtotal": 120.0}, 
            {"name": "Cold Coffee", "qty": 1, "subtotal": 60.0}
        ],
        "total": 180.0,
        "status": "Completed"
    },
    1002: {
        "items": [
            {"name": "Masala Dosa", "qty": 1, "subtotal": 80.0}, 
            {"name": "Filter Coffee", "qty": 2, "subtotal": 50.0}
        ],
        "total": 130.0,
        "status": "Ready"
    },
    1003: {
        "items": [
            {"name": "Veg Thali", "qty": 2, "subtotal": 240.0}, 
            {"name": "Tea", "qty": 3, "subtotal": 45.0}
        ],
        "total": 285.0,
        "status": "Preparing"
    }
}

order_counter = 1003
valid_statuses = ["Received", "Preparing", "Ready", "Completed"]

def create_order(cart):
    """Calculates subtotal for all the items in the cart and saves the order."""
    global order_counter
    
    if len(cart) == 0:
        return None, "Cart is empty."

    order_items = []
    total_amount = 0.0
    for item_id, qty in cart:
        item = menu.get_item(item_id)
        if item and qty > 0:
            subtotal = item["price"] * qty
            total_amount += subtotal
            order_items.append({
                "name": item["name"],
                "qty": qty,
                "subtotal": subtotal
            })

    if not order_items:
        return None, "No valid items selected."
    order_counter += 1
    order_database[order_counter] = {"items": order_items,
        "total": total_amount,
        "status": "Received"}
    return order_counter, "Order successful."
def check_status(order_id):
    """Gets the current status of an order."""
    if order_id in order_database:
        return order_database[order_id]["status"]
    return None
def update_status(order_id, new_status):
    """Changes the status of an existing order."""
    if order_id in order_database and new_status in valid_statuses:
        order_database[order_id]["status"] = new_status
        return True
    return False    