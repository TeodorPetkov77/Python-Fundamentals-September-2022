plunder_days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0

for day in range(1, plunder_days + 1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        total_plunder += daily_plunder / 2
    if day % 5 == 0:
        total_plunder *= 0.7

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only "
          f"{(total_plunder / expected_plunder * 100):.2f}% "
          f"of the plunder.")