#!/usr/bin/env python3

class Shoe:
    pass
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size

    def get_size(self):
        return self._size

    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print('size must be an integer')  

    size = property(get_size, set_size)

    def cobble(self):
        print('Your shoe is as good as new!')   
        self.condition = 'New'           


shoe1 = Shoe('test', 9)   
shoe1.size = 'cada'   
shoe1.cobble()          
