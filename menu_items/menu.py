


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self,menu_item:"MenuItem")->None:
        self.items.append(menu_item)

    def remove_item(self,item_name:"MenuItem")->None:
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)

    def  get_item_by_name(self,name:"MenuItem")->"MenuItem":
        for item in self.items:
            if item.name == name:
                return item
        return None

    def get_items_by_category(self,category)->list["MenuItem"]:
        all_category = []
        for item in self.items:
            if item.category == category:
                all_category.append(item)
        return all_category

    def display_menu(self)->None:
        for item in self.items:
            if item.available:
                item.get_info()

    def get_total_items(self)->float:
        return f"total items:{len(self.items)}"

if __name__ == "__main__":
    from menu_item import MenuItem
    i1 = MenuItem("fhis", 20, "A")
    i2 = MenuItem("mit", 100, "A")
    i3 = MenuItem("koki", 5, "B")
    i4 = MenuItem("milk", 7, "B")
    m = Menu()
    m.add_item(i1)
    m.add_item(i2)
    m.add_item(i3)
    m.add_item(i4)
    m.display_menu()
    print(m.get_total_items())
    print(m.get_items_by_category('A'))
    m.remove_item(i1.name)
    print(m.get_total_items())
    print(m.get_item_by_name(i2.name))





