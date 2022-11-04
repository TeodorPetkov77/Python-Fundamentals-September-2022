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

# https://judge.softuni.org/Contests/Practice/Index/1732#0

# 1.	Social Distribution
# A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what, and that is exactly what you are called to do for this problem.
# On the first line, you will be given the population (numbers separated by comma and space ", "). On the second line, you will be given the minimum wealth. You should distribute the wealth so that no part of the population has less than the minimum wealth. To do that, you should always take wealth from the wealthiest part of the population.
# There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible".
# Example
# Input	Output
# 2, 3, 5, 15, 75
# 5	[5, 5, 5, 15, 70]
# 2, 3, 5, 15, 75
# 20	[20, 20, 20, 20, 20]
# 2, 3, 5, 45, 45
# 30	No equal distribution possible