"""
Testing Module
Contains basic unit tests to ensure the logic works.
"""
import unittest
import menu
import order
import billing

class TestCanteen(unittest.TestCase):

    def test_menu_retrieval(self):
        item = menu.get_item(101)
        self.assertEqual(item["name"], "Veg Sandwich")
        
        invalid_item = menu.get_item(999)
        self.assertIsNone(invalid_item)

    def test_create_order(self):
        # 1 Cold Coffee (60) + 1 Tea (15) = 75
        cart = [(403, 1), (401, 1)]
        order_id, msg = order.create_order(cart)
        self.assertIsNotNone(order_id)
        
        saved_order = order.order_database[order_id]
        self.assertEqual(saved_order["total"], 75.0)
        self.assertEqual(saved_order["status"], "Received")

    def test_status_update(self):
        # We can test against the pre-loaded dummy order 1001
        current = order.check_status(1001)
        self.assertEqual(current, "Completed")
        
        # Test updating a valid order to a new valid status
        success = order.update_status(1001, "Ready")
        self.assertTrue(success)
        self.assertEqual(order.check_status(1001), "Ready")
        
        # Test invalid status rejection
        fail = order.update_status(1001, "Delivered")
        self.assertFalse(fail)

if __name__ == "__main__":
    unittest.main()