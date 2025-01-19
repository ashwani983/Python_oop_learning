from item import Item
#child class
class Keyboard(Item):
    def __init__(self, name, price, quantity, broken_keyboards=0):
        #Declare the variable 
        super().__init__(name, price, quantity)
        self.broken_keyboards = broken_keyboards

        #Validatetion of price and quantity
        assert broken_keyboards >= 0, f"Broken keyboards {broken_keyboards} is negative."