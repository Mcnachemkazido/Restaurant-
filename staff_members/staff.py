


class Staff:
    def __init__(self,name:str,salary:int):
        self.name = name
        self.salary = salary
        self.energy = 100

    def work(self)->None:
        self.energy -= 10
        print("i im work")

    def rest(self)->None:
        if self.energy <= 80:
            self.energy += 20
        else:
            self.energy = 100

    def is_tired(self)->bool:
        return self.energy < 30

    def get_info(self):
        print(f"name:{self.name}, energy:{self.energy},"
              f" salary:{self.salary}")



