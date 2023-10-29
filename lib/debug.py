#!/usr/bin/env python3
# import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

customer1 = Customer("Kat")
customer2 = Customer("Ant")
customer3 = Customer("Alberto")
customer4 = Customer("Austin")

coffee1 = Coffee("dirty chai")
coffee2 = Coffee("psl")
coffee3 = Coffee("espresso")
coffee4 = Coffee("light oatmilk macchiato")

order1 = Order(customer1, coffee2, 5.00)
order2 = Order(customer3, coffee4, 9.50)
order3 = Order(customer1, coffee2, 6.00)
order3 = Order(customer2, coffee2, 6.00)
order3 = Order(customer1, coffee2, 6.00)
order3 = Order(customer3, coffee2, 6.00)
order3 = Order(customer1, coffee2, 6.00)
order3 = Order(customer1, coffee2, 6.00)
order3 = Order(customer1, coffee2, 6.00)

if __name__ == '__main__':
    print("HELLO! :) let's debug")

print("bananas")
    # ipdb.set_trace()
