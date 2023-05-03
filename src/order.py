from decimal import Decimal


class Order:
    def __init__(self, id: int, name: str, price: Decimal):
        self.id = id
        self.name = name
        self.price = price

    def __hash__(self):
        return hash((self.id, self.name, self.price))

    def __eq__(self, other):
        if isinstance(other, Order):
            return (self.id, self.name, self.price) == (
                other.id,
                other.name,
                other.price,
            )
        return False
