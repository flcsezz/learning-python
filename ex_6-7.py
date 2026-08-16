people = [
    {
        'first' : 'gaurav',
        'last' : 'baghel',
        'age' : 19,
    },
    {
        'first' : 'jojo',
        'last' : 'bizzare',
        'age' : 21,
    },
    {
        'first' : 'noona',
        'last' : 'willson',
        'age' : 30 ,
    }

]



for people in people:
    firstn = f"{people['first']}  {people['last']}"
    
    agen = people['age']

    print(f'\tName:{firstn.title()}\n\tage : {agen}\n')