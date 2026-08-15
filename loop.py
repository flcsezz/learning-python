my_pizza = ['garlic', 'new' , 'old' , 'momo']

friend_pizza = my_pizza[:]

my_pizza.append('holo')
friend_pizza.append('notholo')

print(my_pizza)
print(friend_pizza)

for pizza in my_pizza:
    print(pizza)

for pizza in friend_pizza:
    print(pizza)
