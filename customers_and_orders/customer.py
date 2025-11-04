

class Customer:
    def __init__(self,name):
        self.name = name
        self.satisfaction = 50

    def increase_satisfaction(self,amount):
        if 50 < amount <= 100:
            self.satisfaction = amount
        else:
            print("only 51 - 100")

    def decrease_satisfaction(self,amount):
        if 0 >= amount < 50:
            self.satisfaction = amount
        else:
            print("only 0 - 49")

    def is_happy(self):
        return self.satisfaction > 70

    def get_info(self):
        print(f"name: {self.name}, satisfaction:{self.satisfaction}")


