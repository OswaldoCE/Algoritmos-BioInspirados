import random

# Function to minimize (example: f(x) = x^2)
def f(x):
    return x**2

# Parameters
num_particles = 5
iterations = 20

# Initialize particles
particles = [random.uniform(-10, 10) for _ in range(num_particles)]
velocities = [0 for _ in range(num_particles)]

# Best positions
personal_best = particles[:]
global_best = min(particles, key=f)

# PSO loop
for _ in range(iterations):
    for i in range(num_particles):
        
        # Update velocity
        velocities[i] = (
            0.5 * velocities[i] +
            random.random() * (personal_best[i] - particles[i]) +
            random.random() * (global_best - particles[i])
        )
        
        # Update position
        particles[i] += velocities[i]
        
        # Update personal best
        if f(particles[i]) < f(personal_best[i]):
            personal_best[i] = particles[i]
    
    # Update global best
    global_best = min(particles, key=f)

# Result
print("Best solution:", global_best)
print("Best value:", f(global_best))