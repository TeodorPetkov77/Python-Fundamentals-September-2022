import re

tickets = [ticket.strip() for ticket in input().split(",")]

pattern = re.compile(r'(@{6,10}|#{6,10}|\${6,10}|\^{6,10})')

for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    try:
        ticket_part_1 = re.search(pattern, ticket[0:11]).group()
        ticket_part_2 = re.search(pattern, ticket[10:21]).group()
    except AttributeError:
        print(f'ticket "{ticket}" - no match')
        continue
    if len(ticket_part_1) + len(ticket_part_2) == 20:
        print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
    elif len(ticket_part_1) >= 6 and len(ticket_part_2) >= 6:
        uninterrupted_match_length = min([len(ticket_part_1), len(ticket_part_2)])
        print(f'ticket "{ticket}" - {uninterrupted_match_length}{ticket_part_1[0]}')

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