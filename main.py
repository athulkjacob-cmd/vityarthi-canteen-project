"""
Main Module
The user interface to interact with the system.
"""
import menu
import order
import billing

def main():
    while True:
        print("\n=== SMART COLLEGE CANTEEN ===")
        print("1. View Menu & Order")
        print("2. Check Order Status")
        print("3. Admin: Update Status")
        print("4. Admin: View Sales Report")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            menu.display_menu()
            cart = []
            while True:
                try:
                    user_input = input("Enter Item ID (0 to stop): ").strip()
                    if not user_input:
                        continue
                    i_id = int(user_input)
                    if i_id == 0:
                        break
                    
                    qty_input = input("Enter Quantity: ").strip()
                    qty = int(qty_input) if qty_input else 0
                    
                    if qty > 0:
                        cart.append((i_id, qty))
                    else:
                        print("Quantity must be greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
            
            o_id, msg = order.create_order(cart)
            if o_id:
                print(f"\n{msg}")
                billing.print_bill(o_id)
            else:
                print(f"\nError: {msg}")

        elif choice == "2":
            try:
                o_id = int(input("Enter Order ID (e.g., 1001): "))
                status = order.check_status(o_id)
                print(f"\nOrder #{o_id} Status: {status}" if status else "\nOrder not found.")
            except ValueError:
                print("Invalid ID format.")

        elif choice == "3":
            try:
                o_id = int(input("Enter Order ID to update: "))
                if not order.check_status(o_id):
                    print("Order not found.")
                    continue
                    
                print("Statuses: Received, Preparing, Ready, Completed")
                new_status = input("Enter new status exactly as above: ").strip()
                
                if order.update_status(o_id, new_status):
                    print("Status successfully updated.")
                else:
                    print("Failed to update status. Check spelling.")
            except ValueError:
                print("Invalid ID format.")

        elif choice == "4":
            billing.show_analytics()

        elif choice == "5":
            print("\nExiting System. Goodbye!")
            break
        else:
            print("Invalid choice. Select a number from 1 to 5.")

if __name__ == "__main__":
    main()