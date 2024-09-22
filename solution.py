import random

class Solution:
    
    def __init__(self, n):
        self.n = n
        self.solution =  random.sample(range(self.n), self.n)
        
        
    def get_coords(self):
        x = list(range(self.n))
        y = self.solution
        return list(zip(x, y))