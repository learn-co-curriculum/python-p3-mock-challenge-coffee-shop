from classes.coffee import Coffee
from classes.customer import Customer
from classes.order import Order
import pytest


class TestOrders:
    '''Order in order.py'''

    def test_has_price(self):
        '''is initialized with a price'''
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert (order_1.price == 2)
        assert (order_2.price == 5)

    # def test_raise_exception_for_invalid_price(self):
    #     '''raise exception when invalid price'''
    #     coffee = Coffee("Mocha")
    #     customer = Customer('Steve')
    #     order = Order(customer, coffee, 2)
    #     with pytest.raises(Exception):
    #         order.rating = 13
    #     with pytest.raises(Exception):
    #         order.rating = "5"
    #     with pytest.raises(Exception):
    #         order.rating = -3

    def test_has_a_customer(self):
        '''order has a customer .'''
        coffee = Coffee("Mocha")
        customer_1 = Customer('Wayne')
        customer_2 = Customer('Dima')
        order_1 = Order(customer_1, coffee, 2)
        order_2 = Order(customer_2, coffee, 5)

        assert (order_1.customer == customer_1)
        assert (order_2.customer == customer_2)

    def test_customer_of_type_customer(self):
        '''customer is of type Customer'''
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert (isinstance(order_1.customer, Customer))
        assert (isinstance(order_2.customer, Customer))

    def test_has_a_coffee(self):
        '''Review has a coffee.'''
        coffee_1 = Coffee("Mocha")
        coffee_2 = Coffee("Peppermint Mocha")
        customer = Customer('Wayne')
        order_1 = Order(customer, coffee_1, 2)
        order_2 = Order(customer, coffee_2, 5)

        assert (order_1.coffee == coffee_1)
        assert (order_2.coffee == coffee_2)

    def test_coffee_of_type_coffee(self):
        '''coffee is of type Coffee'''
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert (isinstance(order_1.coffee, Coffee))
        assert (isinstance(order_2.coffee, Coffee))

    def test_get_all_orders(self):
        '''test Order class all attribute'''
        Order.all = []
        coffee = Coffee("Mocha")
        customer = Customer('Wayne')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer_2, coffee, 5)

        assert (len(Order.all) == 2)
        assert (order_1 in Order.all)
        assert (order_2 in Order.all)
