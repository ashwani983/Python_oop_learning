from item import Item
#child class
class Phone(Item):
    def __init__(self, name, price, quantity, broken_phones=0):
        #Declare the variable 
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

        #Validatetion of price and quantity
        assert broken_phones >= 0, f"Broken phones {broken_phones} is negative."