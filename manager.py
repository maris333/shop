from typing import Dict

from order import Order


class Manager:
    quantity_in_stock: Dict[Order, int] = {}
    orders: Dict[Order, int] = {}

    def add_order(self, order: Order):
        if order in self.orders:
            self.orders[order] += 1
        else:
            self.orders[order] = 1

    def delete_order(self, order: Order):
        if order in self.orders:
            if self.orders[order] == 1:
                self.orders.pop(order)
            elif self.orders[order] > 1:
                self.orders[order] -= 1
        else:
            print("This order has been deleted")
