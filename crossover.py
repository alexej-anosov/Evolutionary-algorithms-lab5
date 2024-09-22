from solution import Solution
import random

class Crossover:
    def __init__(self, n: int):
        self.n = n
    
    def crossover(self, p1: Solution, p2: Solution):

        point_a = random.randint(0, self.n-1)
        alpha = random.random()**0.2
        point_b = int(point_a * alpha + self.n * (1-alpha))
        
        p2_ = [i for i in p2.solution if i not in p1.solution[point_a: point_b]]
        c = Solution(n=self.n)
        c.solution = p2_[:point_a] + p1.solution[point_a: point_b] + p2_[point_a:]
        
        if len(c.solution) != self.n:
            1/0
            
        return c