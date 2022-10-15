materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
shadowmourne = False
valanyr = False
dragonwrath = False

while shadowmourne is False and valanyr is False and dragonwrath is False:
    items = input().split(" ")
    for i in range(0, len(items), 2):
        item = items[i + 1].casefold()
        quantity = int(items[i])
        if item in materials:
            materials[item] += quantity
            if materials[item] >= 250:
                if item == "shards":
                    shadowmourne = True
                    materials[item] -= 250
                    print(f"Shadowmourne obtained!")
                    break
                elif item == "fragments":
                    valanyr = True
                    materials[item] -= 250
                    print(f"Valanyr obtained!")
                    break
                elif item == "motes":
                    dragonwrath = True
                    materials[item] -= 250
                    print(f"Dragonwrath obtained!")
                    break
            continue
        else:
            if item not in junk:
                junk[item] = 0
            junk[item] += quantity

print(f"shards: {materials['shards']}")
print(f"fragments: {materials['fragments']}")
print(f"motes: {materials['motes']}")

for key, value in junk.items():
    print(f"{key}: {value}")


