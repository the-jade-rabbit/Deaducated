"""Class Definition for measurement"""
#
from argparse import REMAINDER
from argparse import REMAINDER
import math
import random
##
## code starts here

class MeasurementSetup():
    """class to test stuff"""
    
    def __init__(self, direcT = ""):
        """initialisation"""
    
        self.xpos = random.randint(30, 290)
        self.ypos = random.randint(22, 190)
        self.direction = direcT
        ## self.move(x,y)

    def move(self, x, y):
        """move the object to said position"""
        if not isinstance(x, int):
            raise TypeError("only integers genius...")
        if x%2:
            raise ValueError("only even numbers GENIUS!")
        else: self.xpos = x

        if not isinstance(y, int):
            raise TypeError("only integers genius...")
        if y%2:
            raise ValueError("only even numbers GENIUS!")
        else: self.ypos = y

    def reset(self):
        """reset object pos to 0"""

        (self).move(0,0)

    def calc_grad(self, other_point):
        """calculate gradient between both objects"""
        if self.direction == "left":
            print("no calculations to be made")
        elif self.direction == "right":
            return math.sqrt((self.ypos - other_point.ypos)/(self.xpos - other_point.xpos))
        elif self.direction != ["right", "left"]:
            raise TypeError("no direction recognised")