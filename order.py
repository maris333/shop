from decimal import Decimal


class Order:
    def __init__(self, id: int, name: str, price: Decimal):
        self.id = id
        self.name = name
        self.price = price
