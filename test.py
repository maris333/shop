from unittest import TestCase

from manager import Manager
from order import Order


class Test(TestCase):
    # only work when run separately ;/

    def testAddOrder(self):
        order = Order(1, "apples", 10)
        manager = Manager()
        manager.add_order(order)
        self.assertEqual(len(manager.orders), 1)

    def testAddExistingOrder(self):
        order = Order(1, "apples", 10)
        manager = Manager()
        manager.add_order(order)
        manager.add_order(order)
        self.assertEqual(manager.orders[order], 2)

    def testDeleteOrder(self):
        manager = Manager()
        order = Order(1, "apples", 10)
        manager.orders = {order: 1}
        manager.delete_order(order)
        self.assertEqual(len(manager.orders), 0)

    def testDeleteExistingOrder(self):
        manager = Manager()
        order = Order(1, "apples", 10)
        manager.orders = {order: 2}
        manager.delete_order(order)
        self.assertEqual(manager.orders[order], 1)
