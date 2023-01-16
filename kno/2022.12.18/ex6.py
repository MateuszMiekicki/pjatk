import numpy as np
from pygad import *

maze = np.array([[1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [0, 1, 1, 1, 1],
                [0, 0, 0, 1, 1]])


gene_space = [0, 1, 2, 3] # kierunki ruchu: prawo, lewo, góra, dół
chromosome_length = len(maze) * len(maze[0]) # długość chromosomu równa liczbie komórek labiryntu

population_size = 100
num_parents_mating = 10

mutation_percent = 1 # 1% szansy na mutację

def fitness_func(chromosome):
    x, y = 0, 0 # pozycja początkowa
    fitness = 1 # liczba komórek po drodze
    for direction in chromosome:
        if direction == 0:
            x += 1 # ruch w prawo
        elif direction == 1:
            x -= 1 # ruch w lewo
        elif direction == 2:
            y -= 1 # ruch w górę
        elif direction == 3:
            y += 1 # ruch w dół
        if (x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze) or maze[y][x] == 0): # sprawdzenie czy wychodzi poza labirynt lub na ścianę
            return 0
        else:
            fitness += 1 # jeśli jest to komórka labiryntu, zwiększ fitness
    return fitness

ga_obj = GA(num_generations=100,
            sol_per_pop=chromosome_length,
            num_parents_mating=num_parents_mating,
            fitness_func=fitness_func,
            gene_space=gene_space,
            mutation_percent=mutation_percent)

best_solution, best_fitness = ga_obj.run()
print("Najlepsze rozwiązanie: ", best_solution)
