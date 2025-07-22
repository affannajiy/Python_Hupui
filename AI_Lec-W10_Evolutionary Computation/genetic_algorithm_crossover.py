'''
Genetic Algorithm - Crossover

1. Initial Population
2. Fitness Function
3. Selection
4. Crossover
5. Mutation
'''

import random

# Fitness function: (a + b) + (c + d)
def fitness(chromosome):
    a, b, c, d = [int(gene) for gene in chromosome]
    return (a + b) + (c + d)

# One-point crossover
def one_point_crossover(p1, p2):
    point = 2  # fixed midpoint for 4-digit chromosome
    return p1[:point] + p2[point:], p2[:point] + p1[point:]

# Two-point crossover
def two_point_crossover(p1, p2):
    # fixed points for 4-digit chromosome
    return p1[0] + p2[1] + p2[2] + p1[3], p2[0] + p1[1] + p1[2] + p2[3]

# Uniform crossover
def uniform_crossover(p1, p2, mask='BAAB'):
    child1 = ''
    child2 = ''
    for i in range(len(mask)):
        if mask[i] == 'A':
            child1 += p1[i]
            child2 += p2[i]
        else:
            child1 += p2[i]
            child2 += p1[i]
    return child1, child2

# Initial population
population = {
    'x1': '3265',
    'x2': '1456',
    'x3': '9875',
    'x4': '4276'
}

# Evaluate fitness
fitness_scores = {k: fitness(v) for k, v in population.items()}
sorted_individuals = sorted(fitness_scores.items(), key=lambda x: x[1], reverse=True)

print("Initial Population Fitness (Descending):")
for name, score in sorted_individuals:
    print(f"{name}: {population[name]} => Fitness: {score}")

# Select top 3 individuals
x3 = population['x3']  # fittest
x4 = population['x4']  # second fittest
x1 = population['x1']  # tied third
mask = 'BAAB'  # uniform crossover pattern

# Perform crossovers
child1, child2 = one_point_crossover(x3, x4)
child3, child4 = two_point_crossover(x4, x1)
child5, child6 = uniform_crossover(x3, x1, mask)

# New population
new_population = {
    'child1': child1,
    'child2': child2,
    'child3': child3,
    'child4': child4,
    'child5': child5,
    'child6': child6
}

# Evaluate fitness of new population
print("\nNew Offspring Fitness:")
for name, chrom in new_population.items():
    print(f"{name}: {chrom} => Fitness: {fitness(chrom)}")