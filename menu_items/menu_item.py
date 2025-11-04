
class MenuItem:
    def __init__(self,name:str, price:float,category:str,available:bool=True):
        self.name = name
        self.price = price
        self. category =  category
        self.available = available

    def get_info(self)->str:
        print(f"name:{self.name}, price:{self.price },"
                f"category:{self.category}")

    def set_available(self,status)->None:
        if status == "is available":
            self.available =  True
        elif status == "sold out":
            self.available = False
        else:
            raise ValueError("is available or sold out")

    def is_available(self)->bool:
        return self.available





if __name__ == "__main__":
    m = MenuItem("shuu",10,"drink")
    print(m.get_info())
    print(m.is_available())
    m.set_available("sold out")
    print(m.is_available())