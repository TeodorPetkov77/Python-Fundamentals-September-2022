import re

pattern_customer = re.compile('(?<=%)[A-Z][a-z]+(?=%)')
pattern_product = re.compile('(?<=<)\w+(?=>)')
pattern_amount = re.compile('(?<=\|)[0-9]+(?=\|)')
pattern_price = re.compile('[0-9]+\.?[0-9]*(?=\$)')

total_income = 0

input_line = input()

while input_line != 'end of shift':
    if re.search(pattern_customer, input_line) and \
            re.search(pattern_product, input_line) and \
            re.search(pattern_amount, input_line) and \
            re.search(pattern_price, input_line):
        match_customer = re.search(pattern_customer, input_line).group()
        match_product = re.search(pattern_product, input_line).group()
        match_amount = int(re.search(pattern_amount, input_line).group())
        match_price = float(re.search(pattern_price, input_line).group())
        total_income += match_amount * match_price
        print(f'{match_customer}: {match_product} - {match_amount * match_price:.2f}')
        input_line = input()
    else:
        input_line = input()

print(f'Total income: {total_income:.2f}')