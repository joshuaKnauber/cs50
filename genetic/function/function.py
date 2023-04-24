import random

def func(x,y,z):
    res = 3*x**2 + 12*y**2 + 30*z
    return res

def fitness(x,y,z):
    res = func(x,y,z)
    goal = 25
    return 1/(abs(res-goal))

if __name__ == "__main__":
    steps = 100
    numberChildren = 1000
    amountBestParents = 100

    solutions = []
    for s in range(numberChildren):
        solutions.append((random.uniform(-100,100),random.uniform(-100,100),random.uniform(-100,100)))

    for i in range(steps):
        ranked = sorted(solutions, key=lambda s: fitness(*s), reverse=True)
        print(f"Step {i}: {ranked[0]} with fitness {fitness(*ranked[0])} and function value {func(*ranked[0])}")

        best = ranked[:amountBestParents]

        newGeneration = []
        for _ in range(numberChildren):
            # crossover
            parent1 = random.choice(best)
            parent2 = random.choice(best)
            # parent3 = random.choice(best)
            child = [parent1[0], parent2[1], parent2[2]]

            # mutation
            child[0] += random.uniform(-0.01,0.01)
            child[1] += random.uniform(-0.01,0.01)
            child[2] += random.uniform(-0.01,0.01)

            newGeneration.append(tuple(child))
        solutions = newGeneration
    
    print(f"Best solution: {ranked[0]} with fitness {fitness(*ranked[0])} and function value {func(*ranked[0])}")