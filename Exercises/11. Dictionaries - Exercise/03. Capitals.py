countries = input().split(", ")
capitals = input().split(", ")

# capi_count = dict(zip(countries, capitals))

capi_count = {country: capital for country, capital in zip(countries, capitals)}

for key, value in capi_count.items():
    print(f"{key} -> {value}")

