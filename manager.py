from typing import Dict

from order import Order


class Manager:
    def __init__(self, quantity_in_stock: Dict[str, int]):
        self.quantity_in_stock = quantity_in_stock
        self.orders: Dict[Order, int] = {}

    def check_if_order_is_in_stock(self, order: Order, amount: int):
        if order.name in self.quantity_in_stock:
            if self.quantity_in_stock[order.name] >= amount:
                return True
            print("There is not enough {} in stock".format(order.name))
            return False
        print("{} are not in stock".format(order.name.title()))
        return False

    def add_order(self, order: Order, amount: int):
        if self.check_if_order_is_in_stock(order, amount):
            if order in self.orders:
                self.orders[order] += amount
                self.quantity_in_stock[order.name] -= amount
                return True
            self.orders[order] = amount
            self.quantity_in_stock[order.name] -= amount
            return True
        return False

    def delete_order(self, order: Order, amount: int):
        if order in self.orders:
            if self.orders[order] == amount:
                self.orders.pop(order)
                self.quantity_in_stock[order.name] += amount
                return True
            elif self.orders[order] > amount:
                self.orders[order] -= amount
                self.quantity_in_stock[order.name] += amount
                return True
            print("The quantity to be removed exceeds the order")
            return False
        print("{} were not ordered".format(order.name.title()))
        return False
