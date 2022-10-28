def best_streak(ticket):
    streak = 0
    best_streak = 0
    temp_chars = ""
    for char in ticket:
        if not temp_chars:
            temp_chars += char
            streak += 1
            if best_streak < streak:
                best_streak = streak
            continue
        if temp_chars and char not in temp_chars:
            temp_chars = char
            streak = 1
            continue
        if temp_chars and char in temp_chars:
            temp_chars += char
            streak += 1
            if best_streak < streak:
                best_streak = streak
    return best_streak


tickets = [ticket.strip() for ticket in input().split(", ")]
index = 0

for ticket in tickets:
    uninterrupted_values = []

    winning = False
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    if ticket == "@@@@@@@@@@@@@@@@@@@@" \
            or ticket == "####################" \
            or ticket == "$$$$$$$$$$$$$$$$$$$$" \
            or ticket == "^^^^^^^^^^^^^^^^^^^^":
        winning_char = ticket[0]
        print(f'ticket "{ticket}" - 10{winning_char} Jackpot!')
        continue

    ticket_1 = ticket[0:(len(ticket) // 2)]
    ticket_2 = ticket[len(ticket) // 2:len(ticket) + 1]

    if "@@@@@@" in ticket_1 and "@@@@@@" in ticket_2:
        winning_char = "@"
        winning = True
    elif "######" in ticket_1 and "######" in ticket_2:
        winning_char = "#"
        winning = True
    elif "$$$$$$" in ticket_1 and "$$$$$$" in ticket_2:
        winning_char = "$"
        winning = True
    elif "^^^^^^" in ticket_1 and "^^^^^^" in ticket_2:
        winning_char = "^"
        winning = True
    if winning:
        uninterrupted_values.append(best_streak(ticket_1))
        uninterrupted_values.append(best_streak(ticket_2))
        print(f'ticket "{ticket}" - {min(uninterrupted_values)}{winning_char}')
    else:
        print(f'ticket "{ticket}" - no match')
