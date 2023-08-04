"""Class Definition for measurement"""

import math
##
## code starts here

class MeasurementSetup():
    """class to test stuff"""
    def __init__(self, x, y):
        """initialisation"""

        self.move(x,y)

    def move(self, x, y):
        """move the object to said position"""

        self.x = x
        self.y = y

    def reset(self):
        """reset object pos to 0"""

        (self).move(0,0)

    def calculate_gradient(self, other_point):
        """calculate gradient between both objects"""

        grad = math.sqrt((self.y - other_point.y)/(self.x - other_point.x))
        return grad 

