sandwitch_orders = ['aalo','chalu', 'claude' ,'sandwitch']
finishd_orders = []

for fin in sandwitch_orders:
    finishd_orders.append(fin)
    print(f"i made your {fin.title()} sandwitch\n")

print('completed order today: \n')
for fin in finishd_orders:
    print(f"{fin.title()} sandwitch")