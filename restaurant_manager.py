
from customers_and_orders.order import Order
from customers_and_orders.customer import Customer
from menu_items.menu import *


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.staff = []
        self.orders = []
        self.money = 1000

    def hire_staff(self,staff_member:"Staff"):
        self.staff.append(staff_member)

    def fire_staff(self,staff_name):
        for s in self.staff:
            if s.name == staff_name:
                self.staff.remove(s)

    def create_order(self,customer:"Customer"):
        new_order = Order(customer,1)
        self.orders.append(new_order)

    def process_order(self,order):
        pass

    def complete_order(self,order:"Order"):
        pass









