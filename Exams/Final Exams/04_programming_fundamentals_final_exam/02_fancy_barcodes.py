import re

pattern = re.compile('^@#+(?P<item>[A-Z][A-Za-z0-9]{4,}[A-Z])@#+')
num_pattern = re.compile('[0-9]+')

n = int(input())

for _ in range(n):
    barcode = input()
    if re.search(pattern, barcode):
        item_in_code = re.search(pattern, barcode).group('item')
        if re.findall(num_pattern, item_in_code):
            product_group = ''.join(re.findall(num_pattern, item_in_code))
        else:
            product_group = '00'
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')

