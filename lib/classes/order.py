class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise AttributeError("Must be an instance of the Customer class")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise AttributeError("Must be an instance of the Coffee class")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, int) and 1 <= price <= 10:
            self._price = price
        else:
            raise AttributeError("Must be an integer between 1 and 10")


from classes.coffee import Coffee
from classes.customer import Customer