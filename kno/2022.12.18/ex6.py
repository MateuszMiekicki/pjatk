import numpy as np
from pygad import GA

# Definicja labiryntu jako macierzy
maze = np.array([[1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 1],
                 [1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1]])

# Funkcja fitness
def fitness_fn(solution):
    x, y = 0, 0
    for move in solution:
        if move == 0:
            x -= 1
        elif move == 1:
            x += 1
        elif move == 2:
            y -= 1
        elif move == 3:
            y += 1
    if maze[x][y] == 1:
        return 0
    return 1

# Ustawienia algorytmu genetycznego
ga = GA(num_generations=100,
        num_parents_mating=4,
        fitness_fn=fitness_fn,
        sol_per_pop=8,
        num_genes=100,
        gene_range=(0, 3))

# Uruchomienie algorytmu
ga.run()

# Wypisanie najlepszego rozwiązania
print(ga.best_solution())