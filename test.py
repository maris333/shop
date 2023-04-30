from decimal import Decimal

from manager import Manager
from order import Order


class Test:
    def test_get_order_in_stock_by_id(self):
        order = Order(1, "oranges", Decimal(10))
        manager = Manager({Order(1, "oranges", Decimal(10)): 100, Order(1, "bananas", Decimal(10)): 100})
        assert manager.get_order_in_stock_by_id(order.id).id, order.id

    def test_check_if_order_is_in_stock(self):
        order = Order(1, "oranges", Decimal(10))
        manager = Manager({Order(1, "oranges", Decimal(10)): 100, Order(1, "bananas", Decimal(10)): 100})
        assert manager.check_if_order_is_in_stock(order, 10, 1)

    def test_check_if_order_is_not_in_stock(self):
        order = Order(3, "grapes", Decimal(10))
        manager = Manager({Order(1, "oranges", Decimal(10)): 100, Order(1, "bananas", Decimal(10)): 100})
        assert not manager.check_if_order_is_in_stock(order, 10, 3)

    def test_check_if_too_little_is_in_stock(self):
        order = Order(1, "oranges", Decimal(10))
        manager = Manager({Order(1, "oranges", Decimal(10)): 100, Order(1, "bananas", Decimal(10)): 100})
        assert not manager.check_if_order_is_in_stock(order, 110, 1)

    def test_add_order(self):
        order = Order(1, "oranges", Decimal(10))
        manager = Manager({Order(1, "oranges", Decimal(10)): 100, Order(2, "bananas", Decimal(10)): 100})
        manager.add_order(order, 10, 1)
        assert len(manager.orders) == 1

    def test_add_existing_order(self):
        order = Order(1, "oranges", Decimal(10))
        manager = Manager({Order(1, "oranges", Decimal(10)): 100, Order(2, "bananas", Decimal(10)): 100})
        manager.add_order(order, 1, 1)
        manager.add_order(order, 1, 1)
        assert manager.orders[order], 2

    def test_add_existing_order_check_if_stock_is_reduced(self):
        order = Order(1, "oranges", Decimal(10))
        manager = Manager({Order(1, "oranges", Decimal(10)): 100, Order(1, "bananas", Decimal(10)): 100})
        manager.add_order(order, 10, 1)
        order_in_stock = manager.get_order_in_stock_by_id(order.id)
        assert manager.orders_in_stock[order_in_stock], 90

    def test_add_existing_order_check_if_not_in_stock(self):
        order = Order(3, "apples", Decimal(10))
        manager = Manager({Order(1, "oranges", Decimal(10)): 100, Order(1, "bananas", Decimal(10)): 100})
        assert not manager.add_order(order, 10, 3)

    def test_add_existing_order_check_if_not_enough_in_stock(self):
        order = Order(1, "oranges", Decimal(10))
        manager = Manager({Order(1, "oranges", Decimal(10)): 100, Order(1, "bananas", Decimal(10)): 100})
        assert not manager.add_order(order, 110, 1)

    def test_delete_order(self):
        manager = Manager({Order(1, "oranges", Decimal(10)): 100, Order(1, "bananas", Decimal(10)): 100})
        order = Order(1, "oranges", Decimal(10))
        manager.orders = {order: 1}
        manager.delete_order(order, 1, 1)
        assert len(manager.orders) == 0

    def test_delete_more_than_one_order(self):
        manager = Manager({Order(1, "oranges", Decimal(10)): 100, Order(1, "bananas", Decimal(10)): 100})
        order = Order(1, "oranges", Decimal(10))
        manager.orders = {order: 3}
        manager.delete_order(order, 2, 1)
        assert manager.orders[order], 1

    def test_delete_not_existing_order(self):
        manager = Manager({Order(1, "oranges", Decimal(10)): 100, Order(1, "bananas", Decimal(10)): 100})
        order = Order(3, "apples", Decimal(10))
        assert not manager.delete_order(order, 1, 3)

    def test_delete_existing_order_check_if_stock_is_refilled(self):
        order = Order(1, "oranges", Decimal(10))
        manager = Manager({Order(1, "oranges", Decimal(10)): 100, Order(1, "bananas", Decimal(10)): 100})
        manager.add_order(order, 10, 1)
        manager.delete_order(order, 10, 1)
        order_in_stock = manager.get_order_in_stock_by_id(order.id)
        assert manager.orders_in_stock[order_in_stock], 100

