cities= {
    'jab' : {
        'country' : 'india',
        'population' : '100',
        'fact'  : 'is good',
    },
    'backport' : {
        'country' : 'Outsude india',
        'population' : '1000',
        'fact'  : 'is good',
        
    },

}

for city, info in cities.items():
    print(f"\nThe city {city.title()} info is : ")
    for k, v in info.items():
        print(f"{k.title()} = {v.title()}")

    


