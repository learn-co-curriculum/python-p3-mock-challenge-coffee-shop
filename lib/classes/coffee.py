class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and not hasattr(self, 'name'):
            self._name = name
            
        else: 
            raise Exception("Name already exist")
        
    def orders(self, new_order=None):
        from classes.order import Order
        
        # print(f"A new order for this coffee is recieved: reciept: {new_order}")
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        
        return self._orders
        
    def customers(self, new_customer=None):
        from classes.customer import Customer
        
        if new_customer not in self._customers and isinstance(new_customer, Customer):
            self._customers.append(new_customer)
        
        return self._customers
        
        
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        total = 0
        
        for order in self._orders:
            total += order.price
            
        return total/len(self._orders)
        