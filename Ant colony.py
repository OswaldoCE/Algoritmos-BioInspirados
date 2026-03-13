import numpy as np
import random

# Distance matrix between cities
distances = np.array([
    [0, 2, 2, 5, 7],
    [2, 0, 4, 8, 2],
    [2, 4, 0, 1, 3],
    [5, 8, 1, 0, 2],
    [7, 2, 3, 2, 0]
])

n_cities = len(distances)
pheromone = np.ones((n_cities, n_cities))

alpha = 1      # pheromone importance
beta = 2       # distance importance
evaporation = 0.5
ants = 5
iterations = 50

def path_length(path):
    total = 0
    for i in range(len(path)-1):
        total += distances[path[i]][path[i+1]]
    return total

best_path = None
best_length = float("inf")

for _ in range(iterations):
    all_paths = []

    for ant in range(ants):
        path = [random.randint(0, n_cities-1)]

        while len(path) < n_cities:
            current = path[-1]
            probabilities = []

            for city in range(n_cities):
                if city not in path:
                    tau = pheromone[current][city] ** alpha
                    eta = (1 / distances[current][city]) ** beta
                    probabilities.append((city, tau * eta))

            cities, probs = zip(*probabilities)
            probs = np.array(probs) / sum(probs)
            next_city = np.random.choice(cities, p=probs)

            path.append(next_city)

        all_paths.append(path)

        length = path_length(path)
        if length < best_length:
            best_length = length
            best_path = path

    pheromone *= (1 - evaporation)

    for path in all_paths:
        length = path_length(path)
        for i in range(len(path)-1):
            pheromone[path[i]][path[i+1]] += 1 / length

print("Best Path:", best_path)
print("Best Distance:", best_length)