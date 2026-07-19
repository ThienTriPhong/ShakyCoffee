class Order:
    def __init__(self):
        # This list stores all items added to the order.
        self.items = []

    def add_item(self, menu_item, quantity):
        order_item = {
            "item": menu_item,
            "quantity": quantity
        }

        self.items.append(order_item)

    def calculate_total(self):
        total = 0

        for order_item in self.items:
            item = order_item["item"]
            quantity = order_item["quantity"]

            total += item.price * quantity

        return total

    def get_order_summary(self):
        summary = ""

        for order_item in self.items:
            item = order_item["item"]
            quantity = order_item["quantity"]
            item_total = item.price * quantity

            summary += (
                f"{item.name} x{quantity} - "
                f"${item_total:.2f}\n"
            )

        return summary

    def clear_order(self):
        self.items.clear()