"""
Menu Module
Stores an expanded food catalog and handles displaying the menu.
"""

canteen_menu = {
    # Breakfast
    101: {"name": "Veg Sandwich", "price": 60.0},
    102: {"name": "Masala Dosa", "price": 80.0},
    103: {"name": "Idli Sambar (3 pcs)", "price": 50.0},
    
    # Snacks
    201: {"name": "French Fries", "price": 70.0},
    202: {"name": "Samosa (2 pcs)", "price": 30.0},
    203: {"name": "Veg Burger", "price": 85.0},

    # Main Course
    301: {"name": "Veg Thali", "price": 120.0},
    302: {"name": "Chole Bhature", "price": 100.0},
    303: {"name": "Fried Rice", "price": 95.0},

    # Beverages 
    401: {"name": "Tea", "price": 15.0},
    402: {"name": "Filter Coffee", "price": 25.0},
    403: {"name": "Cold Coffee", "price": 60.0},
    404: {"name": "Vanilla Ice Cream", "price": 50.0},
}

def display_menu():
    """Prints the menu in a clean, aligned table."""
    print("\n" + "="*45)
    print("          SMART CANTEEN MENU")
    print("="*45)
    print("ID   | Item Name                  | Price")
    print("-" * 45)
    for item_id, details in canteen_menu.items():
        print(f"{item_id}  | {details['name']:<24} | ₹{details['price']:.2f}")
    print("="*45 + "\n")

def get_item(item_id):
    """Returns the item details if the ID exists."""
    return canteen_menu.get(item_id)