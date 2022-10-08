pokemons = list(map(int, input().split(" ")))
total_points = 0

while len(pokemons) > 0:
    index_to_remove = int(input())
    if index_to_remove < 0:
        removed_item = pokemons[0]
        pokemons[0] = pokemons[-1]
    elif index_to_remove > len(pokemons) - 1:
        removed_item = pokemons[-1]
        pokemons[-1] = pokemons[0]
    else:
        removed_item = pokemons.pop(index_to_remove)
    pokemons = list(map(
        lambda x: x + removed_item if x <= removed_item
        else x - removed_item, pokemons
                ))
    total_points += removed_item
print(total_points)