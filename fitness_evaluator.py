from solution import Solution
from typing import List


class FitnessEvaluator:
    def __init__(self, n: int):
        self.n = n
        
    def evaluate_solution(self, solution: Solution):
        
        solution_coords = solution.get_coords()
        fitness_value = 0
        
        for x, y in solution_coords:
            
            # right&up diag
            x_, y_ = x+1, y+1
            while (x_ < self.n) and (y_ < self.n):
                if (x_, y_) in solution_coords:
                    fitness_value -= 1
                x_ +=1
                y_ +=1
                
            # right&down diag
            x_, y_ = x+1, y-1
            while (x_ < self.n) and (y_ >= 0):
                if (x_, y_) in solution_coords:
                    fitness_value -= 1
                x_ +=1
                y_ +=1
                
        return fitness_value
    
    def evaluate_population(self, population: List[Solution]):
        return [self.evaluate_solution(solution) for solution in population]