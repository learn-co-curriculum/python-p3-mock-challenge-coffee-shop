class Customer:
    all = []
    
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise AttributeError("Must be a string between 1 and 15 characters long")

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, new_coffee, new_price):
        # remember to pass the values in this order
        # customer, coffee, price
        return Order(self, new_coffee, new_price)

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("Must be a Coffee instance")
        if coffee_all_orders := [order for order in Order.all if order.coffee is coffee]:
            return max(
                cls.all,
                key=lambda customer: sum(
                    order.price
                    for order in coffee_all_orders
                    if order.customer is customer
                ),
            )
        return None
        

from classes.order import Order
from classes.coffee import Coffee