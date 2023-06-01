import pytest

from classes.coffee import Coffee
from classes.customer import Customer
from classes.order import Order

class TestCoffee:
    '''Coffee in coffee.py'''

    def test_has_name(self):
        '''coffee is initialized with a name'''
        coffee = Coffee("Mocha")
        assert (coffee.name == "Mocha"), "The name attribute of Coffee was not set"

    def test_name_is_string(self):
        '''coffee is initialized with a name of type str'''
        coffee = Coffee("Mocha")
        assert (isinstance(coffee.name, str)), "The name attribute of Coffee was not initialized with a str"

    def test_name_setter(self):
        '''Cannot change the name of the coffee'''
        coffee = Coffee("Mocha")

        with pytest.raises(Exception):
            coffee.name = "Peppermint Mocha"

    def test_has_many_orders(self):
        '''coffee has many orders.'''
        coffee = Coffee("Hazelnut Latte")
        coffee_2 = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)
        order_3 = Order(customer, coffee_2, 5)

        assert (len(coffee.orders()) == 2)
        assert (order_1 in coffee.orders()), "order was not added to the coffee object's order list. Check that coffee.orders() is being called in Order.__init__"
        assert (order_2 in coffee.orders())
        assert (not order_3 in coffee.orders())

    def test_orders_of_type_order(self):
        '''coffee orders are of type Order'''
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert (isinstance(coffee.orders()[0], Order)), "Coffee.orders() should return a list with objects of type Order" 
        assert (isinstance(coffee.orders()[1], Order))

    def test_has_many_customers(self):
        '''coffee has many customers.'''
        coffee = Coffee("Flat White")

        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer_2, coffee, 5)

        assert (customer in coffee.customers()), "customer was not added to the coffee object's customer list. Check that coffee.customers() is being called in Order.__init__"
        assert (customer_2 in coffee.customers())

    def test_has_unique_customers(self):
        '''coffee has unique list of all the customers that have ordered it.'''
        coffee = Coffee("Vanilla Latte")

        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer_2, coffee, 2)
        order_3 = Order(customer, coffee, 5)
        
        assert (len(coffee.customers()) == 2), "the Coffee.customers() method did not return a list of 2 customers"
        assert (len(set(coffee.customers())) == len(coffee.customers())), "Duplicate customers found in in Coffee"
        

    def test_customers_of_type_customer(self):
        '''coffee customers are of type Customer'''
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer_2, coffee, 5)

        assert (isinstance(coffee.customers()[0], Customer)), "Coffee.customers() should return a list with objects of type Customer" 
        assert (isinstance(coffee.customers()[1], Customer))

    def test_get_number_of_orders(self):
        '''test num_orders()'''
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert (coffee.num_orders() == 2), "num_orders does not return the correct number. Check that Order.__init__ is calling coffee.orders()"

    def test_average_price(self):
        '''test average_price()'''
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        Order(customer, coffee, 2)
        Order(customer_2, coffee, 5)

        assert (coffee.average_price() == 3.5), "average_price() computes incorrect result"
