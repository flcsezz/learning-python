places = ['dholakpur', 'furfuri nagar','konoha','akiotan']
print(places)

nimo = sorted(places)
print(nimo)

print(f"Oringinal list still here {places}")

nimo = sorted(places, reverse=True)
print(nimo)

print(f"Oringinal list still here {places}")

places.reverse()
print(places)
places.reverse()
print(places)

places.sort()
print(f'sorted list {places}')

places.sort()
print(f"again chanager {places}")
