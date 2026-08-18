sandwitch_orders = ['aalo','chalu', 'claude' ,'sandwitch', 'past', 'past', 'past']
finishd_orders = []

while 'past' in sandwitch_orders:
    sandwitch_orders.remove('past')

for fin in sandwitch_orders:
    finishd_orders.append(fin)
    print(f"i made your {fin.title()} sandwitch\n")

print('completed order today: \n')
for fin in finishd_orders:
    print(f"{fin.title()} sandwitch")
