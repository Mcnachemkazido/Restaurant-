# from staff import Staff
# from customers_and_orders.order import Order
# from customers_and_orders.customer import Customer
# from menu_items.menu import *

class Waiter(Staff):
    def __init__(self,name:str, salary:int,tips:int):
        super().__init__(name,salary)
        self.tips = tips

    def take_order(self,customer:"Customer", menu:"Menu",order_number:int):
        new_order =Order(customer,order_number)
        flag = True
        while flag:
            menu.display_menu()
            status = input("האם ברצונך לבחור פריט yes or no ")
            if status == "yes":
                name = input("תכניס את השם של המוצר")
                name_true = menu.get_item_by_name(name)
                new_order.add_item(name_true)
            else:
                flag = False
        new_order.display_order()
        return new_order

    def serve_order(self,order:"Order",customer:"Customer"):
        order.status = 'delivered'
        customer.get_info()

    def receive_tip(self,amount):
        self.tips += amount

    def get_total_earnings(self):
        return f"total_earnings{self.salary + self.tips}"




# w = Waiter("menacehm",1000,50)
# c = Customer("moshe")
# w.take_order(c,m,10)










