

class Order:
    def __init__(self,customer:"Customer",order_number:int):
        self.customer = customer
        self.order_number = order_number
        self.items = []
        self. status = 'pending'
        self.total_price = 0

    def add_item(self,menu_item:"MenuItem")->None:
        self.items.append(menu_item)
        self.total_price += menu_item.price

    def remove_item(self,menu_item:"MenuItem")->None:
        self.items.remove(menu_item)
        self.total_price -= menu_item.price

    def get_total(self)->float:
        return self.total_price

    def set_status(self,new_status)->None:
            if new_status in ['pending','cooking','ready','delivered']:
            self.status = new_status

    def display_order(self)->None:
        print(f"order_number:{self.order_number},\n"
              f" customer:{self.customer.name},\n"
              f" items:{self.items},\n "
              f"status: {self.status},\n "
              f"total_price:{self.total_price }")

    def  is_complete(self)->bool:
        return self.status == 'delivered'

if __name__ == "__main__":
    from menu_items.menu_item import MenuItem
    from customer import Customer
    m1 = MenuItem("milk",10,"drink")
    m2 = MenuItem("shoko",10,"drink")
    c = Customer("menachem")
    o = Order(c,10)
    o.add_item(m1)
    o.add_item(m2)
    print(o.get_total())
    o.display_order()