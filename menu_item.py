class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display_item(self):
        return f"{self.name} - ${self.price:.2f}"