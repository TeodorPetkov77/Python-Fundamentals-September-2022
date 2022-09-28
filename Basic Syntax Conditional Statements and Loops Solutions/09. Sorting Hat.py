command = str(input())

while command != "Welcome!" and command != "Voldemort":
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")
    command = str(input())

if command == "Welcome!":
    print("Welcome to Hogwarts.")
elif command == "Voldemort":
    print("You must not speak of that name!")