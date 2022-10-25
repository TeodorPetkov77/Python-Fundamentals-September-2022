population = list(map(int, input().split(", ")))
minimum_wage = int(input())

if sum(population) < minimum_wage * len(population):
    print("No equal distribution possible")
else:
    for index, person in enumerate(population):
        highest = population.index(max(population))
        while population[index] < minimum_wage:
            population[index] += 1
            population[highest] -= 1
            if population[highest] == minimum_wage:
                highest = population.index(max(population))
    print(population)

