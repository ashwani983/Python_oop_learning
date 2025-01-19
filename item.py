import csv
class Item:
    pay_rate=0.8

    all=[]
    def __init__(self, name:str, price:int, quantity=0):
        #Declare the variable 
        self.__name = name
        self.__price = price
        self.quantity = quantity

        #Validatetion of price and quantity
        assert price >= 0, f"Price {price} is negative."
        assert quantity >= 0, f"Quantity {quantity} is negative."

        #store all instence into all
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.__price * self.quantity
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    
    def apply_increment(self,increment_value):
        self.__price = self.__price + increment_value
    
    @classmethod
    def instence_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name= item.get("name"),
                price= float(item.get("price")),
                quantity=int(item.get('quantity')),
            )
    
    @staticmethod
    def is_instance(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    
    # create repr method for each item
    def __repr__(self):
        return f"{self.__class__.__name__} , Item('{self.name}', {self.price}, {self.quantity})"
    

    @property
    def name(self):
        print("This is getter")
        return self.__name
    
    @name.setter
    def name(self,value):
        print("This is setter")
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    @property
    # read only property
    def price(self):
        return self.__price
    
    @price.setter
    # write only property
    def price(self,value):
        if value < 0:
            raise Exception("The price is too low")
        else:
            self.__price = value
    

    def __connect(self,smpt_server):
        pass

    def __send(self):
        pass
    def __prepare(self):
        return f"""
        Hi {self.name}
        Here is your invoice for the purchase of the item
        Price: {self.price}
        Quantity: {self.quantity}
        Total price: {self.calculate_total_price()}
        """
    def send_email(self):
        self.__prepare()
        self.__connect("smtp.gmail.com")
        self.__send()
    