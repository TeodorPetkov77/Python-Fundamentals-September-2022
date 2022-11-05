food_gr = float(input()) * 1000
hay_gr = float(input()) * 1000
cover_gr = float(input()) * 1000
pig_weight = float(input()) * 1000

for i in range(1, 31):
    food_gr -= 300
    if i % 2 == 0:
        hay_gr -= food_gr * 0.05
    if i % 3 == 0:
        cover_gr -= pig_weight / 3
    if food_gr <= 0 or hay_gr <= 0 or cover_gr <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! Food: {(food_gr / 1000):.2f}, "
          f"Hay: {(hay_gr / 1000):.2f}, Cover: {(cover_gr / 1000):.2f}.")

# https://judge.softuni.org/Contests/Practice/Index/2031#0