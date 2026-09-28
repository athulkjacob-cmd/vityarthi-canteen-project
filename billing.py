"""
Billing Module
Calculates GST, prints bills, and generates sales reports.
"""
import order

def print_bill(order_id):
    """Calculates 5% GST and prints the final receipt."""
    if order_id not in order.order_database:
        print("Order not found.")
        return

    order_data = order.order_database[order_id]
    subtotal = order_data["total"]
    gst = round(subtotal * 0.05, 2)
    grand_total = subtotal + gst

    print("\n------- CANTEEN RECEIPT -------")
    print(f"Order ID: #{order_id}")
    for item in order_data["items"]:
        print(f"{item['name']:<15} x{item['qty']} : ₹{item['subtotal']:.2f}")
    print("-------------------------------")
    print(f"Subtotal : ₹{subtotal:.2f}")
    print(f"GST (5%) : ₹{gst:.2f}")
    print(f"TOTAL    : ₹{grand_total:.2f}")
    print("-------------------------------\n")

def show_analytics():
    """Calculates total revenue and finds the most popular item."""
    total_revenue = 0
    item_counts = {}

    for o_id, o_data in order.order_database.items():
        total_revenue += o_data["total"]
        for item in o_data["items"]:
            name = item["name"]
            item_counts[name] = item_counts.get(name, 0) + item["qty"]

    print("\n" + "="*35)
    print("        DAILY SALES REPORT")
    print("="*35)
    print(f"Total Orders   : {len(order.order_database)}")
    print(f"Gross Revenue  : ₹{total_revenue:.2f}")
    
    if item_counts:
        best_item = max(item_counts, key=item_counts.get)
        print(f"Most Popular   : {best_item}")
        
    print("-" * 35)
    print("Item Breakdown:")
    for name, qty in item_counts.items():
        print(f"  - {name:<18} : {qty} sold")
    print("="*35 + "\n")    