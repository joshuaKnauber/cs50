import random

def fitness(items, solution, weightLimit):
    weight = 0
    value = 0
    for i in range(len(items)):
        weight += items[i][0] * solution[i]
        value += items[i][1] * solution[i]
    if weight > weightLimit:
        return 0
    return value


if __name__ == "__main__":
    steps = 100
    numberChildren = 100
    numberBestParents = 10
    elite = 2

    items = [ # (weight, value)
        (2, 7),
        (3, 11),
        (5, 19),
        (8, 28),
        (12, 40),
        (14, 45),
        (17, 52),
        (20, 58),
        (23, 65),
        (26, 72),
        (28, 76),
        (31, 80),
        (35, 88),
        (38, 92),
        (41, 98),
    ]
    weightLimit = 75

    population = []
    for s in range(numberChildren):
        population.append([random.randint(0,1) for _ in range(len(items))])

    for i in range(steps):
        ranked = sorted(population, key=lambda s: fitness(items, s, weightLimit), reverse=True)
        print(f"Step {i}: {ranked[0]}, Fitness: {fitness(items, ranked[0], weightLimit)}, Weight: {sum([items[i][0]*ranked[0][i] for i in range(len(items))])}")

        best = ranked[:numberBestParents]

        newGeneration = []

        # elitism
        newGeneration += best[:elite]

        for _ in range(numberChildren - elite):
            # single point crossover
            parent1 = random.choice(best)
            parent2 = random.choice(best)
            cutIndex = random.randint(0, len(items)-1)
            child = parent1[:cutIndex] + parent2[cutIndex:]

            # mutation
            for i in range(len(items)):
                if random.random() < 0.01:
                    child[i] = 1 - child[i]

            newGeneration.append(child)
        population = newGeneration

    print(f"Best solution: {ranked[0]}, Fitness: {fitness(items, ranked[0], weightLimit)}, Weight: {sum([items[i][0]*ranked[0][i] for i in range(len(items))])}")