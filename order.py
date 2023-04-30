import decimal


class Order:
    def __init__(self, id: int, name: str, price: decimal):
        self.id = id
        self.name = name
        self.price = price
