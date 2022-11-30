number_of_cars = int(input())
cars = {}

for _ in range(number_of_cars):
    command = input().split('|')
    car, distance, fuel = command[0], int(command[1]), int(command[2])
    if car not in cars.keys():
        cars[car] = {}
    cars[car]['distance'] = distance
    cars[car]['fuel'] = fuel

command = input()

while command != 'Stop':
    command = command.split(' : ')
    action = command[0]
    car = command[1]
    if action == 'Drive':
        distance, fuel = int(command[2]), int(command[3])
        if cars[car]['fuel'] >= fuel:
            cars[car]['fuel'] -= fuel
            cars[car]['distance'] += distance
            print(f'{car} driven for {distance} kilometers. '
                  f'{fuel} liters of fuel consumed.')
            if cars[car]['distance'] >= 100000:
                cars.pop(car)
                print(f'Time to sell the {car}!')
        else:
            print('Not enough fuel to make that ride')
    elif action == 'Refuel':
        fuel = int(command[2])
        if cars[car]['fuel'] + fuel > 75:
            print(f'{car} refueled with {75 - cars[car]["fuel"]} liters')
            cars[car]['fuel'] = 75
        else:
            cars[car]['fuel'] += fuel
            print(f'{car} refueled with {fuel} liters')
    elif action == 'Revert':
        kilometers = int(command[2])
        if cars[car]['distance'] - kilometers >= 10000:
            cars[car]['distance'] -= kilometers
            print(f'{car} mileage decreased by {kilometers} kilometers')
        else:
            cars[car]['distance'] = 10000
    command = input()

for key, value in cars.items():
    print(f'{key} -> Mileage: {value["distance"]} kms, Fuel in the tank: '
          f'{value["fuel"]} lt.')

