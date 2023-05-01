from typing import Dict

from order import Order


class Manager:
    def __init__(self, orders_in_stock: Dict[Order, int]):
        self.orders_in_stock = orders_in_stock
        self.orders: Dict[Order, int] = {}

    def get_order_in_stock_by_id(self, id: int):
        for order_in_stock in self.orders_in_stock.keys():
            if order_in_stock.id == id:
                return order_in_stock

    def check_if_order_is_in_stock(self, order: Order, amount: int):
        if self.get_order_in_stock_by_id(order.id) is not None:
            order_in_stock = self.get_order_in_stock_by_id(order.id)
            if self.orders_in_stock[order_in_stock] >= amount:
                return True
            print("There is not enough {} in stock".format(order_in_stock.name))
            return False
        print("{} are not in stock".format(order.name.title()))
        return False

    def add_order(self, order: Order, amount: int):
        if self.check_if_order_is_in_stock(order, amount):
            order_in_stock = self.get_order_in_stock_by_id(order.id)
            if order in self.orders:
                self.orders[order] += amount
                self.orders_in_stock[order_in_stock] -= amount
                print("{} of {} was added".format(amount, order.name))
                return True
            self.orders[order] = amount
            self.orders_in_stock[order_in_stock] -= amount
            print("{} of {} was added".format(amount, order.name))
            return True
        return False

    def delete_order(self, order: Order, amount: int):
        if order in self.orders:
            order_in_stock = self.get_order_in_stock_by_id(order.id)
            if self.orders[order] == amount:
                self.orders.pop(order)
                self.orders_in_stock[order_in_stock] += amount
                print("{} of {} were deleted".format(amount, order.name))
                return True
            elif self.orders[order] > amount:
                self.orders[order] -= amount
                self.orders_in_stock[order_in_stock] += amount
                print("{} of {} were deleted".format(amount, order.name))
                return True
            print("The quantity to be removed exceeds the order")
            return False
        print("{} were not ordered".format(order.name.title()))
        return False
