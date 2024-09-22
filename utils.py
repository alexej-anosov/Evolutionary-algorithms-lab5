import random

def tournament_selection(population_values, k: int, p: float):
    tournament = random.sample(population_values, k)
    tournament.sort(key=lambda x: x[1], reverse=True)
    
    probabilities = [p * ((1 - p) ** i) for i in range(k-1)]
    probabilities.append(1 - sum(probabilities))
    
    selected_index = random.choices(range(k), weights=probabilities, k=1)[0]
    
    return tournament[selected_index]