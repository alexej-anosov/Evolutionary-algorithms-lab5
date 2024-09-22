from solution import Solution

class Factory:
    def __init__(self, n: int):
        self.n = n
    
    def generate(self, population_size: int):
        population = []
        for _ in range(population_size):
            solution = Solution(self.n)
            population.append(solution)
        return population
    