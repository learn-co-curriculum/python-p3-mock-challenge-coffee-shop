class Customer:
    def __init__(self, name):
        self.name = name
        
    def orders(self, new_order=None):
        from classes.order import Order
        pass
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        pass