from classes.coffee import Coffee
from classes.customer import Customer
from classes.order import Order
import pytest


class TestCustomer:
    '''Customer in customer.py'''

    def test_has_name(self):
        '''customer is initialized with name'''
        customer = Customer('Steve')
        assert (customer.name == "Steve")

    def test_can_change_name(self):
        '''customer name can be changed'''
        customer = Customer('Steve')
        customer.name = "Stove"
        assert (customer.name == "Stove")

    def test_customer_name_is_str(self):
        '''customer name is a string'''
        customer = Customer('Steve')
        assert (isinstance(customer.name, str))
        customer.name = 1
        assert (isinstance(customer.name, str))

    def test_customer_name_length(self):
        '''customer name is between 1 and 15 characters'''
        customer = Customer('Steve')
        assert (len(customer.name) == 5)
        customer.name = "NameLongerThan15Characters"
        assert (len(customer.name) == 5)
        customer.name = ""
        assert (len(customer.name) == 5)

    # def test_raise_exception_for_non_string_name(self):
    #     '''raise exception when trying to change name to non str'''
    #     customer = Customer('Steve')
    #     with pytest.raises(Exception):
    #         customer.name = True
    #     with pytest.raises(Exception):
    #         customer.name = "a"*26
    #     with pytest.raises(Exception):
    #         customer.name = ""

    def test_has_many_orders(self):
        '''customer has many orders'''
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)
        order_3 = Order(customer_2, coffee, 5)

        assert (len(customer.orders()) == 2)
        assert (not order_3 in customer.orders())
        assert (order_1 in customer.orders())
        assert (order_2 in customer.orders())

    def test_orders_of_type_order(self):
        '''customer orders are of type Order'''
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert (isinstance(customer.orders()[0], Order))
        assert (isinstance(customer.orders()[1], Order))

    def test_has_many_coffees(self):
        '''customer has many coffees.'''
        coffee = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")

        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee_2, 5)

        assert (coffee in customer.coffees())
        assert (coffee_2 in customer.coffees())

    def test_has_unique_coffees(self):
        '''customer has unique list of all the coffees they have ordered.'''
        coffee = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")

        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 2)
        order_3 = Order(customer, coffee_2, 5)

        assert (len(set(customer.coffees())) == len(customer.coffees()))
        assert (len(customer.coffees()) == 2)

    def test_create_order(self):
        '''test create_order()'''
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert (len(customer.orders()) == 2)
        customer.create_order(coffee, 1)
        assert (len(customer.orders()) == 3)
        assert (customer.orders()[2].price == 1)
        assert (customer.orders()[2].coffee == coffee)
