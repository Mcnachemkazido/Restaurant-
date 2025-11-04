from staff import Staff

class Chef(Staff):
    def __init__(self,name:str,salary:int,specialty:str):
        super().__init__(name,salary)
        self.specialty = specialty

    def cook_order(self,order:"Order")->None:
        if order.status == 'pending':
            order.status = 'cooking'
        elif order.status == 'cooking':
            order.status = 'ready'

    def Override_work(self)->None:
        self.energy -= 15
        print("cooking is harder")
