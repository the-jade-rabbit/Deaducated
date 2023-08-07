##
''' this file will generate objects with random core data to eb fed into calcT'''
##
import random
##

class SampleData():
    '''initialise core data members as random values'''
    def __init__(self, direction = 'left/right') -> None:
        self.CoreData = {'ts_start': [random.randint(3, 99)],
                    'ts_end': [random.randint(3, 99)],
                    'no_of_bits': [random.randint(1096, 512*8)],
                        }
        directionLR = direction 
        
    @property
    def checkDirect(self):
        if directionLR == '':
            raise