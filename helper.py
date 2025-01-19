# when to use classmethod and when we use static method ?


class Item:
    @staticmethod
    def is_integer(num):
        '''
        This should be do somthing that has a relationship with the class , but not something that must be unique per instance !
        '''
    
    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do something that has a relationship with the clashh bit usually those are used to manipulate differenct 
        structures of the data to instantiate objects, like we have done with csv and json. 
        '''



item1 = Item()
item1.is_integer(5)
item1.instantiate_from_something()