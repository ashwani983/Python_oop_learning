from item import Item
from phone import Phone
from keyboard import Keyboard

# # all the instance of the class

# print(Item.instence_from_csv())
# print(Item.all)

# #creating instance of the class
# item1 = Item('Phone',100,1)
# item2 = Item('Laptop',1000,3)
# item3 = Item('Mouse',20,2)

# #accesing the static method 
# print(Item.is_instance(5))
# print(Item.is_instance(5.0))
# print(Item.is_instance('5'))


phone1 = Phone('Iphone',1000,2,1)
print(Item.all)
print(Phone.all)
print(phone1.apply_increment(20))


item1 = Item('Phone',100)
item1.apply_discount()
print(item1.price)
item1.apply_increment(20)
print(item1.price)
print(item1.name)

# print(item1.read_only_name)
# item1.read_only_name = "asdaks"
# print(item1.read_only_name)

item1.send_email()


#call kryboard class
keyboard1 = Keyboard('Dell',100,2,1)
print(Item.all)
print(Keyboard.all)
print(keyboard1.apply_increment(20))
