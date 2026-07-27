# Program 15: Real-world OOP sketch
class Order:
    def __init__(self, order_id):
        self.order_id = order_id

print(Order(101).order_id)
