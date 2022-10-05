pokemons = list(map(int, input().split(" ")))
list_of_removed_item = []

while len(pokemons) > 0:
    index_to_remove = int(input())
    if index_to_remove < 0:
        index_to_remove = 0
        removed_item = pokemons.pop(0)
        pokemons.insert(0, pokemons[len(pokemons) - 1])
    elif index_to_remove > len(pokemons) - 1:
        index_to_remove = len(pokemons) - 1
        removed_item = pokemons.pop(len(pokemons) - 1)
        pokemons.append(removed_item)
    else:
        removed_item = pokemons.pop(index_to_remove)
    pokemons = list(map(
        lambda x: x + removed_item if x <= removed_item
        else x - removed_item, pokemons
                ))
    list_of_removed_item.append(removed_item)
    print(pokemons)
print(sum(list_of_removed_item))