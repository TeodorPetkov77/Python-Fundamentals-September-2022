heroes = {}

n = int(input())

for _ in range(n):
    hero_list = input().split()
    hero_name, health, mana = hero_list[0], int(hero_list[1]), int(hero_list[2])
    if health > 100:
        health = 100
    if mana > 200:
        mana = 200
    if hero_name not in heroes.keys():
        heroes[hero_name] = {'health': 0, 'mana': 0}
    heroes[hero_name]['health'] = health
    heroes[hero_name]['mana'] = mana

command = input()

while command != 'End':
    command = command.split(' - ')
    action, hero_name = command[0], command[1]
    if action == 'CastSpell':
        mana_needed, spell_name = int(command[2]), command[3]
        if heroes[hero_name]['mana'] >= mana_needed:
            heroes[hero_name]['mana'] -= mana_needed
            print(f'{hero_name} has successfully cast {spell_name} '
                  f'and now has {heroes[hero_name]["mana"]} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')
    elif action == 'TakeDamage':
        damage, attacker = int(command[2]), command[3]
        if heroes[hero_name]['health'] > damage:
            heroes[hero_name]['health'] -= damage
            print(f'{hero_name} was hit for {damage} HP by {attacker} '
                  f'and now has {heroes[hero_name]["health"]} HP left!')
        else:
            print(f'{hero_name} has been killed by {attacker}!')
            heroes.pop(hero_name)
    elif action == 'Recharge':
        amount = int(command[2])
        if heroes[hero_name]['mana'] + amount > 200:
            amount_healed = 200 - heroes[hero_name]["mana"]
            heroes[hero_name]['mana'] = 200
        else:
            heroes[hero_name]['mana'] += amount
            amount_healed = amount
        print(f'{hero_name} recharged for {amount_healed} MP!')
    elif action == 'Heal':
        amount = int(command[2])
        if heroes[hero_name]['health'] + amount > 100:
            amount_healed = 100 - heroes[hero_name]["health"]
            heroes[hero_name]['health'] = 100
        else:
            amount_healed = amount
            heroes[hero_name]['health'] += amount
        print(f'{hero_name} healed for {amount_healed} HP!')
    command = input()

for key, value in heroes.items():
    print(f'{key}\n  HP: {value["health"]}\n  MP: {value["mana"]}')

# https://judge.softuni.org/Contests/Practice/Index/2303#2

# Problem 3 - Heroes of Code and Logic VII
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2303#0.
#
# You got your hands on the most recent update on the best MMORPG of all time – Heroes of Code and Logic. You want to play it all day long! So cancel all other arrangements and create your party!
# On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose for your party. On the next n lines, the heroes themselves will follow with their hit points and mana points separated by a single space in the following format:
# "{hero name} {HP} {MP}"
# -	HP stands for hit points and MP for mana points
# -	a hero can have a maximum of 100 HP and 200 MP
# After you have successfully picked your heroes, you can start playing the game. You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given.
# There are several actions that the heroes can perform:
# "CastSpell – {hero name} – {MP needed} – {spell name}"
# •	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
# o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
# •	If the hero is unable to cast the spell print:
# o	"{hero name} does not have enough MP to cast {spell name}!"
# "TakeDamage – {hero name} – {damage} – {attacker}"
# •	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
# o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
# •	If the hero has died, remove him from your party and print:
# o	"{hero name} has been killed by {attacker}!"
# "Recharge – {hero name} – {amount}"
# •	The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to 200. (the MP can't go over the maximum value).
# •	 Print the following message:
# o	"{hero name} recharged for {amount recovered} MP!"
# "Heal – {hero name} – {amount}"
# •	The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100), HP is increased to 100 (the HP can't go over the maximum value).
# •	 Print the following message:
# o	"{hero name} healed for {amount recovered} HP!"
# Input
# •	On the first line of the standard input, you will receive an integer n
# •	On the following n lines, the heroes themselves will follow with their hit points and mana points separated by a space in the following format
# •	You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given
# Output
# •	Print all members of your party who are still alive, in the following format (their HP/MP need to be indented 2 spaces):
# "{hero name}
#   HP: {current HP}
#   MP: {current MP}"
# Constraints
# •	The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative or exceed the respective limits.
# •	The HP/MP amounts in the commands will never be negative.
# •	The hero names in the commands will always be valid members of your party. No need to check that explicitly.
# Examples
# Input	Output
# 2
# Solmyr 85 120
# Kyrre 99 50
# Heal - Solmyr - 10
# Recharge - Solmyr - 50
# TakeDamage - Kyrre - 66 - Orc
# CastSpell - Kyrre - 15 - ViewEarth
# End	Solmyr healed for 10 HP!
# Solmyr recharged for 50 MP!
# Kyrre was hit for 66 HP by Orc and now has 33 HP left!
# Kyrre has successfully cast ViewEarth and now has 35 MP!
# Solmyr
#   HP: 95
#   MP: 170
# Kyrre
#   HP: 33
#   MP: 35
# Input	Output
# 4
# Adela 90 150
# SirMullich 70 40
# Ivor 1 111
# Tyris 94 61
# Heal - SirMullich - 50
# Recharge - Adela - 100
# CastSpell - Tyris - 1000 - Fireball
# TakeDamage - Tyris - 99 - Fireball
# TakeDamage - Ivor - 3 - Mosquito
# End	SirMullich healed for 30 HP!
# Adela recharged for 50 MP!
# Tyris does not have enough MP to cast Fireball!
# Tyris has been killed by Fireball!
# Ivor has been killed by Mosquito!
# Adela
#   HP: 90
#   MP: 200
# SirMullich
#   HP: 100
#   MP: 40