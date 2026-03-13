import random

# Problem data
weights = [2, 3, 4, 5]
values = [3, 4, 5, 8]
capacity = 12

POPULATION_SIZE = 5
GENERATIONS = 20
MUTATION_PROBABILITY = 0.1


def create_individual():
    """
    Creates a random individual represented as a binary list.
    """
    return [random.randint(0, 1) for _ in range(len(weights))]


def create_population():
    """
    Generates the initial population.
    """
    return [create_individual() for _ in range(POPULATION_SIZE)]


def fitness(individual):
    """
    Evaluates an individual by calculating the total value of selected items.
    If the total weight exceeds the capacity, the fitness is zero.
    """
    total_weight = 0
    total_value = 0

    for i in range(len(individual)):
        if individual[i] == 1:
            total_weight += weights[i]
            total_value += values[i]

    if total_weight > capacity:
        return 0

    return total_value


def select_best(population):
    """
    Selects the two best individuals based on fitness.
    """
    population.sort(key=fitness, reverse=True)
    return population[:2]


def crossover(parent1, parent2):
    """
    Performs one-point crossover between two parents.
    """
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]


def mutate(individual):
    """
    Applies mutation by flipping bits with a small probability.
    """
    for i in range(len(individual)):
        if random.random() < MUTATION_PROBABILITY:
            individual[i] = 1 - individual[i]
    return individual


# Main genetic algorithm
population = create_population()

for generation in range(GENERATIONS):
    parents = select_best(population)
    new_population = parents.copy()

    while len(new_population) < POPULATION_SIZE:
        child = crossover(parents[0], parents[1])
        child = mutate(child)
        new_population.append(child)

    population = new_population
    best = select_best(population)[0]
    print(f"Generation {generation}: Best solution = {best}, Value = {fitness(best)}")

print("Best solution found:", best)
