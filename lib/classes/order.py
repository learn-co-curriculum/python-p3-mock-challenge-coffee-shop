
class Order:
    
    all = []
    
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        Order.all.append(self)
        
        coffee.orders(self)
        coffee.customers(customer)
        
        customer.orders(self)
        customer.coffees(coffee)
        
        
        
    def __repr__(self):
        return f"{self.customer.name} ordered {self.coffee.name}"
        
    @property 
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if type(price) == (int or float) and 1<= price <= 10:
            self._price = price 
        else: 
            raise Exception

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        
        from classes.customer import Customer;
        if isinstance(customer, Customer):
            self._customer = customer
            
        else: 
            raise Exception("You did not pass a customer object!!")
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        from classes.coffee import Coffee
        if type(coffee) == Coffee:
            self._coffee = coffee
            
        else: 
            raise Exception("You must pass a coffee object")