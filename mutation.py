from typing import List
from solution import Solution
import random

class Mutation:
    def __init__(self, n: int, mutation_p: float):
        self.n = n
        self.mutation_p = mutation_p
    
    def mutate(self, population: List[Solution]):
        new_population = []
        for solution in population:
            if random.random() < self.mutation_p:
                point_a = random.randint(0, self.n-1)
                alpha = random.random()**0.7
                point_b = int(point_a * alpha + self.n * (1-alpha))
                new_solution = Solution(n=self.n)
                new_solution.solution = solution.solution
                new_solution.solution[point_a], new_solution.solution[point_b] = new_solution.solution[point_b], new_solution.solution[point_a]
                new_population.append(new_solution)
            else:
                new_population.append(solution)
        return population