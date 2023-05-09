#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    
    customer1 = Customer("Steve")
    customer2 = Customer("Dima")
    customer3 = Customer("Wayne")
    customer4 = Customer("Peter")
    
    coffee1 = Coffee("Mocha")
    coffee2 = Coffee("Peppermint Mocha")
    
    order1 = Order(customer1, coffee1, 2)
    order2 = Order(customer2, coffee1, 2)
    order5 = Order(customer2, coffee1, 2)
    order3 = Order(customer3, coffee2, 4)
    order4 = Order(customer4, coffee2, 4)
    
    
    ipdb.set_trace()
