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
        # else:
        #     raise Exception

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        # else:
        #     raise Exception

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if (
            isinstance(price, float)
            and 1.0 <= price <= 10.0
            and not hasattr(self, "price")
        ):
            self._price = price
        # else:
        #     raise Exception


from classes.coffee import Coffee
from classes.customer import Customer
