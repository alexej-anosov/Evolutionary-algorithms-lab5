from factory import Factory
from fitness_evaluator import FitnessEvaluator
from mutation import Mutation
from crossover import Crossover
from utils import tournament_selection


class Alg:
    
    def __init__(self, n: int, population_size: int,
                 elite_count: int, garbage_count: int, 
                 tournament_p: float, tournament_k: int,
                 mutation_p: float):
        self.n = n
        self.population_size = population_size
        self.elite_count = elite_count
        self.garbage_count = garbage_count
        
        self.tournament_p = tournament_p
        self.tournament_k = tournament_k
        
        self.factory = Factory(self.n)
        self.fitness_calculator = FitnessEvaluator(self.n)
        self.mutation = Mutation(self.n, mutation_p)
        self.crossover = Crossover(self.n)

        
    def run(self, max_iterations):
        population = self.factory.generate(self.population_size)
        fitness_values = self.fitness_calculator.evaluate_population(population)
        sorted_population_values = sorted(zip(population, fitness_values), key=lambda x: x[1], reverse=True)
        population, fitness_values = zip(*sorted_population_values)
        
        iteration = 0 
        while (fitness_values[0] != 0) and (iteration<max_iterations):
            iteration+=1 
            
            new_population = []
            new_population.extend(population[:self.elite_count])
            new_population.extend(population[-self.garbage_count:])
             
            for _ in range(self.population_size-self.elite_count-self.garbage_count):
                p1, p1_value = tournament_selection(sorted_population_values, self.tournament_k, self.tournament_p)
                p2, p2_value = tournament_selection(sorted_population_values, self.tournament_k, self.tournament_p)
                
                c = self.crossover.crossover(p1, p2)
                new_population.append(c)
                
            population = self.mutation.mutate(new_population)
            fitness_values = self.fitness_calculator.evaluate_population(population)
            sorted_population_values = sorted(zip(population, fitness_values), key=lambda x: x[1], reverse=True)
            population, fitness_values = zip(*sorted_population_values)
            
            print(f"Iteration: {iteration} || Best fitness value: {fitness_values[0]} || Mean fitness value: {sum(fitness_values) / self.population_size}")
                    

if __name__ == '__main__':
    alg = Alg(64, 100, 5, 5, 0.5, 4, 0.1)
    alg.run(1000)
             
             
        