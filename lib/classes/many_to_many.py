class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property # getter
    def name(self):
        return self._name
    
    @name.setter # setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Coffee must be a string")
        elif len(new_name) < 3:
            raise ValueError("Coffee must be more than 3 chars")
        elif hasattr(self, "name"):
            raise AttributeError("Cannot change coffee order")
        else:
            self._name = new_name
        
    def orders(self):
        return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if len(prices) else 0

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property # getter
    def name(self):
        return self._name
    
    @name.setter # setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        elif not 0 < len(new_name) < 16:
            raise ValueError("Name must be 1-15 chars")
        else:
            self._name = new_name
        
    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    # associates it with that customer and coffee obj provided?
    
    @classmethod
    def most_aficionado(cls, coffee):
        max_customer = None
        temp_max = 0
        max_spent = 0
        coffee_orders = [order for order in Order.all if order.coffee == coffee]
        for customer in cls.all:
            for order in coffee_orders:
                if order.customer == customer:
                    temp_max += order.price
            if temp_max > max_spent:
                max_spent = temp_max
                max_customer = customer
            temp_max = 0
        return max_customer

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property # getter
    def customer(self):
        return self._customer
    
    @customer.setter # setter
    def customer(self, new_customer):
        if not isinstance(new_customer, Customer):
            raise TypeError("Customer must be part of Customer class")
        else:
            self._customer = new_customer
    
    @property # getter
    def coffee(self):
        return self._coffee
    
    @coffee.setter # setter
    def coffee(self, new_coffee):
        if not isinstance(new_coffee, Coffee):
            raise TypeError("Coffee must be part of Coffee class")
        else:
            self._coffee = new_coffee
    
    @property # getter
    def price(self):
        return self._price
    
    @price.setter # setter
    def price(self, new_price):
        if not isinstance(new_price, float):
            raise TypeError("Price must be a float")
        elif not 1.0 <= new_price <= 10.0:
            raise ValueError("Price must be between $1-10")
        elif hasattr(self, "price"):
            raise AttributeError("Cannot change price")
        else:
            self._price = new_price