import re

pattern = re.compile(r'([=|/])(?P<country>[A-Z][A-Za-z]{2,})\1')
countries = input()
country_list = [i.group('country') for i in re.finditer(pattern, countries)]
travel_points = len("".join(country_list))

print(f"Destinations: {', '.join(country_list)}")
print(f"Travel Points: {travel_points}")