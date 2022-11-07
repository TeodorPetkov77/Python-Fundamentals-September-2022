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


# https://judge.softuni.org/Contests/Compete/Index/1740#9

# 10.	*Winning Ticket
# The lottery is exciting. However, checking a million tickets for winnings only by hand is not. So, you are given the task of creating a program that automatically checks if a ticket is a winner.
# You are given a collection of tickets separated by commas and spaces (one or many). You need to check each ticket to see if it has a winning combination of symbols:
# •	A valid ticket has exactly 20 characters.
# •	A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly repeated at least 6 times in both halves of the tickets.
# •	In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
# An example of a valid winning ticket:
# "Cash$$$$$$Ca$$$$$$sh"
# An example of a Jackpot winning valid ticket:
# "$$$$$$$$$$$$$$$$$$$$"
# Input
# The input will be read from the console. The input consists of a single line containing all tickets separated by commas and one or more white spaces in the format:
# •	"{ticket}, {ticket}, … {ticket}"
# Output
# Print the result for every ticket in the order of their appearance, each on a separate line in the format:
# •	If the ticket is invalid: "invalid ticket"
# •	If the ticket is valid, but it is not winning: "ticket "{ticket}" - no match"
# •	If the ticket is valid and winning, but not a Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"
# •	It the ticket hits the Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"
# Constrains
# •	Number of tickets will be in range [0 … 100]
# Examples
# Input	Output
# Cash$$$$$$Ca$$$$$$sh	ticket "Cash$$$$$$Ca$$$$$$sh" - 6$
# $$$$$$$$$$$$$$$$$$$$, aabb  , th@@@@@@eemo@@@@@@ey	ticket "$$$$$$$$$$$$$$$$$$$$" - 10$ Jackpot!
# invalid ticket
# ticket "th@@@@@@eemo@@@@@@ey" - 6@
# validticketnomatch:(, Cas$$$$$$$Ca$$$$$$s$	ticket "validticketnomatch:(" - no match
# ticket "Cas$$$$$$$Ca$$$$$$s$" - 6$